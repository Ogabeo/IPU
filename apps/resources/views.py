from django.shortcuts import render
from apps.resources.models import BakalavrYunalishlar, XalqaroHamkorliklar, XalqaroHamkorliklarRasm, IlmiyYangiliklar, IlmiyYangilikRasm
from django.views import View
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q 

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

class IlmiyYangiliklarView(ListView):
    model = IlmiyYangiliklar
    template_name = 'ilmiy_yangiliklar_listi.html'
    context_object_name = 'ilmiy_yangiliklar'
    paginate_by = 8
    PAGINATION_URL = ''
    def get_queryset(self):
        queryset = IlmiyYangiliklar.objects.filter(is_active=True).order_by('?')  # Base queryset

        # Get search query from request.GET (modify as needed)
        search_query = self.request.GET.get('search', '')
        if search_query:
            self.PAGINATION_URL = f'&search={search_query}'  
            queryset = queryset.filter(Q(title__icontains=search_query) |
                                       Q(description__icontains = search_query))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')  
        context['pagination_url'] = self.PAGINATION_URL
        ilmiy_yangiliklar = self.object_list
        paginator = Paginator(ilmiy_yangiliklar, self.paginate_by)
        page_number = self.request.GET.get('page', 1)  # Get current page from GET
        page_obj = paginator.get_page(page_number)
            # Update context with pagination information
        context['page_obj'] = page_obj
        context['is_paginated'] = paginator.num_pages > 1

        return context


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
        
        context = {
            'yunalishlar':yunalishlar,
            
        }
        return render(request, "uquv_faoliyati.html", context)
    
