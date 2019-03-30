from django.contrib import admin
from .models import Agenda
from .models import Pessoa
from .models import AgendaInstitucional

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(AgendaInstitucional)
class AgendaInstitucionalAdmin(admin.ModelAdmin):
    pass