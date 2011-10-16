# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.admin.models import User
from django.template.defaultfilters import slugify

class Aluno(models.Model):
	
	user = models.ForeignKey(User, blank=True, editable=False, null=True)

	username = models.CharField(max_length=32)
	matricula = models.CharField(max_length=15)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=64)
	password = models.CharField(max_length=50)
	telefone = models.CharField(max_length=16)
	data_cadastro = models.DateTimeField(default=datetime.now)#, editable=False
	
	class Meta:
		ordering = ['-id']

	def save(self):
		if not self.id:
			c = Aluno.objects.filter(email=self.email).count()
			if c:
				raise EmailExistente

			usr = User.objects.filter(username=self.username)
			if usr:
				u = usr[0]
			else:
				u = User.objects.create_user(self.username, self.email, self.password)
			u.save()
			self.user = u
		else:
			self.user.username = self.username
			self.user.email = self.email
			self.user.set_password(self.password)
			self.user.save()

		super(Aluno, self).save()

	def __unicode__ (self):
		return self.username

class Editora(models.Model):
	nome = models.CharField(max_length=64)
	slug = models.SlugField(max_length=64)
	
	def __unicode__ (self):
		return self.nome

class Livro(models.Model):
	titulo = models.CharField(max_length=255)
	idioma = models.CharField(max_length=2)
	local = models.CharField(max_length=64)
	isbn = models.CharField(max_length=17)
	edicao = models.CharField(max_length=50)
	data_lancamento = models.DateTimeField(default=datetime.now)#,editable=False
	data_cadastro = models.DateTimeField(default=datetime.now)#,editable=False
	descricao = models.TextField()
	serie = models.CharField(max_length=32)
	quantidade = models.CharField(max_length=3)
	editora = models.ForeignKey(Editora)
	classificacao = models.CharField(max_length=1)
	
	def __unicode__(self):
		return self.titulo
	
