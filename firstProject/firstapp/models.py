from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class IITPStudent(models.Model):
    DOMAIN_CHOICES = [
        ('WD', 'Web Development'),
        ( 'ML', 'Machine Learning'),
        ('AI', 'Artificial Intelligence'),
        ('DS', 'Data Science'),
        ('DA', 'Data Analysis'),
        ('CS', 'Cyber Security')
    ]
    name = models.CharField(max_length = 100)
    roll = models.IntegerField()
    images = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default = timezone.now)
    domain = models.CharField(max_length = 2, choices = DOMAIN_CHOICES)
    description = models.TextField(default="This is a student of IITP")


    def __str__(self):
        return f"{self.name} - ₹{self.roll}"

# One to Many relationship(like every item is a one and it has many ratings)
class ItemsReview(models.Model):
    item = models.ForeignKey(IITPStudent, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default="Good")
    Date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.item.name}"

# Many to many relationship(like there can be multiple store have multiple items)
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    items = models.ManyToManyField(IITPStudent, related_name='stores')

    def __str__(self):
        return self.name
    
# One to one relationship(Like every user has one profile)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="This is a bio")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
