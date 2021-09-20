from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('approved-users/<int:users_id>', views.approvedUser, name='approve'),
    path('reject-users/<int:users_id>', views.rejectUser, name='reject'),
    
]