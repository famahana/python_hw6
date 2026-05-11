from django.contrib import admin

# Register your models here.
from .models import Post,Contacts,Restraunt
admin.site.register(Post)
admin.site.register(Contacts)
admin.site.register(Restraunt)