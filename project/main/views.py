from django.shortcuts import render

# Create your views here.
def firstpage(request):
    return render(request, 'main/firstpage.html')

def secondpage(request):
    return render(request, 'main/secondpage.html')  