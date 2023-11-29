from django.shortcuts import render

# Create your views here.
def boostrap_cdn(request):
    return render(request,'boostrap_cdn.html')