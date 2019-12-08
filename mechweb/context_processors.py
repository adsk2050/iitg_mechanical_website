from .models import MechHomePage, ResearchLabPage

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

# def get_mech_workshop():
# 	workshop = ResearchLabPage.objects.all().get(name="Mechanical Workshop")
# 	return {'workshop':workshop }
	