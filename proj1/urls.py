from django.urls import path
from .import views

app_name="party"

urlpatterns=[
    path("create_party/",views.create_party,name="create_party")
]