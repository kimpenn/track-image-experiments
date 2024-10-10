from .models import SiteSettings


# To be able to use data from settings in the pattern, we add an object of settings here view
def settings(request):
    return {"settings": SiteSettings.load()}
