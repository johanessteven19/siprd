from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('approved-users/<int:id>', views.approved_user, name='approve'),
    path('reject-users/<int:id>', views.reject_user, name='reject'),
    
]