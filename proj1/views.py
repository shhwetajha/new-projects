from django.shortcuts import render

# Create your views here.

def create_party(request):
    return render(request,f'create_party.html')

