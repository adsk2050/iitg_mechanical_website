from .models import MechHomePage

def navbar(request):
	navlist_parent = MechHomePage.objects.all()
	if navlist_parent :
		navlist = navlist_parent[0].get_children().live().order_by('first_published_at')
		# for item in navlist:
		# 	item
		# for item in nav_items:
		return {'navlist': navlist}
	else:
		return {'navlist':[]}
