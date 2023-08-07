from django import forms

class StarRatingWidget(forms.RadioSelect):
    template_name = 'star_rating_widget.html'  # Create a template for rendering the stars

    class Media:
        css = {
            'all': ('C:\code\Student_feedback_system\student_feedback\student_feedback\static\css\main.css',),  # Replace with your actual CSS file path
        }
