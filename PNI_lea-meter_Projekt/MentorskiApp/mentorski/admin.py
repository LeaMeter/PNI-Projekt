from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm
from .models import Korisnici, Upisi, Predmeti

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Korisnici
    list_display = ('email','password','role','status')
    fieldsets = ((
            'Korisnik',
            {
                'fields':(
                    'username',
                    'email',
                    'password',
                    'role',
                    'status',)
            }
        ),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('first_name','last_name','last_login', 'is_superuser','is_staff','is_active','date_joined',),
        }),
    )


class UpisiAdmin(admin.ModelAdmin):
    list_display = ('student_id','predmet_id','status')

class PredmetiAdmin(admin.ModelAdmin):
    list_display = ('ime','kod','program','ECTS','sem_redovni','sem_izvanredni','izborni')

admin.site.register(Korisnici, CustomUserAdmin)
admin.site.register(Upisi, UpisiAdmin)
admin.site.register(Predmeti, PredmetiAdmin)
admin.site.unregister(Group)
