# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CourseInfo(models.Model):
    code = models.CharField(db_column='CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    course_name = models.CharField(db_column='COURSE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cu = models.IntegerField(db_column='CU', blank=True, null=True)  # Field name made lowercase.
    lh = models.IntegerField(db_column='LH', blank=True, null=True)  # Field name made lowercase.
    ph = models.IntegerField(db_column='PH', blank=True, null=True)  # Field name made lowercase.
    th = models.IntegerField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    ch = models.IntegerField(db_column='CH', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=50, blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year_of_study = models.IntegerField(blank=True, null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_info'
