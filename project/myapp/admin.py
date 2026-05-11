from django.contrib import admin

# Register your models here.
from .models import Post,Contacts
admin.site.register(Post)
admin.site.register(Contacts)