# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView
from django.contrib import admin
from .views import register_user


app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path('register/', views.register_user, name='register'),
    path("djangoapp/register/", register_user), 

    path("", TemplateView.as_view(template_name="index.html")),

    # path for login
    path(route='login', view=views.login_user, name='login'),
    path('login/', TemplateView.as_view(template_name="index.html")),

    # path for logout
    path('logout/', views.logout_user, name='logout'),

    path(route='get_cars', view=views.get_cars, name ='getcars'),

    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),

    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),

    path('add_review', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
