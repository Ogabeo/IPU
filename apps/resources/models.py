from django.db import models
from apps.common.models import BaseModel
from django.utils.text import slugify
# Create your models here.










class IlmiyYangiliklar(BaseModel):
    title = models.CharField(max_length=300)
    created_at = models.TimeField(auto_now=True)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'ilmiy_yangilik'
        verbose_name_plural = "ilmiy_yangiliklar"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# Bitta yangilikka bir nechta rasm qo‘shish uchun
class IlmiyYangilikRasm(models.Model):
    yangilik = models.ForeignKey(IlmiyYangiliklar, 
                                 on_delete=models.CASCADE,
                                 related_name='rasmlar')
    image = models.ImageField(upload_to='ilmiy_yangiliklar/')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.yangilik.title} - rasm"











class XalqaroHamkorliklar(BaseModel):
    title = models.CharField(max_length=300)
    created_at = models.TimeField(auto_now=True)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'xalqaro hamkorlik'
        verbose_name_plural = "xalqaro hamkorliklar"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# Bitta yangilikka bir nechta rasm qo‘shish uchun
class XalqaroHamkorliklarRasm(models.Model):
    yangilik = models.ForeignKey(XalqaroHamkorliklar, 
                                 on_delete=models.CASCADE,
                                 related_name='rasmlar')
    image = models.ImageField(upload_to='ilmiy_yangiliklar/')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.yangilik.title} - rasm"
    














class BakalavrYunalishlar(BaseModel):
    shifr = models.CharField(max_length=20, null=False, blank=False)
    yunalish_nomi = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.shifr} - {self.yunalish_nomi}"
    
    class Meta:
        verbose_name = "yo'nalish"
        verbose_name_plural = "yo'nalishlar"

class UqitiladiganFanlar(BaseModel):
    title = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'fan'
        verbose_name_plural = 'fanlar'
    
