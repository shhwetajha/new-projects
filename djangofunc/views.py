from django.shortcuts import render

def view_create_party(request):
    return render(request,"create_party.html")