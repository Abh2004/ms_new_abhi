from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('gallery/',views.gallery, name='gallery'),
    path('noticehn/',views.halln, name='halln'),
    path('noticegc/',views.gcn, name='gcn'),
    path('noticemn/',views.messn, name='messn'),
    path('noticegn/',views.genn, name='genn'),
    path('database/',views.dat, name='dat'),
    path('database/ug_data/',views.datug, name='datug'),
    path('database/phd_data/',views.datphd, name='datphd'),
    path('database/alumni_data/',views.datalumni, name='datalumni'),
    path('hall_of_fame/',views.hof, name='hof'),
    path('hcm/',views.hcm, name='hcm'),
    path('login/',views.login, name='login'),
    path('logged/',views.logged, name='logged'),
    path('logout/',views.logout, name='logout'),
    path('change/',views.change, name='change'),
    path('signup/',views.signup, name='signup'),
    path('blogs/',views.blogs, name='blogs'),
    path('blogs/<int:id>',views.blog_Desc, name='blog_Description'),
    path('Gallery/',views.gallery_new, name='gallery_new'),
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)