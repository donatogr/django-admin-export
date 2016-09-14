# -- encoding: UTF-8 --
import random
from admin_export.views import AdminExport
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
import pytest
from .models import ModelUnderTest


class ModelAdminTest(admin.ModelAdmin):
    def get_queryset(self, request):
        return super(ModelAdminTest, self).get_queryset(request).filter(value__lt=request.magic)


def queryset_valid(request, queryset):
    return all(x.value < request.magic for x in queryset)


@pytest.mark.django_db
def test_queryset_from_admin(rf, admin_user):
    for x in range(100):
        ModelUnderTest.objects.get_or_create(value=x)
    assert ModelUnderTest.objects.count() >= 100

    request = rf.get("/")
    request.user = admin_user
    request.magic = random.randint(10, 90)
    request.GET = {
        "ct": ContentType.objects.get_for_model(ModelUnderTest).pk,
        "ids": ",".join(str(id) for id in ModelUnderTest.objects.all().values_list("pk", flat=True))
    }

    old_registry = admin.site._registry
    admin.site._registry = {}
    admin.site.register(ModelUnderTest, ModelAdminTest)
    assert queryset_valid(request, admin.site._registry[ModelUnderTest].get_queryset(request))
    assert not queryset_valid(request, ModelUnderTest.objects.all())

    admin_export_view = AdminExport()
    admin_export_view.request = request
    admin_export_view.args = ()
    admin_export_view.kwargs = {}
    assert admin_export_view.get_model_class() == ModelUnderTest
    assert queryset_valid(request, admin_export_view.get_queryset(ModelUnderTest))
    admin.site._registry = old_registry
