from django.urls import path
from . import views

urlpatterns = [
    path('', views.HydroSystemListCreate.as_view(),
         name='hydro_systems_list_create'),
    path('hydro-systems/',views.UserHydroSystemsListCreate.as_view(),
         name="user_hydro_systems_list_create"),
    path('hydro-systems/<int:pk>/',views.HydroSystemRetrieveUpdateDestroy.as_view(),
         name='hydro_system_retrieve'),
    path('hydro-systems/<int:pk>/measurements/',views.MeasurementsFromHydroSystemListCreate.as_view(),
         name='hydro_system_measurements_retrieve_update_destroy'),
    path('measurements/<int:pk>/', views.MeasurementRetrieveUpdateDestroy.as_view(),
         name='measurements_retrieve_update_destroy'),
]
