# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('finalapp/', views.homepage1, name='finalapp'),
    # path('t/', views.tpage, name='t'),
    # path('fillform',views.index, name="index"),
    path('',views.landing, name="landing"),
    path('form/',views.index, name="form"),
    path('predict',views.predict,name="predict")
]
