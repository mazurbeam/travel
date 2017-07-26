from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.
# Create your models here.
class UserManager(models.Manager):
	def registerVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['f_name']) < 3:
			results['status'] = False
			results['errors'].append('First Name must be at least 3 chars.')
		if len(postData['l_name']) < 3:
			results['status'] = False
			results['errors'].append('Last Name must be at least 3 chars.')
		if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
			results['status'] = False
			results['errors'].append('Please enter a valid email.')
		if len(postData['password']) < 4  or  postData['password'] != postData['c_password']:
			results['status'] = False
			results['errors'].append('Please enter a valid password.')

		user = User.objects.filter(email = postData['email'])
		print user, '*****', len(user)
		if len(user) >= 1:
			results['status'] = False
			results['errors'].append('User already exists!!!!')



		#check to see if user is not in db

		return results
	def createUser(self, postData):
		p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(f_name = postData['f_name'], l_name = postData['l_name'], email = postData['email'], password = p_hash)
		return user
	def loginVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		results['user'] = User.objects.filter(email = postData['email'])
		if len(results['user'] ) <1:
			results['status'] = False
			results['errors'].append('Something went wrong')
		else:
			hashed = bcrypt.hashpw(postData['password'].encode(), results['user'][0].password.encode())
			if hashed  != results['user'][0].password:
				results['status'] = False
				results['errors'].append('Something went wrong')
		return results
        




class User(models.Model):
	f_name = models.CharField(max_length = 400)
	l_name = models.CharField(max_length = 400)
	email = models.CharField(max_length = 400)
	password = models.CharField(max_length = 400)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	objects = UserManager()
