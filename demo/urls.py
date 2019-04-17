from django.urls import path

from . import views

app_name = 'demo'
urlpatterns = (
    # urls for Demo
    path('', views.DemoListView.as_view(), name='list'),
    path('create/', views.DemoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DemoDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.DemoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DemoDeleteView.as_view(), name='delete'),
)
