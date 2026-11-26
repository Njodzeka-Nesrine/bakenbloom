from django.contrib import admin
from django.urls import path
from recipes import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('category/<slug:category_slug>/',
         views.category, name='category'),

    path('recipe/<slug:recipe_slug>/',
         views.recipe_detail, name='recipe_detail'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),
]