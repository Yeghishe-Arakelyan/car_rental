from django.urls import path
from .views import (
    CarCreateView,
    CarListView,
    CarDetailView,
    CarDeleteUpdateView,
    ReservationCreateView,
    ReservationListView,
    ReservationDetailView,
    UserCreateView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Car Rental API",
        default_version="v1",
        description="API for managing car rentals",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    
    path('cars/create/', CarCreateView.as_view(), name='car-create'),
    path('', CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/<int:pk>/update/', CarDeleteUpdateView.as_view(), name='car-update-delete'),

    path('reservations/create/', ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/', ReservationListView.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('register/', UserCreateView.as_view(), name='create_user'),
    
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]