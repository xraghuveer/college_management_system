from django.shortcuts import render,redirect
from cmsapp.models import Staff , Staff_Notification ,Staff_Leave
from django.contrib import messages


def HOME(request):
    return render(request,'Staff/home.html')


def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id=staff_id)

        context = {
            'notification':notification,
        }
    return render(request,'Staff/notification.html',context)


def STAFF_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')


def STAFF_APPLY_LEAVE(request):
    return render(request,'Staff/apply_leave.html')


def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_Leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request,'Leave Applied Successfully')
        return redirect('staff_apply_leave')