from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Organization


# Create your views here.

def index(request):
    organization_list = Organization.objects.all()
    context = {
        'organization_list': organization_list,
    }
    return render(request, 'ifc/index.html', context)


def organization_detail(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    context = {
        'organization': organization
    }
    return render(request, 'ifc/organization_detail.html', context)
