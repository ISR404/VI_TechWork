from pydoc import text
from django import forms

class MarkerForm(forms.Form):
    marker_name = forms.CharField(max_length=40, label="Название места")
    x_map_pos = forms.FloatField(label='Широта (смотри значение Latitude)')
    y_map_pos = forms.FloatField(label='Долгота (смотри значение Longtitude')
    description = forms.CharField(max_length=4000, label="Описание места")