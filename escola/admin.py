from django.contrib import admin
from escola.models import Aluno, Curso, Matricula
# Register your models here.
class Alunos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
    list_display_links = list_display
    search_fields = ['nome', 'cpf',]
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ['id','codigo_curso', 'descricao']
    list_display_links = list_display
    search_fields = ['codigo_curso',]

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ['id', 'aluno', 'curso']
    list_display_links = list_display

admin.site.register(Matricula, Matriculas)