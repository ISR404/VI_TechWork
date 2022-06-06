from tkinter import Place
from django.test import TestCase
from Impressions_app.models import PlaceMarker


class MarkerModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        PlaceMarker.objects.create(
            marker_name='Test Marker', x_position=0, y_position=0, description='desc')

    def test_marker_model_description_max_length(self):
        marker = PlaceMarker.objects.get(id=1)
        field_max_length = marker._meta.get_field('description').max_length
        self.assertEqual(field_max_length, 4000)

    def test_marker_model_name_max_length(self):
        marker = PlaceMarker.objects.get(id=1)
        field_max_length = marker._meta.get_field('marker_name').max_length
        self.assertEqual(field_max_length, 40)
