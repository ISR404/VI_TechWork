from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class MarkerForm(forms.Form):
    marker_name = forms.CharField(max_length=40, label="Place Name")
    y_map_pos = forms.FloatField(label='Latitude (watch on Map)', validators=[
                                 MinValueValidator(-86), MaxValueValidator(86)])
    x_map_pos = forms.FloatField(label='Longtitude (watch on Map)')
    description = forms.CharField(max_length=4000, label="Description")
