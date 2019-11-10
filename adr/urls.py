from django.urls import path

from . import views

urlpatterns = [
    path('naranjo', views.naranjo, name='naranjo'),
    path('', views.home, name='home'),
    path('reverseSave', views.reverseSave, name='reverseSave'), # reverse/<int:id>
    path('prescriptionRecords/', views.prescription_record, name='prescriptionRecords'), # reverse/<int:id>
    path('prescriptionRecords/<int:id>', views.prescription_record, name='prescriptionRecordsId'), # reverse/<int:id>
]