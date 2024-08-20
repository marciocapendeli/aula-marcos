from django.contrib import admin
from django.urls import path
from escola import views
from tipo_atividade.views import cadastro_tipoatividade, lista_tipoatividade

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.escola),
    path('tipoatividade/', cadastro_tipoatividade),
    path('tipoatividade/lista', lista_tipoatividade)

]
