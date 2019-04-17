from django.contrib import admin
from .models import Actors, Movies, Categories, Comments, Awards
# Register your models here.


admin.site.register(Actors)
admin.site.register(Movies)
admin.site.register(Categories)
admin.site.register(Comments)
admin.site.register(Awards)