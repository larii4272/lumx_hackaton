from django.contrib import admin
from app_lumxs.models import CustomUser, Wallet, Contract, Athlete, Experience, Transaction

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Wallet)
admin.site.register(Contract)
admin.site.register(Athlete)
admin.site.register(Experience)
admin.site.register(Transaction)