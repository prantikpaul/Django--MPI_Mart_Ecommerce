from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import random
from .models import Profile
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def login(request):
    
    if request.user.is_authenticated:
         return redirect ('index')
    else:
         
    
        if request.method=='POST':
            Uname=request.POST['uname']
            Pass=request.POST['pass']
            login=auth.authenticate(username=Uname,password=Pass)
            if login:
                prof=Profile.objects.get(user=login) #profile er nam & user er nam same
                if prof.is_token_verified is True or prof.sign_in_otp_verify is True:
                    auth.login(request,login)
                    messages.success(request, "User Logged In")
                    return redirect('index')
                else:
                        messages.warning(request,'Please Verify Your Mail')
                        return redirect('verify_otp')
            else:
                    messages.warning(request,'Invalid Username or password')

    

    return render(request,'account/Log_In.html',locals())

def register(request):
    if request.user.is_authenticated:
         return redirect ('index')
    else:
        otpp = random.randint(111111,999999)
        if request.method=='POST':
            Fname=request.POST['fname']
            Lname=request.POST['lname']
            Uname=request.POST['uname']
            Email=request.POST['email']
            Pass=request.POST['pass']
            Cpass=request.POST['cpass']
            Add1=request.POST['add1']
            Add2=request.POST['add2']
            phone=request.POST['phn']
            print(Fname,Lname,Email,Uname,Pass,Cpass)
            if Pass==Cpass:
                if User.objects.filter(username=Uname).exists():
                        messages.warning(request, "⚠️ This Username is alreay taken")
                elif User.objects.filter(email=Email).exists():
                    messages.warning(request, "⚠️ This email is alreay taken")
                else:
                    
                    if len(Pass)>7:
                        
                        pp=User.objects.create(
                            first_name=Fname,
                            last_name=Lname,
                            username=Uname,
                            email=Email,
                            password=Pass,
                        )
                        pp.set_password(Pass)
                        pp.save()

                        auth_token = str(uuid.uuid4())

                        if Add2: # jodi Address 2 thake ->
                            pro_obj = Profile.objects.create(user=pp, auth_token=auth_token,otp=otpp,Address1=Add1,Address2=Add2,phone=phone) #creatig a profile on this user
                            pro_obj.save()
                            send_mail_registration(Email, auth_token,otpp)
                            return redirect ('verify_otp')
                        else:
                            pro_obj = Profile.objects.create(user=pp, auth_token=auth_token,otp=otpp,Address1=Add1,phone=phone) #creatig a profile on this user
                            pro_obj.save()
                            send_mail_registration(Email, auth_token,otpp)
                            return redirect ('verify_otp')
                    else:
                        messages.warning(request, "Password Must contain atleast 8 letters !!")
            else:
                    messages.warning(request, "Your Password Didn't Match !!")
                            
    

    return render(request,'account/Register.html',locals())

def send_mail_registration(Email, token,otpp):
    subject = "Account Verification link"
    message = f'hi click the link for verify http://127.0.0.1:8000/Accounts/verify_token/{token}\n\n\n Or You can use this OTP :{otpp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)

def verify_otp(request):
    if request.method=='POST':
        otpp = request.POST['otp']
        try:
            ppr=Profile.objects.get(otp=otpp)
            if ppr :
                ppr.sign_in_otp_verify= True
                ppr.save()
                messages.success(request,'Your Email Verified Successfully')
                return redirect ('login')
        except:
             messages.warning(request,'OTP Didn"t match ! Please Try Again ... ')
            

    
    return render(request,'account/verify_otp.html')
def verify(request, auth_token):
    #verify using auth token
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    profile_obj.is_token_verified = True
    profile_obj.save()
    messages.success(request, 'Your mail is verified')
    return redirect('login')

def logout(request):
    auth.logout(request)
    messages.success(request, "User Logged Out")
     

    return redirect ('index')

def forget_pass(request):
     otp=random.randint(111111,999999)
     if request.method=='POST':
        email=request.POST['email']

        if email :
            try:
                pp = User.objects.get(email=email) #email diye user name ber kora
                if pp:
                    print(pp)
                    rr = Profile.objects.get(user=pp) #username diye profile ber kora
                    rr.otp=otp
                    rr.save()
                    send_mail_forget_pass(email,otp)
                    
                    # print(rr)

                    return redirect('forget_pass_otp')

            except:
                messages.warning(request,"No User Found With This Email !!")
            

        
                
        else:
            messages.warning(request,"Please Enter An Email !")

     
     return render (request,'account/forget_pass.html',locals())

def send_mail_forget_pass(Email, otp):
    subject = "Password Reset OTP"
    message = f'Hi this is your OTP : {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)

def forget_pass_otp(request):
    
    if request.method=='POST':
        otp=request.POST['otp']

        if otp :
            try:
                get_prof=Profile.objects.get(otp=otp)
                if get_prof:
                    return redirect('forget_pass_confirm',get_prof.user.id)
            except:
                messages.warning(request,"OTP Didn't matached")

        else:
            messages.warning(request,"Please Enter Your OTP")

     


    return render(request,'account/forget_pass_otp.html',locals())

def forget_pass_confirm(request,id):
     if request.method=='POST':
        ppr=User.objects.get(id=id)
        Pass=request.POST['pass']
        Cpass=request.POST['cpass']
        if Pass and Cpass :
            if Pass==Cpass:
                if len(Pass)>7:
                    ppr.set_password(Pass)
                    ppr.save()
                    update_session_auth_hash(request,ppr)
                    messages.success(request,'Password Changed Successfully')
                    return redirect ('login')
                else:
                        messages.warning(request, "Password Must contain atleast 8 letters !!")
            else:
                messages.warning(request, "Your Password Didn't Match !!")
        else:
                messages.warning(request, "Please Enter Password !!")

     return render (request,'account/forget_pass_confirm.html',locals())