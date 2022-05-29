from django.contrib import admin

# Register your models here.
from core.models import User

from core.models import PersonAdmin

admin.site.register(User, PersonAdmin)
#admin.site.register(PersonAdmin)

