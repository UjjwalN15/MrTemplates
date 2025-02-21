from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Package)
admin.site.register(Theme)
admin.site.register(StoreCategory)
admin.site.register(Store)
admin.site.register(Payment)
