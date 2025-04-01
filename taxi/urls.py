from django.urls import path

from .views import index, ManufacturerListView, CarListView, CarDetailView, \
    DriverListView, DriverDetailView, ManufacturerDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturers"),
    path("manufacturers/<int:pk>", ManufacturerDetailView.as_view(),
         name="manufacturers_by_index"),
    path("cars/", CarListView.as_view(), name="cars"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="cars_by_index"),
    path("drivers/", DriverListView.as_view(), name="drivers"),
    path("drivers/<int:pk>", DriverDetailView.as_view(),
         name="drivers_by_index"),
]

app_name = "taxi"
