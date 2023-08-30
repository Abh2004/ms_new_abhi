from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import blog, Hallpics, pics2019, pics2018, Champs2020to2021tech, Champs2011to2012sports, Champs2012to2013socult, Champs2016to2017sports, Champs2017to2018sports, Champs2018to2019sports, Champs2019to2020socult, Champs2019to2020tech, hallnotices, messnotices, gcnotices, gnrlnotices, ugd, phdd, alumnid
# Register your models here.
@admin.register(blog)
@admin.register(Hallpics)
@admin.register(pics2019)
@admin.register(pics2018)
@admin.register(hallnotices)
@admin.register(gcnotices)
@admin.register(messnotices)
@admin.register(gnrlnotices)
@admin.register(Champs2019to2020tech)
@admin.register(Champs2011to2012sports)
@admin.register(Champs2012to2013socult)
@admin.register(Champs2016to2017sports)
@admin.register(Champs2018to2019sports)
@admin.register(Champs2017to2018sports)
@admin.register(Champs2020to2021tech)
@admin.register(Champs2019to2020socult)
@admin.register(ugd)
@admin.register(phdd)
@admin.register(alumnid)

class usrdet(ImportExportModelAdmin) :
    pass