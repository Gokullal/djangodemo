from shop.models import Categories

def menu_link(request):
    c=Categories.objects.all()
    return {'links':c}   # we used the data globally across all webpagest inside our app