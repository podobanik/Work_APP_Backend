from django.contrib import admin
from .models import Problem, Staff, Sector, ObjectOfWork, ProblemType, ProblemStatus

admin.site.register(Problem)
admin.site.register(Staff)
admin.site.register(Sector)
admin.site.register(ProblemType)
admin.site.register(ProblemStatus)
admin.site.register(ObjectOfWork)