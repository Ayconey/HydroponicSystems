from django.urls import path
from . import views

urlpatterns = [
    path('hydro_systems/', views.HydroSystemListCreate.as_view(), name='hydro_systems_list_create'),
    path('hydro_systems/user/',views.UserHydroSystemsListCreate.as_view(),name="user_hydro_systems_list_create"),
    path('hydro_systems/<int:pk>/', views.HydroSystemRetrieveUpdateDestroy.as_view(), name='hydro_systems_retrieve_update_destroy'),
    path('measurements/', views.MeasurementListCreate.as_view(), name='measurements_list_create'),
    path('measurements/<int:pk>/', views.MeasurementRetrieveUpdateDestroy.as_view(), name='measurements_retrieve_update_destroy'),
]
