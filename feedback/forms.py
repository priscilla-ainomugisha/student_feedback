from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#new
from feedback.models import Card_info, Facilities
from feedback.models import Feedback
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.forms import Field, modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


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
        (1, '👍'),   # Unicode character for X emoji
        (2, '👎'),   # Unicode character for star emoji
        
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
        widget=forms.Select(attrs={'class': 'select'}),
        required=True
    )

    lecturer_interest = forms.ChoiceField(
        label="The lecturer showed an interest in helping students learn.",
        choices=LECTURER_INTEREST_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        required=True
    )

    feedback_useful = forms.ChoiceField(
        label="I received useful feedback on my performance on tests, papers, etc.",
        choices=USEFUL_FEEDBACK_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        required=True
    )

    lecturers_complement = forms.ChoiceField(
        label="The lectures, tests, and assignments complemented each other.",
        choices=LECTURES_COMPLEMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'select'}),
        required=True
    )

    instructional_materials = forms.ChoiceField(
        label="The instructional materials (i.e., books, readings, handouts, study guides, lab manuals, multimedia, software) increased my knowledge and skills in the subject matter.",
        choices=INSTRUCTIONAL_MATERIALS_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        required=True
    )

    course_organization = forms.ChoiceField(
        label="The course was organized in a manner that helped me understand the underlying concepts.",
        choices=COURSE_ORGANIZATION_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        required=True
    )

    confidence_in_advanced_work = forms.ChoiceField(
        label="The course gave me the confidence to do more advanced work in the subject.",
        choices=CONFIDENCE_IN_ADVANCED_WORK_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        required=True
    )

    exam_measurement = forms.ChoiceField(
        label="The examinations, projects measured my knowledge of the course material",
        choices=EXAM_MEASUREMENT_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        required=True
    )

    concept_understanding = forms.ChoiceField(
        label="Rate your understanding of the course concepts",
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        required=True
    )

    concept_understanding_feedback = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea'}),
        label="Share with us",
        required=False
    )

    applicability = forms.ChoiceField(
        label="Rate your understanding of the course concepts",
        choices=RATING_CHOICES,
        widget=forms.NumberInput(attrs={'class': 'custom-slider','type': 'range', 'min': '1', 'max': '5', 'step': '1'}),
        required=True
    )

    applicability_reasoning = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea'}),
        label="Why do you think so?",
        required=False
    )

    recommend_course = forms.TypedChoiceField(
    label="On a scale of 1-10, recommend this course to others",
    choices=[
        
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ],
    coerce=lambda value: value[0],
    widget=forms.RadioSelect(attrs={'class': 'card'})
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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
            Submit('submit', 'Submit', css_class='btn btn-primary')
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
    Lecture_rooms = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    halls_of_residence = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    cafeterias = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    sports_equipment = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    facility_availability = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    equipment_access = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    usage_frequency = forms.ChoiceField(label="How often do you use campus facilities?",choices=USAGE_FREQUENCY_CHOICES, widget=forms.Select(attrs={'class': 'select'}),)
    Labs_usage= forms.ChoiceField(label="How often do you use the campus labs?" ,choices=CONVENIENCE_CHOICES, widget=forms.Select(attrs={'class': 'select'}),)
    facility_up_to_date = forms.ChoiceField(label="How up-to-date are campus facilities?",choices=CONVENIENCE_CHOICES, widget=forms.Select(attrs={'class': 'select'}),)
    school_resources_availability = forms.ChoiceField(label="How readily available are school resources to aid your studies?List your suggestions below. ",choices=CONVENIENCE_CHOICES, widget=forms.Select(attrs={'class': 'select'}),)
    library_usage = forms.ChoiceField(label="How often do you use the campus library? ",choices=USAGE_FREQUENCY_CHOICES, widget=forms.Select(attrs={'class': 'select'}),)
    coursework_improvement = forms.CharField(label="How can school resources be improved to aid students’ coursework? List your suggestions below.  ",widget=forms.Textarea(attrs={'rows': 5, 'maxlength': SUGGESTIONS_MAX_LENGTH, 'class': 'textarea'}))
    sports_equipment_adequacy = forms.ChoiceField(label="How adequate is the school sports equipment? ",choices=CONVENIENCE_CHOICES, widget=forms.Select(attrs={'class': 'select'}),)
    sports_facilities_wish = forms.CharField(label="Are there any sports facilities you would like the university to provide? ",widget=forms.Textarea(attrs={'rows': 5, 'maxlength': SUGGESTIONS_MAX_LENGTH,'class': 'textarea'}))
    equipment_wish = forms.CharField(label="Please list them below.",widget=forms.Textarea(attrs={'rows': 5, 'maxlength': SUGGESTIONS_MAX_LENGTH,'class': 'textarea'}))
    overall_satisfaction = forms.ChoiceField(label="How satisfied are you with the overall experience at this university?  ",choices=RATING_CHOICES, widget=forms.Select(attrs={'class': 'select'}),)
    experience_improvement = forms.CharField(label="How can your experience at this university be improved? Please leave your comments below.? ",widget=forms.Textarea(attrs={'rows': 5, 'maxlength': SUGGESTIONS_MAX_LENGTH,'class': 'textarea'}))


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


