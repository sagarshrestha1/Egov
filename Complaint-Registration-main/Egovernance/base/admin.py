from django.contrib import admin
from.models import Complaint
# Register your models here.
@admin.register(Complaint)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['name','category']
