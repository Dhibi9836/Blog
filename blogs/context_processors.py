from .models import Category
from references.models import SocialLink

def get_categories(request) :
    categories = Category.objects.all()
    return dict(categories = categories)

def get_socials(request) :
    social_links = SocialLink.objects.all()
    return dict(socials = social_links)