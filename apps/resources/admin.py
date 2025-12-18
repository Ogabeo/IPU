from django.contrib import admin
from apps.resources.models import BakalavrYunalishlar, IlmiyYangiliklar, IlmiyYangilikRasm, XalqaroHamkorliklar, XalqaroHamkorliklarRasm
# Register your models here.



    
class IlmiyYangilikRasmInline(admin.TabularInline):
    model = IlmiyYangilikRasm
    extra = 1  
    fields = ('image', 'alt_text',)
    readonly_fields = ()
    show_change_link = True

@admin.register(IlmiyYangiliklar)
class IlmiyYangiliklarAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'slug']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description']
    inlines = [IlmiyYangilikRasmInline]

    class Meta:
        verbose_name = 'ilmiy yangilik'
        verbose_name_plural = 'ilmiy yangiliklar'







class XalqaroHamkorliklarRasmInline(admin.TabularInline):
    model = XalqaroHamkorliklarRasm
    extra = 1  # yangi rasm qo'shish uchun bo'sh satrlar
    fields = ('image', 'alt_text',)
    readonly_fields = ()
    show_change_link = True

@admin.register(XalqaroHamkorliklar)
class XalqaroHamkorliklarAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'slug']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description']
    inlines = [XalqaroHamkorliklarRasmInline]

    class Meta:
        verbose_name = 'xalqaro hamkorlik'
        verbose_name_plural = 'xalqaro hamkorliklar'

@admin.register(BakalavrYunalishlar)
class BakalavrYunalishlarAdmin(admin.ModelAdmin):
    list_display=('id', 'shifr', 'yunalish_nomi')
    list_display_links = ('id', 'shifr', 'yunalish_nomi')
    