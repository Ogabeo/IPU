from django.shortcuts import render
from apps.resources.models import BakalavrYunalishlar, UqitiladiganFanlar, XalqaroHamkorliklar, XalqaroHamkorliklarRasm, IlmiyYangiliklar, IlmiyYangilikRasm
from django.views import View
from django.shortcuts import get_object_or_404


# Create your views here.
class XalqaroHamkorlikView(View):
    def get(self, request):
        xalqaro_faoliyatlar = XalqaroHamkorliklar.objects.all().order_by('-created_at')
        context={
          'xalqaro_faoliyatlar':xalqaro_faoliyatlar
        }
        return render(request, 'xalqaro_hamkorlik.html', context)
    
class XalqaroFaoliyatDetailView(View):
    def get(self, request, slug):
        muayyan_xalqaro_yangilik = get_object_or_404(XalqaroHamkorliklar, slug=slug)
        context = {
            'muayyan_xalqaro_yangilik': muayyan_xalqaro_yangilik
        }
        return render(request, 'xalqaro_faoliyat_detail.html', context)

class ResourceTypeResourcesView(View):
    pass

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

class IlmiyFaoliyatView(View):
    def get(self, request):
        ilmiy_yangiliklar = IlmiyYangiliklar.objects.all().order_by('-created_at')
        context={
            'ilmiy_yangiliklar':ilmiy_yangiliklar
        }
        return render(request, 'ilmiy_faoliyat.html', context)

class IlmiyFaoliyatDetailView(View):
    def get(self, request, slug):
        muayyan_ilmiy_yangilik = get_object_or_404(IlmiyYangiliklar, slug=slug)
        context = {
            'muayyan_ilmiy_yangilik': muayyan_ilmiy_yangilik
        }
        return render(request, 'ilmiy_faoliyat_detail.html', context)

    
class UquvFaoliyatiView(View):
    def get(self, request):
        yunalishlar = BakalavrYunalishlar.objects.all()
        fanlar = UqitiladiganFanlar.objects.all()
        context = {
            'yunalishlar':yunalishlar,
            'fanlar':fanlar
        }
        return render(request, "uquv_faoliyati.html", context)
    
