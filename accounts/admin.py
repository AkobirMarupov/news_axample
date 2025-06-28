from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from accounts.models import User



class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'hash_password')

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("id", "email", "first_name", "last_name", "is_active", "is_staff")
    list_display_links = ("id", "email", "first_name", "last_name")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")

    fieldsets = (
        (None, {'fields': ('email', 'hash_password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'avatar', 'bio')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'hash_password'),
        }),
    )

    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
