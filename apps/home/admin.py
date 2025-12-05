from django.contrib import admin
from apps.home.models import Elonlar, Worker, Yangiliklar, UslubiyNashr, Videodarslik, Loyiha, IlmiyNashr, AvtoReferat, Sertificate
from apps.home.models import MeyoriyHujjat, Fan, Fan_tarkibi, Adabiyotlar
# Register your models here.





@admin.register(MeyoriyHujjat)
class MeyoriyHujjatAdmin(admin.ModelAdmin):
    list_display=['id','title', 'file_link']
    list_display_links = ['id', 'title']
    search_fields =['title']

    class Meta:
        verbose_name = "Me'yoriy hujjat"
        verbose_name_plural = "Me'yoriy hujjatlar"

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'meyoriy_hujjat', 'talim_shakli', 'course']
    list_display_links = ['id', 'title', 'talim_shakli']
    search_fields = ['title']
    list_filter = ['meyoriy_hujjat', 'course', 'talim_shakli']

    class Meta:
        verbose_name = 'fan'
        verbose_name_plural = 'fanlar'

@admin.register(Fan_tarkibi)
class FanTarkibiAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subject_name']
    list_display_links =['id', 'title']
    search_fields = ['title']
    list_filter = ['subject_name__talim_shakli', 'subject_name__course']

    class Meta:
        verbose_name = 'fan tarkibi'
        verbose_name_plural = 'fan tarkiblari'
@admin.register(Adabiyotlar)
class AdabiyotlarAdmin(admin.ModelAdmin):
    list_display=['id', 'specific_subject', 'total_name']
    list_display_links = ['id', 'specific_subject']
    search_fields = ['specific']
    class Meta:
        verbose_name = 'adabiyot'
        verbose_name_plural = "adabiyotlar"

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'familiya', 'otchestva', 'email_address']
    list_display_links = ['id', 'ism', 'familiya', 'otchestva']

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'
@admin.register(Yangiliklar)
class YangilikAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'description']
    list_display_links=['id', 'title']

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

@admin.register(UslubiyNashr)
class UslubiyNashrAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year', 'pdf_nomi', 'get_authors', 'extra_authors', 'document_link']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'year', 'authors__ism', 'authors__familiya', 'extra_authors']
    list_filter = ['year', 'authors']
    filter_horizontal = ('authors',)  # ko‘p mualliflarni tanlash uchun
    
    def get_authors(self, obj):
        """Bazadagi mualliflarni vergul bilan chiqaradi"""
        return ", ".join([str(author) for author in obj.authors.all()])
    class Meta:
        verbose_name = 'Uslubiy nashr'
        verbose_name_plural = 'Uslubiy nashrlar'

@admin.register(Sertificate)
class SertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','pdf_nomi', 'year', 'document_link', 'photo']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'year']
    list_filter = ['year', 'authors']

    class Meta:
        verbose_name="sertifikat"
        verbose_name_plural = "sertifikatlar"

@admin.register(Videodarslik)
class VideodarslikAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year', 'document_link']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'year']
    list_filter = ['year', 'authors']

    class Meta:
        verbose_name="videodarslik"
        verbose_name_plural = "videodarsliklar"

@admin.register(Loyiha)
class LoyihaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year', 'document_link']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'year']
    list_filter = ['year', 'authors']

    class Meta:
        verbose_name="loyiha"
        verbose_name_plural = "loyihalar"

@admin.register(IlmiyNashr)
class IlmiyNashrAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year', 'doi', 'jurnal_nomi', 'sahifalar_soni', 'get_authors', 'extra_authors', 'document_link']
    list_display_links = ['id', 'title', 'doi']
    search_fields = ['title', 'year', 'authors__ism', 'authors__familiya', 'extra_authors']
    list_filter = ['year', 'authors']
    filter_horizontal = ('authors',)  # ko‘p mualliflarni tanlash uchun
    
    def get_authors(self, obj):
        """Bazadagi mualliflarni vergul bilan chiqaradi"""
        return ", ".join([str(author) for author in obj.authors.all()])
    
    class Meta:
        verbose_name = 'Ilmiy nashr'
        verbose_name_plural = 'Ilmiy nashrlar'


@admin.register(AvtoReferat)
class AvtoReferatAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year', 'pdf_nomi', 'get_authors', 'extra_authors', 'document_link']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'year', 'authors__ism', 'authors__familiya', 'extra_authors']
    list_filter = ['year', 'authors']
    filter_horizontal = ('authors',) 
    
    def get_authors(self, obj):
       
        return ", ".join([str(author) for author in obj.authors.all()])
    class Meta:
        verbose_name = 'Avtoreferat'
        verbose_name_plural = 'Avtoreferatlar'

@admin.register(Elonlar)
class ElonlarAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'short_description', 'data', 'time']
    list_display_links=['id', 'title']
    search_fields=['title', 'short_description', 'description']
    list_filter=['data', 'time']
    

    class Meta:
        verbose_name="e'lon"
        verbose_name_plural = "e'lonlar"