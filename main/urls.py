from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.MainPost.as_view(), name='post-home'),
    path('<int:pk>', views.DetailPost.as_view(), name='post-detail'),
    path('testy/', views.tests ,name='test'),
    path('pilot/', views.test2 ,name='pilot'),
    path('kontakty/', views.test3 ,name='kontakty'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
