from django.conf.urls import url
from django.urls.conf import include,include
from django.db.models.query import ValuesIterable
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    path(r'^uploadImage/',views.uploadImage,name = 'uploadImage'),
    url(r'^registeruser/',views.registeruser,name='registeruser'),
    url(r'^login/',views.loginpage,name='loginpage'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^like/$', views.like, name='like'),
    path(r'^photo/<str:pk>/',views.viewPhoto,name='photo'),
    path(r'^follow/<str:username>/',views.follow,name='follow'),
    path(r'post/<int:pk>/comment/', views.post_detail, name='post_detail')
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
