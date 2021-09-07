from .models import Rows



def menu_links(request):
    links = Rows.objects.all()
    return dict(links=links)