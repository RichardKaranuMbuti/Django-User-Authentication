from django.db import models

'''
lets import Abstract user class-has the basic user log fields such as 
username,password,first name,last name and email
'''
from django.contrib.auth.models import AbstractUser,Group
from django.contrib.auth.models import Permission

class User(AbstractUser):
   

    groups=models.ManyToManyField(
         Group,
         related_name='customer_user_groups',
         blank=True,
         help_text=('The group this user belongs to.'
            'A user will get all permissions granted to each of their groups'),
         )

    user_permissions=models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user',
        )

    class Meta:
        verbose_name='user'
        verbose_name_plural='users'
