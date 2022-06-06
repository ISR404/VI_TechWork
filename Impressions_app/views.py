from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import MarkerForm
from .models import PlaceMarker
import folium
from django.contrib.auth import logout
# from social_core.pipeline.user import get_username

# Create your views here.

def main_page(request):
    active_user = request.user
    if active_user.is_authenticated:
        list_of_markers = active_user.placemarker_set.all()
        map = folium.Map()
        for marker in list_of_markers:
            folium.Marker([marker.x_position, marker.y_position], popup=marker.description, tooltip=marker.marker_name).add_to(map)
        map = map._repr_html_
        context = {
        'active_user': active_user,
        'list_of_markers': list_of_markers,
        'map': map,
        }
    else:
        context = {
            'active_user': active_user,
        }
    return render(request, 'Impressions_app/html-files/main_page.html', context)


def create_marker(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MarkerForm(request.POST)
            if form.is_valid():
                marker = PlaceMarker()
                marker.marker_name = form.cleaned_data['marker_name']
                marker.x_position = form.cleaned_data['x_map_pos']
                marker.y_position = form.cleaned_data['y_map_pos']
                marker.description = form.cleaned_data['description']
                marker.user = request.user
                marker.save()
                return redirect('main_page')
            else:
                return HttpResponse('Форма заполнена неверно. Попробуйте еще раз.')
        else:
            form = MarkerForm()
            map = folium.Map()
            map.add_child(folium.LatLngPopup())
            map = map._repr_html_
            return render(request, 'Impressions_app/html-files/new_marker_form.html', { 'form': form, 'map': map })
    else:
        return HttpResponse('Вы не авторизированы для совершения данного действия')


def logout_view(request):
    logout(request)
    return redirect('main_page')