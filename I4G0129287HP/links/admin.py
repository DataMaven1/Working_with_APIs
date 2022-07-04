from os import link
from django.contrib import admin

from .models import Link, User
#from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Link)
#admin.site.register(User)