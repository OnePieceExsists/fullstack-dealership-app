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

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
