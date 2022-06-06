from django.test import TestCase
from Impressions_app.forms import MarkerForm


class MarkerFormTestClass(TestCase):

    def test_marker_form_description_max_length(self):
        form = MarkerForm()
        self.assertTrue(form.fields['description'].max_length == 4000)

    def test_marker_form_name_max_length(self):
        form = MarkerForm()
        self.assertTrue(form.fields['marker_name'].max_length == 40)
