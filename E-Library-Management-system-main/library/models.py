from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta



class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Mail_ID = models.CharField(max_length=50)
   
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.Mail_ID)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('literature', 'Literature'),
        ('biography', 'Biography'),
        ]
    name=models.CharField(max_length=50)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    ebook=models.CharField(max_length=100,default='education')
    

    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


def get_expiry():
    return datetime.today() + timedelta(days=30)
class IssuedBook(models.Model):
    #moved this in forms.py
    #mail=[(student.mail,str(student.get_name)+' ['+str(student.mail)+']') for student in StudentExtra.objects.all()]
    Mail_ID=models.CharField(max_length=30,default='education')
    #isbn=[(str(book.isbn),book.name+' ['+str(book.isbn)+']') for book in Book.objects.all()]
    isbn=models.CharField(max_length=30,default='education')
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.Mail_ID