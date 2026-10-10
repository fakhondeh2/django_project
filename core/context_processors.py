from settings.models import Settings


def site_settings(request):
    """
    Makes the single Settings row (phone, email, address, logo, etc.)
    available in every template as {{ site_settings }}, the same way the
    built-in 'request' context processor adds `request` everywhere.

    Settings.objects.first() returns None if no row has been created yet
    in the admin, so templates should use {{ site_settings.field }} safely
    (Django just renders nothing for a missing attribute on None/undefined)
    rather than assuming a row always exists.
    """
    return {"site_settings": Settings.objects.first()}
