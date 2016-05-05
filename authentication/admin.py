from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from authentication.models import User, UserScore


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'member_id', 'first_name', 'last_name', 'is_faculty', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email__iexact=email)
        except models.ObjectDoesNotExist:
            return email
        raise forms.ValidationError('User with this Email already exists.')

    def clean_member_id(self):
        member_id = self.cleaned_data['member_id']
        try:
            User.objects.get(member_id__iexact=member_id)
        except models.ObjectDoesNotExist:
            return member_id
        raise forms.ValidationError('User with this id already exists')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Password",
                                         help_text="<a href=\"password/\">Change Password</a>.")

    class Meta:
        model = User
        fields = ('email', 'member_id', 'first_name', 'last_name', 'is_faculty', 'password')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'email', 'member_id', 'first_name', 'is_faculty', 'is_superuser')
    list_filter = ('is_faculty',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'member_id')}),
        ('Permissions', {'fields': ('is_faculty', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member_id', 'email', 'first_name', 'last_name', 'is_faculty', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'member_id')
    ordering = ('email',)
    filter_horizontal = ()


class UserScoreAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'score')

admin.site.register(User, UserAdmin)
admin.site.register(UserScore, UserScoreAdmin)
admin.site.unregister(Group)

