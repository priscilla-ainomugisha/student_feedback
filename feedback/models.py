from django.db import models

# Create your models here.
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


class YearOfStudy(models.Model):
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

    def __str__(self):
        return self.year_of_study

class Semester(models.Model):
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

    def __str__(self):
        return self.semester
    
class Card_info(models.Model):
    id = models.AutoField(null=False,primary_key=True)
    code = models.CharField(db_column='CODE', max_length=10, blank=True, null=False,unique=True)  # Field name made lowercase.
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

class Feedback(models.Model):
    card_info = models.ForeignKey(Card_info, on_delete=models.CASCADE,to_field='code')
    lecturer_preparedness = models.CharField(max_length=100)
    lecturer_interest = models.CharField(max_length=100)
    feedback_useful = models.CharField(max_length=100)
    lecturers_complement = models.CharField(max_length=100)
    instructional_materials= models.CharField(max_length=100)
    course_organization = models.CharField(max_length=100)
    confidence_in_advanced_work = models.CharField(max_length=100)
    exam_measurement = models.CharField(max_length=100)
    concept_understanding  = models.CharField(max_length=100)
    concept_understanding_feedback = models.CharField(max_length=2000)
    applicability  = models.CharField(max_length=100)
    applicability_reasoning  = models.CharField(max_length=100)
    recommend_course  = models.CharField(max_length=100)
    # Other fields from the form go here
