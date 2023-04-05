from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
                    'first_name': 'Your First Name:',
                    'last_name': 'Last Name:',
                    'stars': 'Rating:'
                 }
        error_messages = {
                            'stars': {
                                        'min_value': 'Rating below 1 is not permitted',
                                        'max_value': 'Rating above 5 is not allowed'
                                     }
                         }