from django.urls import path
from . import views


app_name = 'resources'
urlpatterns = [
    path('ilmiy_faoliyat/', views.IlmiyFaoliyatView.as_view(), name='ilmiy_faoliyat'),
    path('uquv_faoliyati/', views.UquvFaoliyatiView.as_view(), name='uquv_faoliyati'),
    path('xalqaro_hamkorlik/', views.XalqaroHamkorlikView.as_view(), name = 'xalqaro_hamkorlik'),
    path('ilmiy_faoliyat-detail/<slug:slug>/', views.IlmiyFaoliyatDetailView.as_view(), name='ilmiy_detail'),
    path('xalqaro_faoliyat_detail/<slug:slug>/,', views.XalqaroFaoliyatDetailView.as_view(), name='xalqaro_detail')
    ]

from django.shortcuts import render
from django.http import Http404

def my_view(request):
    raise Http404  

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)