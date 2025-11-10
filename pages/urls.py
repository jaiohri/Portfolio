from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('experiences/', views.experiences, name='experiences'),
    path('experiences/add/', views.add_experience, name='add_experience'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
