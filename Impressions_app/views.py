from multiprocessing import context
from django.shortcuts import render
# from social_core.pipeline.user import get_username

# Create your views here.

def main_page(request):
    active_user = request.user
    context = {
        'active_user': active_user,
    }
    return render(request, 'Impressions_app/main_page.html', context)