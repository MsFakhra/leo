from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('prolific','name' , 'text','emotions','before','after')
    fields = ['prolific','name' , 'text','emotions','before','after']

admin.site.register(User, UserAdmin)