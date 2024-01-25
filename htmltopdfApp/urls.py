from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path('pdf/',views.generatePdf,name='pdf'),
    path('users/',views.ListUser,name='user'),
    path('users/<int:pk>',views.SingleUser,name='SingleUser'),
     path('users/<int:pk>/pdf',views.generateUserPdf)
]
