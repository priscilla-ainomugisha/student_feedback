from django.db import models
from django.forms import ModelForm

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
    id = models.AutoField(primary_key=True)
    code = models.CharField(db_column='CODE', max_length=10, blank=True, null=True)
    course_name = models.CharField(db_column='COURSE_NAME', max_length=100, blank=True, null=True)
    cu = models.IntegerField(db_column='CU', blank=True, null=True)
    lh = models.IntegerField(db_column='LH', blank=True, null=True)
    ph = models.IntegerField(db_column='PH', blank=True, null=True)
    th = models.IntegerField(db_column='TH', blank=True, null=True)
    ch = models.IntegerField(db_column='CH', blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)
    remark = models.CharField(db_column='Remark', max_length=50, blank=True, null=True)
    origin = models.CharField(db_column='Origin', max_length=50, blank=True, null=True)
    program = models.CharField(db_column='Program', max_length=50, blank=True, null=True)
    year_of_study = models.IntegerField(blank=True, null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
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
    class Meta:
        db_table = 'student_answers'
    

class MultiStepForm(ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'lecturer_preparedness',
            'lecturer_interest',
            'feedback_useful',
            'lecturers_complement',
            'instructional_materials',
            'course_organization',
            'confidence_in_advanced_work',
            'exam_measurement',
            'concept_understanding',
            'concept_understanding_feedback',
            'applicability',
            'applicability_reasoning',
            'recommend_course',
        ]

    def save(self, commit=True):
        form_data = self.cleaned_data
        # Save the form data to the database.
        form_instance = super().save(commit=False)
        if commit:
            form_instance.save()
            return form_instance
    

class Facilities (models.Model):
    halls_of_residence = models.CharField(max_length=100)
    cafeterias = models.CharField(max_length=100)
    Lecture_rooms =models.CharField(max_length=100)
    sports_equipment = models.CharField(max_length=100)
    facility_availability = models.CharField(max_length=100)
    equipment_access = models.CharField(max_length=100)
    usage_frequency = models.CharField(max_length=100)
    Labs_usage= models.CharField(max_length=100)
    facility_up_to_date = models.CharField(max_length=100)
    school_resources_availability = models.CharField(max_length=100)
    library_usage = models.CharField(max_length=100)
    coursework_improvement =models.CharField(max_length=5000)
    sports_equipment_adequacy = models.CharField(max_length=100)
    sports_facilities_wish = models.CharField(max_length=5000)
    equipment_wish = models.CharField(max_length=5000)
    experience_improvement = models.CharField(max_length=5000)
    overall_satisfaction =models.CharField(max_length=100)

    class Meta:
        db_table = 'facilities'
        
class CampusFacilitiesFeedbackForm(ModelForm):
    class Meta:
        model = Facilities
        fields = [
            'halls_of_residence',
            'cafeterias',
            'Lecture_rooms',
            'sports_equipment',
            'facility_availability',
            'equipment_access',
            'usage_frequency',
            'Labs_usage',
            'facility_up_to_date',
            'coursework_improvement',
            'sports_equipment_adequacy',
            'sports_facilities_wish',
            'equipment_wish',
            'experience_improvement',
            'overall_satisfaction',
        ]

    def save(self, commit=True):
        form_data = self.cleaned_data
        # Save the form data to the database.
        form_instance = super().save(commit=False)
        if commit:
            form_instance.save()
            return form_instance

     
