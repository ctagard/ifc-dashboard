from django.urls import path
from . import views

urlpatterns = [
    # /ifc/
    path("", views.index, name='index'),
    # /ifc/2/
    path("<int:organization_id>/", views.organization_detail, name="organization_detail")
]