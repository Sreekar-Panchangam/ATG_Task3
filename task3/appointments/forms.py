from django import forms
from .models import Book
from accounts.models import User
from posts.models import Post

class BookingForm(forms.Form):
    eventTitle = forms.CharField(label="event", max_length=255, required=True)
    startDateTime = forms.DateTimeField(label="startDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)
    endDateTime = forms.DateTimeField(label="endDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)
