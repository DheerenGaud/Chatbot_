from django.contrib import admin
from .models import Newevent
from .models import Collageinfo
from .models import Deparment
from .models import Scholarship
# Register your models here.

admin.site.register(Newevent)
admin.site.register(Collageinfo)
admin.site.register(Deparment)
admin.site.register(Scholarship)
