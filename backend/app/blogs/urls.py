from django.urls import path

from . import views

urlpatterns = [
    path("", views.BlogListAPIView.as_view()),
    path("detail/<int:pk>/", views.BlogDetailAPIView.as_view()),
    path("create/", views.BlogCreateAPIView.as_view()),
]
