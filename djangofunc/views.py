from django.shortcuts import render
# hi I am here

def view_create_party(request):
    return render(request,"create_party.html")