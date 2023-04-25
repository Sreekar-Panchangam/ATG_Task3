from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import get_object_or_404
import sys
import time
from django.db.models import Q
import datetime
from datetime import timedelta
import pytz
from apiclient.discovery import build
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from . import models
from accounts.models import User
from posts.models import Post
from posts.models import Post
from . import forms
from .forms import BookingForm

scopes = ['https://www.googleapis.com/auth/calendar']

credentials = pickle.load(open("token.pkl","rb"))

from django.contrib.auth import get_user_model
User = get_user_model()

start_time =0
end_time=0

def doctor(request):
    form = User.objects.filter(is_doctor='True')
    print(form)
    return render(request,'appointments/doctors.html',{'form':form})

def bookform(request,pk):
    form = User.objects.get(id=pk)
    if request.method == 'POST':
        form = User.objects.get(id=pk)
        req = request.POST['req']
        start = request.POST['start']
        time = request.POST['time']
        email = request.POST['email']
        starts = start +' '+ time +':' '00'

        start_time = datetime.datetime.strptime(starts,"%Y-%m-%d %H:%M:%S")
        end_time  = start_time + timedelta(minutes=45)
        context = { 'req':req,'start':start,'time':time,'start_time':start_time, 'end_time':end_time,'email':email,'form':form}
        return  render(request, 'appointments/confirm.html',context)
    return render(request,'appointments/bookform.html',{'form':form})

def confirm(request):
    service = build("calendar", "v3", credentials=credentials)
    if request.method == 'POST':
        req = request.POST['required']
        start = request.POST['starts']
        time = request.POST['time']
        email = request.POST['email']
        start = start +' '+ time +':' '00'
        start_time = datetime.datetime.strptime(start,"%Y-%m-%d %H:%M:%S")
        end_time  = start_time + timedelta(minutes=45)
        timezone = 'Asia/Kolkata'
        print("Gsfgfd",start_time.isoformat(),'vdfdf',end_time.isoformat())
        print("dsdv",req)
        print("Gfdg",email),
        start_time_2 = start_time + timedelta(minutes=30,hours=5)
        end_time_2 = end_time + timedelta(minutes=30,hours=5)
        event = (
        service.events()
        .insert(
            calendarId="primary",
            body={
                    "summary": req,
                    "start": {"dateTime": start_time_2.isoformat(),'timeZone': timezone,},
                    "end": {"dateTime": end_time_2.isoformat(),'timeZone': timezone,},
                    "attendees":[{"email":email}]
                },
              )
        .execute()
         )
        return render(request,'appointments/done.html')
    return render(request,'appointments/confirm.html')

def done():
    return render(request,'appointments/done.html')
