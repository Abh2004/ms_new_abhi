from django.db import models

# Create your models here.

class Hallpics(models.Model):
    img = models.ImageField(upload_to='pics')
    caption = models.CharField(max_length=100,null=True,blank=True)

class pics2019(models.Model):
    img = models.ImageField(upload_to='pics')
    caption = models.CharField(max_length=100,null=True,blank=True)

class pics2018(models.Model):
    img = models.ImageField(upload_to='pics')
    caption = models.CharField(max_length=100,null=True,blank=True)

class Champs2020to2021tech(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)
    roll = models.CharField(max_length=10, null=True, blank=True)

class Champs2019to2020socult(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)
    roll = models.CharField(max_length=10, null=True, blank=True)

class Champs2019to2020tech(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)
    roll = models.CharField(max_length=10, null=True, blank=True)

class Champs2018to2019sports(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)
    roll = models.CharField(max_length=10, null=True, blank=True)

class Champs2017to2018sports(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)
    roll = models.CharField(max_length=10, null=True, blank=True)

class Champs2016to2017sports(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)
    roll = models.CharField(max_length=10, null=True, blank=True)

class Champs2012to2013socult(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)
    roll = models.CharField(max_length=10, null=True, blank=True)

class Champs2011to2012sports(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)
    roll = models.CharField(max_length=10, null=True, blank=True)

class hallnotices(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='notices')
    text = models.TextField()

class gcnotices(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='notices')
    text = models.TextField()

class messnotices(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='notices')
    text = models.TextField()

class gnrlnotices(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='notices')
    text = models.TextField()

class ugd(models.Model):
    Roll = models.CharField(max_length=10, null=True, blank=True)
    Name = models.CharField(max_length=100)
    dept = models.CharField(max_length=5, null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.Name

class phdd(models.Model):
    Roll = models.CharField(max_length=10, null=True, blank=True)
    Name = models.CharField(max_length=100)
    dept = models.CharField(max_length=5, null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.Name

class alumnid(models.Model):
    Roll = models.CharField(max_length=10, null=True, blank=True)
    Name = models.CharField(max_length=100)
    dept = models.CharField(max_length=5, null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.Name
    
class blog(models.Model):
    Title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pictures')
    desc= models.TextField()
    long_desc= models.TextField(default="")
    
    def __str__(self):
        return self.Title