from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Users

responses = {}
def index(request):
    users = Users.objects.all()
    responses['users'] = users
    return render(request, 'adminfeatures/userlist.html', responses)

def approvedUser(request, users_id):
    users = Users.objects.all()

def rejectUser(request, users_id):
    users = Users.objects.all()
