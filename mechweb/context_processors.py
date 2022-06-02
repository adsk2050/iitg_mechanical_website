from collections import defaultdict
from .models import MechHomePage, ResearchLabPage, FooterColumn


def navbar(request):
    navlist_parent = MechHomePage.objects.all()
    if navlist_parent:
        navlist = navlist_parent[0].get_children().filter().live().order_by("first_published_at")
        ordering = {
            "Academics": 1,
            "Research Home": 2,
            "Student Home": 3,
            "Faculty Home": 4,
            "Staff Home": 5,
            "Awards Home": 6,
            "Alumni Home": 7,
            "Event Home": 8,
            "categories home": 9,
            "aboutiitgmech": 10,
            "Alumni Home Page": 11,
        }
        ordering = defaultdict(lambda: 1000, ordering)
        navlist = sorted(navlist, key=lambda x: ordering[x.content_type.name])
        return {"navlist": navlist[:11]}
    else:
        return {"navlist": []}


def footer(request):
    result = {"footer": list(FooterColumn.objects.all().order_by("column_no"))}
    return result


# def get_mech_workshop():
# 	workshop = ResearchLabPage.objects.all().get(name="Mechanical Workshop")
# 	return {'workshop':workshop }
# "faculty home page":1,
# "Student Home":2,
# "Staff Home":3,
# "Alumni Home":4,
# "Research Home":5,
# "Publication Home":6,
# "Lab Home":7,
# "Project Home":8,
# "Awards Home":9,
# "Event Home":10,
# "Course Structure":11,
# "categories home":12,
# "aboutiitgmech":13


# navlist_parent = MechHomePage.objects.all()
# if navlist_parent :
# 	navlist = navlist_parent[0].get_children().live().order_by('first_published_at')
# 	# for item in navlist:
# 	# 	item
# 	# for item in nav_items:
# 	ordering = {
# 		"Course Structure":1,
# 		"Research Home":2,
# 		"Student Home":3,
# 		"faculty home page":4,
# 		"Staff Home":5,
# 		"Awards Home":6,
# 		"Alumni Home":7,
# 		"Event Home":8,
# 		"categories home":9,
# 		"aboutiitgmech":10,
# 		"Departmental Committees":11
# 	}
# 	navlist = sorted(navlist, key=lambda x: ordering[x.content_type.name])
