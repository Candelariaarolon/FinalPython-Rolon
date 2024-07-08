from django.urls import path 
from inicio.views import inicio, sobremi



urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/sobremi', sobremi, name='sobremi' )

    
]


