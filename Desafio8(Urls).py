from django.urls import path
from django.urls import views
from django.http import HttpResponse

def outra_view(request):
    return HttpResponse("Outra view funcionando!")
    
urlpatterns = [
    path('ola/', views.saudacao),
    path('outra/', views.outra_view),
 ]