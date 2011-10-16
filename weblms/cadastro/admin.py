from django.contrib import admin
from cadastro.models import Aluno, Editora, Livro

class AlunoAdmin(admin.ModelAdmin):

	search_fields = ('id','matricula', 'username', 'first_name', 'last_name', 'email',)
	list_display = ('id','matricula', 'username', 'first_name', 'last_name', 'email', 'data_cadastro')
	save_on_top = True

class EditoraAdmin(admin.ModelAdmin):

	search_fields = ('id','nome',)
	list_display = ('id','nome',)
	prepopulated_fields = {'slug': ('nome',)}
	save_on_top = True
	
class LivroAdmin(admin.ModelAdmin):

	search_fields = ('id', 'titulo', 'idioma', 'editora', 'quantidade', 'classificacao', 'data_cadastro',)
	list_display = ('id', 'titulo', 'idioma', 'editora', 'quantidade', 'classificacao', 'data_cadastro',)
	save_on_top = True

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Livro, LivroAdmin)
