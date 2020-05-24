from django.db import models

# Create your models here.
class TeacherInfo(models.Model):
    teacher_id = models.CharField(max_length=64)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    supply_list = models.CharField(max_length=256)
    supply_cost = models.FloatField()
    school_id = models.IntegerField(default=1)

    def __str__(self):
        return self.first_name

class SchoolInfo(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=256)
    street = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=64)
    type = models.CharField(max_length=128)
    district = models.CharField(max_length=256)

    def __str__(self):
        return self.name