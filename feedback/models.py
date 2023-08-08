from django.db import models
from django.forms import ModelForm


# Create your models here.
class CourseFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    lecturer_preparedness = models.CharField(max_length=100)
    lecturer_interest = models.CharField(max_length=100)
    feedback_useful = models.CharField(max_length=100)
    lecturers_complement = models.CharField(max_length=100)
    instructional_materials = models.CharField(max_length=100)
    course_organization = models.CharField(max_length=100)
    confidence_in_advanced_work = models.CharField(max_length=100)
    exam_measurement = models.CharField(max_length=100)
    concept_understanding = models.CharField(max_length=100)
    concept_understanding_feedback = models.CharField(max_length=2000)
    applicability = models.CharField(max_length=100)
    applicability_reasoning = models.CharField(max_length=100)
    recommend_course = models.CharField(max_length=100)

    # Other fields from the form go here
    class Meta:
        db_table = "course_student_answers"


class CourseFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    lecturer_preparedness = models.CharField(max_length=100)
    lecturer_interest = models.CharField(max_length=100)
    feedback_useful = models.CharField(max_length=100)
    lecturers_complement = models.CharField(max_length=100)
    instructional_materials = models.CharField(max_length=100)
    course_organization = models.CharField(max_length=100)
    confidence_in_advanced_work = models.CharField(max_length=100)
    exam_measurement = models.CharField(max_length=100)
    concept_understanding = models.CharField(max_length=100)
    concept_understanding_feedback = models.CharField(max_length=2000)
    applicability = models.CharField(max_length=100)
    applicability_reasoning = models.CharField(max_length=100)
    recommend_course = models.CharField(max_length=100)

    # Other fields from the form go here
    class Meta:
        db_table = "course_student_answers"


class CourseFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    lecturer_preparedness = models.CharField(max_length=100)
    lecturer_interest = models.CharField(max_length=100)
    feedback_useful = models.CharField(max_length=100)
    lecturers_complement = models.CharField(max_length=100)
    instructional_materials = models.CharField(max_length=100)
    course_organization = models.CharField(max_length=100)
    confidence_in_advanced_work = models.CharField(max_length=100)
    exam_measurement = models.CharField(max_length=100)
    concept_understanding = models.CharField(max_length=100)
    concept_understanding_feedback = models.CharField(max_length=2000)
    applicability = models.CharField(max_length=100)
    applicability_reasoning = models.CharField(max_length=100)
    recommend_course = models.CharField(max_length=100)

    # Other fields from the form go here
    class Meta:
        db_table = "course_student_answers"
