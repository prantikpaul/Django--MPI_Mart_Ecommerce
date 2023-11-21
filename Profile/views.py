from django.shortcuts import render
from Accounts.models import Profile

# Create your views here.
def user_profile(request):
    prof=Profile.objects.filter(user=request.user)



    return render (request,'profile/profile.html',locals())