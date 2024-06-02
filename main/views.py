from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def contact_us(request):
    return render(request, 'main/contact_us.html')
