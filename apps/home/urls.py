from django.urls import path
from .views import FanListView, ElonView, MuayyanXodim, QidiruvNatijalariView, FanTarkibiView, AdabiyotlarView, ElonlarView, YangilikView, HomePageView, KafedraXodimlari


app_name = "home"
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path("komputer-tizimlari-kafedrasi/", KafedraXodimlari.as_view(), name="kafedra_xodimlar"),
    path("members/<slug:slug>/", MuayyanXodim.as_view(), name='muayyan_xodim'),
    path('yangilik_detail/<slug:slug>/', YangilikView.as_view(), name='yangilik_detail'),
    path('news/<slug:slug>/', ElonView.as_view(), name='elon'),
    path('news/', ElonlarView.as_view(), name='elonlar'),
    path('fanlar/', FanListView.as_view(), name='fanlar'),
    path('fan/<slug:slug>/', FanTarkibiView.as_view(), name='fan_tarkibi'),
    path('fan/<slug:slug>/adabiyotlar/', AdabiyotlarView.as_view(), name='adabiyotlar'),
    path('search/', QidiruvNatijalariView.as_view(), name='search_results'),
]
