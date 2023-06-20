from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
class Race(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.gender

class MissingPerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    date_Missing = models.DateField(max_length=10)
    age_At_Missing = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.ForeignKey('State', null=True, blank=True, on_delete=models.CASCADE)
    gender = models.ForeignKey('Gender', null=True, blank=True, on_delete=models.CASCADE)
    race = models.ForeignKey('Race', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    def __str__(self):
        return self.last_name
    
class Meta():
    db_table = 'patron_missingperson'