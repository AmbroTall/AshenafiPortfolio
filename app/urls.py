from django.urls import path
from .views import home_page, download_pdf, display_pdf

app_name = "app"
urlpatterns = [
    path('', home_page, name="home"),
    path('download_pdf/', download_pdf, name='download_pdf'),
    path('view_pdf/', display_pdf , name='view_pdf'),

]