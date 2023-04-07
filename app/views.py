from django.shortcuts import render

# Create your views here.
 
def mdb4(request):
    return render(request,'mdb4.html')


def child_mdb4(request):
    return render(request,'child_mdb4.html') 