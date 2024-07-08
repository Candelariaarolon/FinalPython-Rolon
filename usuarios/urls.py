from django.urls import path 
from usuarios.views import registrar_usuario, agregar_producto, pagina_principal, iniciar_sesion, logout_view

urlpatterns = [
    path('registro/', registrar_usuario, name='registro_usuario'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('pagina-principal/', pagina_principal, name='pagina_principal'),
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'), 
    path('logout/', logout_view, name='logout_view'),
]
