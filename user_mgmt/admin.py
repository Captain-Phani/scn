from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
CustomUser = get_user_model()


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomAuthForm(AuthenticationForm):

    username = forms.EmailField(label='Email', max_length=255 )


class CustomUserAdmin(BaseUserAdmin):
    forms = CustomUserChange
    add_form = CustomUserCreation
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_active']
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': (
            'email', 'password'
        )}),
        ('Permissions', {'fields' :('is_staff', 'is_active')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')})
    )

    add_fieldsets = (
        (None, {'classes': ('wides',),
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}),

    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.login_form = CustomAuthForm


