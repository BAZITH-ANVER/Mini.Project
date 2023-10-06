from django.db import models

# Create your models here.
class Frontend(models.Model):
    title=models.CharField(max_length=50)
    def _str_(self):
        return self.title
    
class Backend(models.Model):
    title=models.CharField(max_length=50)
    def _str_(self):
        return self.title
    
class Framework(models.Model):
    title=models.CharField(max_length=50)
    def _str_(self):
        return self.title
    
class Course(models.Model):
    title=models.CharField(max_length=50)
    def _str_(self):
        return self.title


class Student(models.Model):
    Fullname=models.CharField(max_length=250)
    Mobile=models.CharField(max_length=250)
    Projectname=models.CharField(max_length=250)
    Desciption=models.TextField(max_length=250)
    Frontend=models.ForeignKey(Frontend,on_delete=models.CASCADE)
    Backendend=models.ForeignKey(Backend,on_delete=models.CASCADE)
    Framework=models.ForeignKey(Framework,on_delete=models.CASCADE)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def _str_(self):
        return self.Fullname
