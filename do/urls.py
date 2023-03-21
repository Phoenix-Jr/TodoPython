from django.urls import path
from .views import index,update,delete

urlpatterns = [
    path('',index,name='accueil'),
    path('<int:myid>/update',update,name='update'),
    path('<int:myid>/delete',delete,name='delete'),
]
