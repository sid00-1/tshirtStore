from django.urls import path, include
from .views import about_view, contact_view, teston_view, SearchProductView, dashboard_view, customize_view, create_view

app_name = 'basics'
urlpatterns = [
    path("about/", about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('testimonials/', teston_view, name='teston'),
    path('search/', SearchProductView.as_view(), name='query'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('customize/<slug>/', customize_view, name='customize'),
    path('create/', create_view, name='create'),
]
