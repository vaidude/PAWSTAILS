from django.contrib import admin

# Register your models here.
from . models import user_reg,Pet, trainer_reg,Muncipality,Adopt,Pay,Timetable,Vaccinations,Dog_feddback,Admin
admin.site.register(user_reg)
admin.site.register(Pet)
admin.site.register(trainer_reg)
admin.site.register(Muncipality)
admin.site.register(Adopt)
admin.site.register(Pay)
admin.site.register(Timetable)
admin.site.register(Vaccinations)
admin.site.register(Dog_feddback)
admin.site.register(Admin)

