from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('home/', views.home, name= 'home'),
  path('add/', views.add, name = 'add'),
  path('details/<str:pk>/', views.details, name = 'details'),
  path('auth/', views.auth, name = 'auth'),
  path('signup/', views.signup, name = 'signup'),
  path('logout/', views.logoutUser, name = 'logout'),  
  # path('select/', views.select, name = 'select'),
  

  
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)