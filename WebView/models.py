from django.db import models

# we create events model

class Event(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=100)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title

class PLOT(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title

class FARM(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title

class CONSTRUCTION(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title
    
class AGRICULTURE(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title

class CONSULTANT(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title

class UNDERGRADUATE(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title

class MICROCREDIT(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title

class EDUCATION(models.Model):
    title=models.CharField(max_length=50)
    descption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    date=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title


class Broker(models.Model):
    username=models.CharField(max_length=100)
    message=models.TextField()
    
    def __str__(self):
        return self.username

class Contact(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)  
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.fullname


class Suscribe(models.Model):
    email=models.EmailField(max_length=254)

    def __str__(self):
        return self.email
    