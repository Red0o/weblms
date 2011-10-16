from django.contrib import admin
from cadastro.models import Aluno

class AlunoAdmin(admin.ModelAdmin):

	search_fields = ('id','matricula', 'username', 'first_name', 'last_name', 'email',)
	list_display = ('id','matricula', 'username', 'first_name', 'last_name', 'email', 'data_cadastro')
	save_on_top = True

admin.site.register(Aluno, AlunoAdmin)
