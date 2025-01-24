from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100, null=True, blank=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length = 20)
    jwt = models.CharField(max_length = 100,null=True, blank=True)
    verify = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return str(self.email)