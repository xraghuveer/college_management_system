from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cmsapp.models import Course,Session_Year,CustomUser,Student,Staff
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    return render(request,'HOD/home.html')

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name  + " " +  user.last_name + " is " + "Added Successfully !")
            return redirect('add_student')

    context = {
        'course':course,
        'session_year':session_year,
    }

    return render(request,'HOD/add_student.html',context)


def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request,'HOD/view_student.html',context)


def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student': student,
        'course' : course,
        'session_year' : session_year,
    }
    return render(request,'HOD/edit_student.html',context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password is not None and password != "":
            user.set_password(password)
        if profile_pic is not None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender
        course = Course.objects.get(id = course_id)
        student.course_id = course
        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Records Are Successfully Updated !')
        return redirect('view_student')

    return render(request,'HOD/edit_student.html')


def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request, 'Records Are Successfully Deleted !')
    return redirect('view_student')


def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request, "Course Successfully Added !")
        return redirect("add_course")
    return render(request, 'HOD/add_course.html')


def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course' :course,
    }
    return render(request, 'HOD/view_course.html',context)


def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)

    context = {
        'course' :course,
    }
    return render(request, 'HOD/edit_course.html',context)


def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')


        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course Updated !')
        return redirect('view_course')



    return render(request, 'HOD/edit_course.html')


def DELETE_COURSE(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course Deleted Successfully')
    return redirect('view_course')


def ADD_STAFF(request):
    if request.method=='POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Already Exists ! ')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Taken ! ')
            return redirect('add_staff')
        else:
            user = CustomUser(first_name = first_name,last_name=last_name,email=email,username=username,profile_pic=profile_pic,user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender
            )
            staff.save()
            messages.success(request,'Staff Added Successfully ! ')
            return redirect('add_staff')

    return render(request, 'HOD/add_staff.html')


def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff':staff,
    }
    return render(request,'HOD/view_staff.html',context)


def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id = id)

    context = {
        'staff':staff,
    }
    return render(request, 'HOD/edit_staff.html',context)


def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id = staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password is not None and password != "":
            user.set_password(password)
        if profile_pic is not None and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address

        user.save()
        messages.success(request, "Staff is Successfully Updated")
        return  redirect('view_staff')

        return render(request, 'HOD/edit_staff.html')