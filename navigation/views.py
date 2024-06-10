from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'navigation/about.html')
    
def context(request):
    return render(request,'navigation/context.html')

def services(request):
    return render(request,'navigation/services.html')