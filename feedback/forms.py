from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#new
from feedback.models import Card_info, Facilities
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
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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


class CampusFacilitiesFeedbackForm(forms.Form):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    USAGE_FREQUENCY_CHOICES = (
        ('Never', 'Never'),
        ('Rarely', 'Rarely'),
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
        ('Daily', 'Daily'),
    )

    CONVENIENCE_CHOICES = (
        ('Not at all', 'Not at all'),
        ('Slightly', 'Slightly'),
        ('Moderately', 'Moderately'),
        ('Very', 'Very'),
        ('Extremely', 'Extremely'),
    )

    SUGGESTIONS_MAX_LENGTH = 5000

    halls_of_residence = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    cafeterias = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    Lecture_rooms = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    sports_equipment = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    facility_availability = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    equipment_access = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    usage_frequency = forms.ChoiceField(choices=USAGE_FREQUENCY_CHOICES)
    Labs_usage= forms.ChoiceField(choices=CONVENIENCE_CHOICES)
    facility_up_to_date = forms.ChoiceField(choices=CONVENIENCE_CHOICES)
    school_resources_availability = forms.ChoiceField(choices=CONVENIENCE_CHOICES)
    library_usage = forms.ChoiceField(choices=USAGE_FREQUENCY_CHOICES)
    coursework_improvement = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'maxlength': SUGGESTIONS_MAX_LENGTH}))
    sports_equipment_adequacy = forms.ChoiceField(choices=CONVENIENCE_CHOICES)
    sports_facilities_wish = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'maxlength': SUGGESTIONS_MAX_LENGTH}))
    equipment_wish = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'maxlength': SUGGESTIONS_MAX_LENGTH}))
    experience_improvement = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'maxlength': SUGGESTIONS_MAX_LENGTH}))
    overall_satisfaction = forms.ChoiceField(choices=RATING_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        form_data = self.cleaned_data  # Use self.cleaned_data to access the validated form data
        saved_form = Facilities(**form_data)  # Assuming FeedbackModel is a Django model
        saved_form.save()
        return saved_form
    class Meta:
        model = Facilities
        fields = (
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
        )
        label = 'Facilities Feedback'

