import random
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView
from apps.home.models import Elonlar, Worker, Adabiyotlar, Fan, Fan_tarkibi, Yangiliklar, UslubiyNashr, Videodarslik, Loyiha, IlmiyNashr, AvtoReferat , Sertificate
from django.core.paginator import Paginator
from django.db.models import Q 
import random


class HomePageView(View):
    def get(self, request):
        recent_7 = Elonlar.objects.filter(is_active=True).order_by('-data')[:7]
        elonlar = random.sample(list(recent_7), min(4, len(recent_7)))
        yangiliklar = Yangiliklar.objects.filter(is_active=True).order_by('?')
        xodimlar = Worker.objects.all()
      
        context = {
            'elonlar':elonlar,
            'xodimlar': xodimlar,
            'yangiliklar': yangiliklar,
            
        }
        return render(request, 'home.html', context)

    
class KafedraXodimlari(View):
    def get(self, request):
        xodimlar = Worker.objects.all()
        kafedra_xodimi=xodimlar.first()
        context ={
            'kafedra_xodimi':kafedra_xodimi,
            'xodimlar':xodimlar
        }
        return render(request, 'kafedra_xodimlari.html', context)

class MuayyanXodim(View):
    def get(self, request, slug):
        xodim = get_object_or_404(Worker, slug=slug)  
        uslubiy_nashrlar = UslubiyNashr.objects.filter(authors = xodim)
        ilmiy_nashrlar = IlmiyNashr.objects.filter(authors = xodim)
        avtoreferatlar = AvtoReferat.objects.filter(authors = xodim)
        sertifikatlar = Sertificate.objects.filter(authors = xodim)
        loyihalar = Loyiha.objects.filter(authors = xodim)
        videodarsliklar = Videodarslik.objects.filter(authors=xodim)
        context = {
            
            'xodim': xodim,
            'uslubiy_nashrlar':uslubiy_nashrlar,
            'ilmiy_nashrlar':ilmiy_nashrlar,
            'avtoreferatlar':avtoreferatlar,
            'sertifikatlar':sertifikatlar,
            'loyihalar':loyihalar,
            'videodarsliklar':videodarsliklar
        }
        return render(request, 'xodim_detail.html', context)
class YangilikView(View):
    def get(self, request, slug):
        yangilik = get_object_or_404(Yangiliklar, slug=slug)
        
        context ={
            'yangilik':yangilik
        }
        return render(request, 'yangilik_detail.html', context)
class ElonView(View):
    def get(self, request, slug):
        elon = get_object_or_404(Elonlar, slug=slug)
        
        context ={
            'elon':elon
        }
        return render(request, 'elon_detail.html', context)

    
class ElonlarView(ListView):
    model = Elonlar
    template_name = 'elonlar_listi.html'
    context_object_name = 'elonlar'
    paginate_by = 10
    PAGINATION_URL = ''
    def get_queryset(self):
        queryset = Elonlar.objects.filter(is_active=True).order_by('?')  # Base queryset

        # Get search query from request.GET (modify as needed)
        search_query = self.request.GET.get('search', '')
        if search_query:
            self.PAGINATION_URL = f'&search={search_query}'  
            queryset = queryset.filter(Q(title__icontains=search_query) |
                                       Q(short_description__icontains = search_query))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')  
        context['pagination_url'] = self.PAGINATION_URL
        elonlar = self.object_list
        paginator = Paginator(elonlar, self.paginate_by)
        page_number = self.request.GET.get('page', 1)  # Get current page from GET
        page_obj = paginator.get_page(page_number)
            # Update context with pagination information
        context['page_obj'] = page_obj
        context['is_paginated'] = paginator.num_pages > 1

        return context












































class FanListView(ListView):
    model = Fan
    template_name = 'fanlar.html'
    context_object_name = 'fanlar'
    paginate_by = 16
    PAGINATION_URL = ''

    def get_queryset(self):
        queryset = Fan.objects.filter(is_active=True).order_by('?')  # Base queryset

        # Get search query from request.GET (modify as needed)
        search_query = self.request.GET.get('search', '')
        if search_query:
            self.PAGINATION_URL = f'&search={search_query}'  
            queryset = queryset.filter(title__icontains=search_query)

        # Add additional filters based on request.GET parameters (modify as needed)
        filter_by_category = self.request.GET.get('talim_shakli', '')
        if filter_by_category:
          
            self.PAGINATION_URL += f'&talim_shakli={filter_by_category}'  
            queryset = queryset.filter(talim_shakli=filter_by_category)
            
            
        filter_by_type = self.request.GET.get('course', '')
        if filter_by_type:
            self.PAGINATION_URL += f'&kurs={filter_by_type}'
            queryset = queryset.filter(course=filter_by_type)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')  # Pass search query to template
        context['filter_by_category'] = self.request.GET.get('category', '')  # Pass filter value to template
        context['filter_by_type'] = self.request.GET.get('resourceType', '')  
        context['pagination_url'] = self.PAGINATION_URL
        resources = self.object_list
        paginator = Paginator(resources, self.paginate_by)
        page_number = self.request.GET.get('page', 1)  # Get current page from GET
        page_obj = paginator.get_page(page_number)
            # Update context with pagination information
        context['page_obj'] = page_obj
        context['is_paginated'] = paginator.num_pages > 1

        return context

class AdabiyotlarView(View):
    def get(self, request, slug):
        fan = Fan.objects.get(slug=slug)
        adabiyotlar = Adabiyotlar.objects.filter(specific_subject = fan)
        context={
            'adabiyotlar':adabiyotlar
        }
        return render(request, 'adabiyotlar.html', context)

class FanTarkibiView(View):
    def get(self, request, slug):
        fan = Fan.objects.get(slug=slug)
        fan_tarkiblari = Fan_tarkibi.objects.filter(subject_name = fan)
        context={
            'fan':fan,
            'fan_tarkiblari':fan_tarkiblari
        }
        return render(request, 'fan_tarkibi.html', context)










