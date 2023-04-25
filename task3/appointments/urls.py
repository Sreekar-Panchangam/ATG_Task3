from django.urls import path
from . import views

app_name='appointments'

urlpatterns = [
    path('',views.doctor,name='doctor'),
    path('confirm',views.confirm,name='confirm'),
    path('done',views.done,name='done'),
    path('bookform/<str:pk>/',views.bookform,name='bookform'),
]
