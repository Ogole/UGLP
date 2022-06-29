from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import VHT.views as vs


urlpatterns = [
    
    path('manage_vht',vs.manage_VHT, name='manage_vht' ),
     path('',vs.index_view, name='home')
]