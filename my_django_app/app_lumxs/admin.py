from django.contrib import admin
from app_lumxs.models import CustomUser, Wallet

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Wallet)
