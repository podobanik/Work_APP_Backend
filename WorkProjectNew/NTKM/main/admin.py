from django.contrib import admin
from .models import Problem, AppUser, Sector, ObjectOfWork, ProblemType, ProblemStatus

admin.site.register(Problem)
admin.site.register(AppUser)
admin.site.register(Sector)
admin.site.register(ProblemType)
admin.site.register(ProblemStatus)
admin.site.register(ObjectOfWork)
