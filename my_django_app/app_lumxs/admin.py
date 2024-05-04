from django.contrib import admin
from app_lumxs.models import CustomUser, CreateContract, OpenWallet

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CreateContract)
admin.site.register(OpenWallet)
