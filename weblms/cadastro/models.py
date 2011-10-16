# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.admin.models import User
from datetime import datetime

class Aluno(models.Model):
	
	user = models.ForeignKey(User, blank=True, editable=False, null=True)

	username = models.CharField(max_length=32)
	matricula = models.CharField(max_length=15)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=64)
	password = models.CharField(max_length=50)
	telefone = models.CharField(max_length=16)
	data_cadastro = models.DateTimeField(default=datetime.now, blank=True)#, editable=False
	
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

