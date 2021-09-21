from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from .models import Users

responses = {}
def index(request):
    users = Users.objects.all()
    # users1 = Users.objects.get(users_id=4)
    # users1.users_status = 'pending'
    # users1.save()
    responses['users'] = users
    return render(request, 'adminfeatures/userlist.html', responses)

def approved_user(request, id):
    users = Users.objects.get(users_id=id)
    users.users_status = 'accepted'
    users.save()
    return JsonResponse({'status':'ok'})

def reject_user(request, id):
    users = Users.objects.get(users_id=id)
    users.users_status = 'rejected'
    users.save()
    return JsonResponse({'status':'ok'})
