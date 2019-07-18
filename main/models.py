from django.db import models

# Create your models here.
# Every model represents a table
# Every row represents an object

class Student(models.Model):
    GENDER=(
    ('f','Female'),
    ('m','Male'),
    ('u','Undisclosed')
    )
    name= models.CharField(max_length=100)
    roll_no= models.IntegerField(unique= True)
    address=models.TextField(null=True)
    phone_no= models.CharField(max_length= 15,null=True)
    email=models.EmailField(null=True)
    gender=models.CharField(max_length= 1 , choices = GENDER, null=True)

    def __str__(self):
        return self.name

