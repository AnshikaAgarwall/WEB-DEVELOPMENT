from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


  

# Create your views here.
def HomePage(request):
    return render(request , "HOME.html",)
def LoginPage(request):
    if request.method=="POST" and 'subBtn2' in request.POST:
      print("Button 1 clicked .....", request.POST)
      print(request.POST.get('nm'))
      print(request.POST.get('pwd')) 
      user=authenticate(request,d_name='nm',d_email='email')
      if user is not None:
          login(request,user)
          return HttpResponseRedirect('home')
    
    return render(request, "LOGIN.html" )

@login_required(login_url='/login')
def Availability(request):
    return render(request,"AVAILABLE.html")
def ContactPage(request):
    return render(request,"CONTACT.html")
# def mydemo(request):
#     data=[{'dname':"sachin",'dgroup':"A+",'date':'12-09-2024','amt':'1Lt'},
#              {'dname':"rahul",'dgroup':"B+",'date':'12-09-2024','amt':'1Lt'},
#              {'dname':"shivi",'dgroup':"AB+",'date':'12-09-2024','amt':'1Lt'},
#              {'dname':"hari",'dgroup':"AB-",'date':'12-09-2024','amt':'1Lt'},
#              {'dname':"altamash",'dgroup':"A+",'date':'12-09-2024','amt':'1Lt'}]
#     context={"userdata":data}
#     return render(request,"COUNTS.html",context)

def RegisterPage(request):
    
    if request.method=="POST" and 'subBtn3' in request.POST:
      print(request.POST)
      user=DONOR_DATA(
        d_name=(request.POST.get('nm')),
        d_email=(request.POST.get('email')),
        d_mother=(request.POST.get('mother')),
        d_father=(request.POST.get('father')),
        d_dob=(request.POST.get('dob')),
        d_gender=(request.POST.get('g')),
        d_weight=(request.POST.get('w')),
        d_bloodgroup=(request.POST.get('bg')),
        d_adhar=(request.POST.get('adhar')),
        d_uadhar=(request.FILES.get('uadhar'))
       
        )
      user.save()
    return render(request, "REGISTER.html" )

def ShowHeroes(request):
   alldonors=None
   if request.method=="POST" and 'showBtn6' in request.POST:
       alldonors=DONOR_DATA.objects.values() 
       print(alldonors)      
       return render(request,"show.html",{'data':alldonors})
       
   return render(request,"show.html")

@login_required(login_url='/login')
def EditRecord(request,D_id):
    if request.method=="POST" and 'subBtn7' in request.POST:
        donordata=DONOR_DATA.objects.get(id=D_id)
        donordata.d_mother=request.POST.get('mother')
        donordata.save()
        return HttpResponseRedirect('/showall')
    editdonors=DONOR_DATA.objects.get(id=D_id) 
    print(editdonors)

    return render(request,"EDITPAGE.html",{'data1':editdonors}) 

def Cards(request):
    return render(request , "CARDS.html")

def AboutUs(request):
    return render(request , "ABOUTUS.html")

# def NewReg(request):
#     if request.method=="POST" and 'subBtn8' in request.POST:
#        password=request.POST.get('')
#        re_adharno=request.POST.get('re_adhar')
#        if adharno == re_adharno:
#             user= User.objects.create_user(
#                username=request.POST.get('dnm'),
#                password=request.POST.get('demail'),
               
#             )
#             user.save()

#     return render(request , "NEWREG.html")  
def Logout(request):
    logout(request)
      
    return HttpResponseRedirect("/login")



def blood_availability(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        blood_group = request.POST.get('blood_group')

        if city and blood_group:
            blood_donations = BloodDonation.objects.filter(city=city, blood_group=blood_group)
        else:
            blood_donations = None

        return render(request, 'Availability.html', {'donations': BloodDonation.objects.all(), 'blood_donations': blood_donations})
    
    return render(request, 'Availability.html', {'donations': BloodDonation.objects.all()})