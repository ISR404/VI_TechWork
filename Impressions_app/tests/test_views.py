from django.test import TestCase
from Impressions_app.forms import MarkerForm
from Impressions_app.models import PlaceMarker

# Create your tests here.


class ViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        PlaceMarker.objects.create(
            marker_name="test_marker_1", x_position=30, y_position=20, description="desc_1")
        PlaceMarker.objects.create(
            marker_name="test_marker_2", x_position=5, y_position=10, description="desc_2")

    def test_main_page_list_markers(self):
        marker_list = PlaceMarker.objects.all()
        self.assertEqual(
            f'{marker_list}', '<QuerySet [<PlaceMarker: (Undefined) test_marker_1 marker>, <PlaceMarker: (Undefined) test_marker_2 marker>]>')

    def test_form_create_marker_out_of_validator_range(self):
        data = {
            'marker_name': 'Test Place',
            'x_map_pos': 150,
            'y_map_pos': 87,
            'description': 'Test description',
        }
        form = MarkerForm(data)
        self.assertFalse(form.is_valid())

    def test_form_create_marker_in_validator_range(self):
        data = {
            'marker_name': 'Test Place',
            'x_map_pos': 150,
            'y_map_pos': 86,
            'description': 'Test description',
        }
        form = MarkerForm(data)
        self.assertTrue(form.is_valid())
