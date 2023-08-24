from django.contrib import admin
from .models import Votes

class VoteView(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "votes")

# Register your models here.
admin.site.register(Votes, VoteView)
