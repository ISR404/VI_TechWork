from Impressions_app.models import Profile


def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None

    if user != None:
        user_profile = Profile.objects.get_or_create(user=user)
        user.profile = user_profile[0]

    if backend.name == 'vk-oauth2':

        url = response.get('photo', '')

    if url:
        user.profile.avatar = url
        user.profile.save()
