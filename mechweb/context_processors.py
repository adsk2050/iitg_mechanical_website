from .models import MechHomePage

def navbar(request):
	navlist = MechHomePage.objects.all()[0].get_children().live().order_by('-first_published_at')
	# for item in nav_items:
	return {'navlist': navlist}

