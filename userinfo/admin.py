from django.contrib import admin
from .models import Question, ContestDb

# Register your models here.
admin.site.register(Question)
admin.site.register(ContestDb)