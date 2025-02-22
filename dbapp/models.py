# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    major = models.CharField(max_length=50, blank=True, null=True)
    enrollment_year = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'student'  # This tells Django to use an explicit table name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
