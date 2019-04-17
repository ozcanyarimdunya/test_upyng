from django.contrib import admin
from django import forms
from .models import Demo


class DemoAdminForm(forms.ModelForm):
    class Meta:
        model = Demo
        fields = '__all__'


class DemoAdmin(admin.ModelAdmin):
    form = DemoAdminForm
    list_display = ['name', 'created', 'last_updated', 'logo', 'document']
    readonly_fields = ['name', 'created', 'last_updated', 'logo', 'document']


admin.site.register(Demo, DemoAdmin)
