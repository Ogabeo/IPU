from django.db import models
from apps.common.models import BaseModel
from django.utils.text import slugify


# Create your models here.


    
from django.db import models

class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Worker(BaseModel):
    photo = models.ImageField(upload_to='xodimlar/', verbose_name='xodimning_rasmi', null=True, blank=True)
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    otchestva = models.CharField(max_length=50)
    lavozim = models.CharField(max_length=50)
    ilmiy_daraja = models.CharField(max_length=500, null=True, blank=True)
    ilmiy_unvon = models.CharField(max_length=500, null=True, blank=True)
    qabul_kunlar = models.CharField(max_length=100, null=True, blank=True)
    manzil = models.TextField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    mehnat_faoliyati = models.TextField()
    email_address = models.CharField(max_length=100, null=True, blank=True)
    google_scholar=models.CharField(max_length=500, null=True, blank=True)
    scopus=models.CharField(max_length=500, null=True, blank=True)
    researchgate=models.CharField(max_length=500, null=True, blank=True)
    orcid=models.CharField(max_length=500, null=True, blank=True)
    instagram=models.CharField(max_length=500, null=True, blank=True)
    telegram=models.CharField(max_length=500, null=True, blank=True)
    linkedin=models.CharField(max_length=500, null=True, blank=True)
    facebook=models.CharField(max_length=500, null=True, blank=True)
    youtube=models.CharField(max_length=500, null=True, blank=True)
    shaxsiysayt=models.CharField(max_length=500, null=True, blank=True)
    slug=models.SlugField(max_length=300, null=False, blank=True)

    @property
    def full_name(self):
        return f"{self.ism} {self.familiya} {self.otchestva}"

    @property
    def short_name(self):
        """Familiyasi va ism-otchestvo bosh harflari qaytariladi: Toshniyozov O.F."""
        initials = ""
        if self.ism:
            initials += self.ism[0].upper() + "."
        if self.otchestva:
            initials += self.otchestva[0].upper() + "."
        return f"{self.familiya} {initials}"

    def __str__(self):
        return self.short_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs) 

class UslubiyNashr(BaseModel):
    title = models.CharField(max_length=1000)
    year = models.CharField(max_length=5)
    pdf_nomi=models.CharField(max_length=500, null=True, blank=True)
    document_link = models.TextField()
    authors = models.ManyToManyField(Worker, blank=True, related_name="uslubiy_nashrlar")
    extra_authors = models.TextField(blank=True, null=True, help_text="Yana boshqa Mualliflar mavjud bo'lsa, qo'lda kiriting:")
    def __str__(self):
        return self.title

class IlmiyNashr(BaseModel):
    title = models.CharField(max_length=1000)
    year = models.CharField(max_length=5)
    jurnal_nomi=models.CharField(max_length=500, null=True, blank=True)
    sahifalar_soni = models.CharField(max_length=3, null=True, blank=True)
    document_link = models.TextField()
    doi=models.CharField(max_length=100, null=True, blank=True)
    authors = models.ManyToManyField(Worker, blank=True, related_name="ilmiy_nashrlar")
    extra_authors = models.TextField(blank=True, null=True, help_text="Yana boshqa Mualliflar mavjud bo'lsa, qo'lda kiriting:")
    def __str__(self):
        return self.title

class AvtoReferat(BaseModel):
    title = models.CharField(max_length=1000)
    year = models.CharField(max_length=5)
    pdf_nomi=models.CharField(max_length=500, null=True, blank=True)
    document_link = models.TextField()
    authors = models.ManyToManyField(Worker, blank=True, related_name="avtoreferat")
    extra_authors = models.TextField(blank=True, null=True, help_text="Yana boshqa Mualliflar mavjud bo'lsa, qo'lda kiriting:")
    def __str__(self):
        return self.title

class Sertificate(BaseModel):
    title = models.CharField(max_length=1000)
    year = models.CharField(max_length=5)
    pdf_nomi=models.CharField(max_length=500, null=True, blank=True)
    photo=models.ImageField(upload_to='sertifikatlar/', verbose_name='sertificate', null=True, blank=True)
    authors = models.ManyToManyField(Worker, blank=True, related_name="sertificate")
    document_link = models.TextField()
    def __str__(self):
        return self.title
class Videodarslik(BaseModel):
    title = models.CharField(max_length=300)
    year = models.CharField(max_length=5)
    authors = models.ManyToManyField(Worker, blank=True, related_name="videodarslik")
    document_link = models.TextField()
    def __str__(self):
        return self.title
class Loyiha(BaseModel):
    title = models.CharField(max_length=1000)
    year = models.CharField(max_length=5)
    authors = models.ManyToManyField(Worker, blank=True, related_name="loyiha")
    document_link = models.TextField()
    def __str__(self):
        return self.title

class Yangiliklar(BaseModel):
    image = models.ImageField(upload_to="yangiliklar/", verbose_name="yangilik", null=True, blank=True)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=False)
    class Meta:
        verbose_name = 'yangilik'
        verbose_name_plural = 'yangiliklar'

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Elonlar(BaseModel):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='elonlar/', verbose_name="e'lonlar", null=True, blank=True)
    short_description=models.CharField(max_length=150)
    description = models.TextField()
    data=models.DateField()
    time = models.TimeField()
    slug = models.SlugField(null=False, blank=True)

    class Meta:
        verbose_name="e'lon"
        verbose_name_plural = "e'lonlar"
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    



    



class MeyoriyHujjat(BaseModel):
    title = models.CharField(max_length=100)
    file_link = models.CharField(max_length=1000)
    class Meta:
        verbose_name = "meyoriy hujjat"
        verbose_name_plural = "meyoriy hujjatlar"
    def __str__(self):
        return self.title


    
    
class TalimShakli(models.TextChoices):
    kunduzgi = "kunduzgi", "kunduzgi"
    sirtqi = "sirtqi", "sirtqi"
    masofaviy = "masofaviy", "masofaviy"

class Course(models.TextChoices):
    birinchi = '1', '1-kurs'
    ikkinchi = '2', '2-kurs'
    uchinchi = '3', '3-kurs'
    turtinchi='4', '4-kurs'
    beshinchi = '5', '5-kurs'

class Fan(BaseModel): 
    meyoriy_hujjat = models.ForeignKey(MeyoriyHujjat, on_delete=models.CASCADE, related_name='fan') 
    title = models.CharField(max_length=100, blank=False, null=False) 
    talim_shakli = models.CharField(max_length=20, choices=TalimShakli.choices) 
    image = models.ImageField(upload_to='fan/', null=True, blank=True) 
    course = models.CharField(max_length=10, choices=Course.choices) 
    slug = models.SlugField(blank = True, null=False) 
    workers = models.ManyToManyField( Worker, related_name='fanlar', blank=True ) 
    class Meta: 
        verbose_name = "fan" 
        verbose_name_plural = "fanlar" 
    def __str__(self): 
        return f"{self.title}-{self.talim_shakli}, {self.course}-kurs" 
    def save(self, *args, **kwargs): 
        if not self.slug: 
            self.slug = slugify(self.title) 
            super().save(*args, **kwargs)

class Fan_tarkibi(BaseModel):
    subject_name = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name="fan_tarkibi" )
    title=models.CharField(max_length=100, blank=False, null=False)
    file_link = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.title

class Adabiyotlar(BaseModel):
    specific_subject = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='adabiyotlar')
    total_name=models.CharField(max_length=1000)
    file_link = models.CharField(max_length=1000)
    slug = models.SlugField(null=False, blank=True)

    class Meta:
        verbose_name = 'adabiyot'
        verbose_name_plural = "adabiyotlar"
    def __str__(self):
        return self.total_name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.specific_subject)

