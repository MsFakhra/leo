from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index2'),
    path('blob', views.get_blob, name='get_blob'),
    path('text', views.get_text, name='get_text'),
    path('casual', views.get_sentence, name='get_sentence'),
    path('add_to_db', views.add_to_db, name='add_to_db'),
    path('index3', views.index3, name='index3'),
    path('index4', views.index4, name='index4'),
    path('after', views.after, name='after'),
    path('privacy', views.privacy, name='privacy'),
    path('index2', views.index, name='index2'),
    path('thankyou', views.thankyou, name = 'thankyou')
]
