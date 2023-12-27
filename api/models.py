from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    usernome = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Todo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField()

    def __str__(self):
        return self.nome

class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Comment(models.Model):
    postId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    

