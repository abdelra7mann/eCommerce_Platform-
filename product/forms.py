from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# اول حاجه بروح استدعي يوزر و يوزر كريات فورم 
# تاني حاجه بكريت كلاس جديد وبديها ف الباراميتر اليوزر كريات ال استعديتها 
#  تالت حاجه بعمل جوا كلاس ميتا بديله اليوزر ال استدعيته برضه 
# رابع حاجه بعمل الفيلد ال انا عاوز ابعتها لصفحه التمبلت 



class Regesterion(UserCreationForm):
     class Meta():  
         model = User
         fields = ('username','first_name','last_name','email','password1','password2')
    