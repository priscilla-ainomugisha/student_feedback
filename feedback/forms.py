from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#new
from feedback.models import Card_info
from feedback.models import Feedback
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.forms import modelformset_factory


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class MultiStepForm(forms.Form):
    LECTURER_PREPAREDNESS_CHOICES = (
        ('almost_always', 'Almost always'),
        ('frequently', 'Frequently'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('almost_never', 'Almost never'),
    )

    LECTURER_INTEREST_CHOICES = (
        ('almost_always', 'Almost always'),
        ('frequently', 'Frequently'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('almost_never', 'Almost never'),
    )

    USEFUL_FEEDBACK_CHOICES = (
        ('yes', 'Yes'),
        ('a_few_sometimes', 'A few Sometimes'),
        ('rarely', 'Rarely'),
    )

    LECTURES_COMPLEMENT_CHOICES = (
        ('almost_always', 'Almost always'),
        ('frequently', 'Frequently'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('almost_never', 'Almost never'),
    )

    INSTRUCTIONAL_MATERIALS_CHOICES = (
        ('almost_always', 'Almost always'),
        ('frequently', 'Frequently'),
        ('sometimes', 'Sometimes'),
        ('rarely', 'Rarely'),
        ('almost_never', 'Almost never'),
    )

    COURSE_ORGANIZATION_CHOICES = (
        ('strongly_agree', 'Strongly Agree'),
        ('agree', 'Agree'),
        ('neutral', 'Neutral'),
        ('disagree', 'Disagree'),
        ('strongly_disagree', 'Strongly Disagree'),
    )

    CONFIDENCE_IN_ADVANCED_WORK_CHOICES = (
        ('strongly_agree', 'Strongly Agree'),
        ('agree', 'Agree'),
        ('neutral', 'Neutral'),
        ('disagree', 'Disagree'),
        ('strongly_disagree', 'Strongly Disagree'),
    )

    EXAM_MEASUREMENT_CHOICES = (
        ('strongly_agree', 'Strongly Agree'),
        ('agree', 'Agree'),
        ('neutral', 'Neutral'),
        ('disagree', 'Disagree'),
        ('strongly_disagree', 'Strongly Disagree'),
    )
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Below Average'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    
    RECOMMEND_CHOICES =[
        (0, 'Not likely at all'),
        (1, 'Unlikely'),
        (2, 'Somewhat unlikely'),
        (3, 'Neither likely nor unlikely'),
        (4, 'Somewhat likely'),
        (5, 'Likely'),
        (6, 'Very likely'),
        (7, 'Extremely likely'),
        (8, 'Almost certainly'),
        (9, 'Definitely'),
        (10, 'Absolutely'),
    ],

    lecturer_preparedness = forms.ChoiceField(
        label="The lecturer was well prepared for the class.",
        choices=LECTURER_PREPAREDNESS_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    lecturer_interest = forms.ChoiceField(
        label="The lecturer showed an interest in helping students learn.",
        choices=LECTURER_INTEREST_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    feedback_useful = forms.ChoiceField(
        label="I received useful feedback on my performance on tests, papers, etc.",
        choices=USEFUL_FEEDBACK_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    lecturers_complement = forms.ChoiceField(
        label="The lectures, tests, and assignments complemented each other.",
        choices=LECTURES_COMPLEMENT_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    instructional_materials = forms.ChoiceField(
        label="The instructional materials (i.e., books, readings, handouts, study guides, lab manuals, multimedia, software) increased my knowledge and skills in the subject matter.",
        choices=INSTRUCTIONAL_MATERIALS_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    course_organization = forms.ChoiceField(
        label="The course was organized in a manner that helped me understand the underlying concepts.",
        choices=COURSE_ORGANIZATION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    confidence_in_advanced_work = forms.ChoiceField(
        label="The course gave me the confidence to do more advanced work in the subject.",
        choices=CONFIDENCE_IN_ADVANCED_WORK_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    exam_measurement = forms.ChoiceField(
        label="The examinations, projects measured my knowledge of the course material",
        choices=EXAM_MEASUREMENT_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    concept_understanding = forms.ChoiceField(
        label="Rate your understanding of the course concepts",
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    concept_understanding_feedback = forms.CharField(
        widget=forms.Textarea,
        label="Your feedback",
        required=False
    )

    applicability = forms.ChoiceField(
        label="Rate your understanding of the course concepts",
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    applicability_reasoning = forms.CharField(
        widget=forms.Textarea,
        label="Why do you think so?",
        required=False
    )

    recommend_course = forms.TypedChoiceField(
    label="Would you recommend this course to others?",
    choices=[
        (0, 'Not likely at all'),
        (1, 'Unlikely'),
        (2, 'Somewhat unlikely'),
        (3, 'Neither likely nor unlikely'),
        (4, 'Somewhat likely'),
        (5, 'Likely'),
        (6, 'Very likely'),
        (7, 'Extremely likely'),
        (8, 'Almost certainly'),
        (9, 'Definitely'),
        (10, 'Absolutely'),
    ],
    coerce=lambda value: value[0],
    widget=forms.RadioSelect,
    help_text=(
        'Please rate your likelihood of recommending this course to other students on a scale of 0 to 10, where 0 is not likely at all and 10 is very likely. The value you enter must be a number between 0 and 10.'
    )
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['recommend_course'].help_text = (
            'Please rate your likelihood of recommending this course to other students on a scale of 0 to 10, where 0 is not likely at all and 10 is very likely.'
        )
    def save(self, *args, **kwargs):
        form_data = self.cleaned_data  # Use self.cleaned_data to access the validated form data
        saved_form = Feedback(**form_data)  # Assuming FeedbackModel is a Django model
        saved_form.save()
        return saved_form
    
    class Meta:
        model = Feedback
        fields = (
            'card_info'
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
        )
        label = 'Course Feedback'
FeedbackFormSet = inlineformset_factory(Card_info,Feedback,form=MultiStepForm,
                      fields=['institution','date_from','date_to','achievements'],
                      extra=1,can_delete=True)



