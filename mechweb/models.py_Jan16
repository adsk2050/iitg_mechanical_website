from datetime import date

from django import forms
from django.contrib.auth.models import AbstractUser
from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
######################################################
# for tagging
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldRowPanel, FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, \
    ObjectList
    # , StreamFieldPanel
from wagtail.core.fields import RichTextField
    # , StreamField
# from wagtail.core import blocks
# from wagtail.images.blocks import ImageChooserBlock
# from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.models import Page, Orderable
from wagtail.documents.edit_handlers import DocumentChooserPanel
######################################################
from wagtail.images.edit_handlers import ImageChooserPanel
######################################################
from wagtail.search import index
from wagtailautocomplete.edit_handlers import AutocompletePanel

######################################################
# Importing constants and settings
from iitg_mechanical_website.settings.base import CUSTOM_RICHTEXT, AUTH_USER_MODEL
from .constants import LABORATORY_IN_CHARGE, FACULTY_IN_CHARGE, FACULTY_DESIGNATION, FACULTY_ROLES, FACULTY_AWARD_TYPES, \
    FAC_PREV_WORK_TYPES
from .constants import TEXT_PANEL_CONTENT_TYPES, LOCATIONS, EVENTS, STUDENT_PROGRAMME, MASTERS_SPECIALIZATION, \
    STAFF_DESIGNATION, PROJECT_TYPES, PUBLICATION_TYPES, LAB_TYPES, COURSE_TYPES, USER_TYPES, INTEREST_CATEGORIES


######################################################
# NAV_ORDER
# from social_django.strategy import DjangoStrategy

######################################################

######################################################

# when makemigrations are happening this does not show as change in the db
# class CustomUserManager(BaseUserManager):
# 	def has_perm(self, perm, obj=None):
# 		""" Does this user have a specific permission"""
# 		#Simplest possible answer - always true
# 		return True

# 	def has_module_perm(self, app_label):
# 		"""Does the user have the permissions to view the app "app_label"? """
# 		# simplest answer - yes always
# 		return True

# 	@property
# 	def is_staff(self):
# 			"""Is the user a member of staff?"""
# 			#simplest answer - All admins are staff
# 			return self.is_staff

class CustomUser(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Put your webmail ID without @iitg.ac.in'),
    )
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True)
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    user_type = models.CharField(max_length=2, choices=USER_TYPES, default='0')
    uid = models.CharField(max_length=10, default='000000000', verbose_name='Roll Number/Employee Number',
                           help_text='Only students required to provide their roll no. Others may leave "000000000" but not blank')
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    USERNAME_FIELD = 'email'  # Its default is username
    # REQUIRED_FIELDS = [ 'first_name', 'last_name', 'user_type', 'uid']
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_type', 'uid', 'is_staff']


######################################################
class MechHomePage(Page):
    intro = models.CharField(blank=True, max_length=500)
    body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    HOD_message = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    HOD_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='+')
    donation_link = models.URLField(max_length=250, blank=True)
    donate_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='+')
    donate_message = models.CharField(blank=True, max_length=250)
    # intro = RichTextField(blank=True)
    # user = models.OneToOneField(AUTH_USER_MODEL,related_name='mech_home_page_manager', null=True, on_delete=models.SET_NULL)

    # footer links
    # quick_link1
    # quick_link2
    # quick_link3
    # quick_link4
    # quick_link5
    # quick_link6
    #
    # dept_link1
    # dept_link2
    # dept_link3
    # dept_link4
    # dept_link5
    # dept_link6

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery Images", max_num=10),
        FieldPanel('HOD_message'),
        FieldPanel('donate_message'),
        FieldPanel('donation_link'),
        ImageChooserPanel('HOD_image'),
        ImageChooserPanel('donate_image'),
    ]

    notification_tab_panels = [
        InlinePanel('text_panels', label="Mini Articles"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Content"),
        ObjectList(notification_tab_panels, heading="News & Notifications"),
        ObjectList(Page.promote_panels, heading="Promote"),
        ObjectList(Page.settings_panels, heading="Settings"),
    ])

    subpage_types = ['EventHomePage', 'FacultyHomePage', 'StudentHomePage', 'ResearchHomePage', 'StaffHomePage',
                     'CourseStructure', 'AlumniHomePage', 'AwardHomePage', 'Aboutiitgmech', 'CategoriesHome',
                     'CommitteeHomePage', 'GenericPage']

    max_count = 1

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        navlist = self.get_children().live().order_by('-first_published_at')
        hod_name = "Head of Department"
        hod_image = "0"
        hod_url = "0"
        hod_contact = "0"
        try:
            hod = get_hod()
            if hod.count() == 1:
                hod = hod[0]
                hod_name = hod.__str__()
                hod_url = hod.url
                hod_contact = "<p>Office:" + hod.office_address_line_1 + ",<br> Contact: " + hod.office_contact_number + ",<br> Email: " + hod.email_id + "</p>"
        except:
            pass
        # how to raise error in console ?

        categories = get_categories()
        new_events = get_new_events()
        top_awards = get_new_awards()
        # context['navlist'] = navlist
        context['categories'] = categories
        context['hod_name'] = hod_name
        context['hod_url'] = hod_url
        context['hod_contact'] = hod_contact
        context['new_events'] = new_events
        context['top_awards'] = top_awards

        return context

    class Meta:
        verbose_name = "Home"


class HomeTextPanel(Orderable):
    page = ParentalKey(MechHomePage, on_delete=models.CASCADE, related_name='text_panels')
    title = models.CharField(blank=True, max_length=50)
    photo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    # You are trying to change the nullable field 'photo' on hometextpanel to non-nullable without a default; we can't do that (the database needs something to populate existing rows).
    # Please select a fix:
    # 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    # 2) Ignore for now, and let me handle existing rows with NULL myself (e.g. because you added a RunPython or RunSQL operation to handle NULL values in a previous data migration)
    # 3) Quit, and let me add a default in models.py
    # Select an option: 2
    description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    date = models.DateTimeField()
    # change the below content_type code to manage css accordingly
    content_type = models.CharField(
        default="0",
        choices=TEXT_PANEL_CONTENT_TYPES,
        max_length=50
    )
    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('date'),
        FieldPanel('content_type'),
        ImageChooserPanel('photo'),
    ]


class MechHomePageGalleryImage(Orderable):
    page = ParentalKey(MechHomePage, on_delete=models.CASCADE, related_name='gallery_images')
    photo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('photo'),
            FieldPanel('caption'),
        ]),
    ]


#############################################
class Aboutiitgmech(Page):
    vision = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    history = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    about = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    photo = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('vision', classname="full"),
        FieldPanel('history', classname="full"),
        FieldPanel('about', classname="full"),
        ImageChooserPanel('photo'),
    ]

    parent_page_types = ['MechHomePage']
    subpage_types = []
    max_count = 1
######################################################
class GenericPage(Page):
    body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    parent_page_types = ['MechHomePage']
    subpage_types = ['GenericPage']
    # max_count = 1


######################################################
class EventHomePage(Page):
    # nav_order = models.CharField(max_length=1, default=NAV_ORDER[0])
    # user = models.OneToOneField(AUTH_USER_MODEL,related_name='event_home_page_manager', null=True, on_delete=models.SET_NULL)
    featured_event = models.ForeignKey(
        'EventPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='featured_event'
    )
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        AutocompletePanel('featured_event', target_model='mechweb.EventPage'),
        # InlinePanel('event_page', label="New Event"),
    ]

    parent_page_types = ['MechHomePage']
    subpage_types = ['EventPage']
    max_count = 1

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        event_list = self.get_children().live().order_by('-first_published_at')
        paginator = Paginator(event_list, 1)  # Show 1 events per page
        page = request.GET.get('page')
        event_list = paginator.get_page(page)
        context['event_list'] = event_list
        return context

    class Meta:
        verbose_name = "Event Home"


class EventPage(Page):
    # user = models.ForeignKey('CustomUser', related_name='event_manager', null=True, on_delete=models.SET_NULL)
    event_name = models.CharField(blank=True, max_length=50)
    description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    venue = models.CharField(blank=True, max_length=50, choices=LOCATIONS, default='0')
    poster = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='+')
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    event_type = models.CharField(max_length=50, choices=EVENTS, default='0')
    content_panels = Page.content_panels + [
        FieldPanel('event_type'),
        FieldPanel('event_name'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('start_date'),
                FieldPanel('end_date'),
            ]),
        ], heading="Timings"),
        FieldPanel('venue'),
        FieldPanel('description'),
        FieldRowPanel([
            ImageChooserPanel('poster'),
            DocumentChooserPanel('document'),
        ]),
        InlinePanel('gallery_images', label="Gallery Images", max_num=2),
        InlinePanel('links', label="Related Links", max_num=10),
    ]

    # promote_panels=[]
    # settings_panels=[]

    parent_page_types = ['EventHomePage']
    subpage_types = []

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventPageGalleryImage(Orderable):
    page = ParentalKey(EventPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('image'),
            FieldPanel('caption'),
        ]),
    ]


class EventPageLink(Orderable):
    page = ParentalKey(EventPage, on_delete=models.CASCADE, related_name='links')
    link = models.URLField(max_length=250)
    panels = [
        FieldPanel('link'),
    ]


def get_new_events():
    a = EventPage.objects.all().live().order_by('-first_published_at')
    if len(a) >= 10:
        a = a[0:10]
    return a


######################################################
# Can I make a generic class which covers all these repeatedly adding of data models needed to be written only once?
######################################################
class CategoriesHome(Page):
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    parent_page_types = ['MechHomePage']
    subpage_types = ['Categories']
    # , 'CourseProgrammes', 'CourseSpecializations']
    max_count = 1


class Categories(Page):
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    category = models.CharField(max_length=2, choices=INTEREST_CATEGORIES, default='0', unique=True)
    photo = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel('photo'),
        FieldPanel('category'),
    ]
    parent_page_types = ['CategoriesHome']
    max_count = 4

    def serve(self, request):
        faculty_list = self.faculty.all().order_by('facultypage__first_name')
        return render(request, self.template, {
            'page': self,
            'faculty_list': faculty_list,
        })


def get_categories():
    return Categories.objects.all().live().order_by('-category')


def get_cat_fac(cat):
    return Categories.objects.all().get(category=cat).faculty.all().order_by('first_name')


######################################################
######################################################

class FacultyHomePage(Page):
    # nav_order = models.CharField(max_length=1, default=NAV_ORDER[1])
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    parent_page_types = ['MechHomePage']
    subpage_types = ['FacultyPage']
    max_count = 1

    # This function is not working here
    # def list_common_interests(self):

    def serve(self, request):
        faculty_list = FacultyPage.objects.all().order_by('first_name', 'middle_name', 'last_name')

        all_research_interests = faculty_interests()
        all_categories = get_categories()
        cat = request.GET.get('cat')
        cat_name = ''
        if cat and int(cat) < 4:
            cat_name = INTEREST_CATEGORIES[int(cat)][1]
            faculty_list = get_cat_fac(cat)
        tag = request.GET.get('tag')
        if tag:
            faculty_list = faculty_list.filter(research_interests__name=tag)
        current_faculty_list = []
        past_faculty_list = []
        today = date.today()
        for fac in faculty_list:
            try:
                if fac.leaving_date > today:
                    current_faculty_list.append(fac)
                else:
                    if fac.on_lien:
                        current_faculty_list.append(fac)
                    past_faculty_list.append(fac)
            except TypeError:
                current_faculty_list.append(fac)
            # check this bro!! what is name?? both models faculty page or facultyhomepage or facultyresearchinteresttag  dont have name keyword... maybe name keyword is in clustertaggablemanager source code
        # paginator = Paginator(faculty_list, 50) # Show 10 faculty per page
        # page_no = request.GET.get('page_no')
        # faculty_list = paginator.get_page(page_no)

        return render(request, self.template, {
            'page': self,
            'current_faculty_list': current_faculty_list,
            'past_faculty_list': past_faculty_list,
            'all_research_interests': all_research_interests,
            'all_categories': all_categories,
            'cat': cat,
            'cat_name': cat_name,
            'tag': tag,
            # 'page_no':page_no,
        })

        class Meta:
            verbose_name = "Faculty Home"


class FacultyResearchInterestTag(TaggedItemBase):
    content_object = ParentalKey(
        'FacultyPage',
        related_name='tagged_items',
        on_delete=models.CASCADE)
# This function is working here only in shell but not during rendering
# def list_common_interests(self):


class FacultyPage(Page):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='faculty', null=True, blank=True,
                                on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    office_contact_number = models.CharField(max_length=20, blank=True)
    home_contact_number = models.CharField(max_length=20, blank=True)
    office_address_line_1 = models.CharField(max_length=25, blank=True)
    home_address_line_1 = models.CharField(max_length=25, blank=True)
    email_id = models.EmailField(unique=True)
    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    research_interests = ClusterTaggableManager(through=FacultyResearchInterestTag, blank=True,
                                                verbose_name='Research Interests')
    fac_research_categories = ParentalManyToManyField('mechweb.Categories', blank=True, related_name='faculty')
    joining_date = models.DateField(default=timezone.now)
    leaving_date = models.DateField(blank=True, null=True)
    on_lien = models.BooleanField(default=False)
    on_visit = models.BooleanField(default=False)
    on_depute = models.BooleanField(default=False)
    on_insti = models.CharField(max_length=500, blank=True, verbose_name="Visiting from/On lien to/On deputation to",
                                help_text="Institute name")
    designation = models.CharField(max_length=2, choices=FACULTY_DESIGNATION, default='3')
    website = models.URLField(max_length=250, blank=True)
    abbreviation = models.CharField(max_length=10, blank=True)
    #################################################################
    additional_roles = models.CharField(max_length=2, choices=FACULTY_ROLES, default='2')
    laboratory_in_charge = models.CharField(max_length=2, choices=LABORATORY_IN_CHARGE, default='14')
    faculty_in_charge = models.CharField(max_length=2, choices=FACULTY_IN_CHARGE, default='11')
    content_panels = Page.content_panels + [
        ######################################################
        # The user should not be able to change these things from here
        FieldPanel('user'),
        FieldPanel('first_name'),
        FieldPanel('middle_name'),
        FieldPanel('last_name'),
        FieldPanel('email_id'),
        ######################################################
        FieldPanel('designation'),
        MultiFieldPanel([
            FieldPanel('on_depute'),
            FieldPanel('on_lien'),
            FieldPanel('on_visit'),
            FieldPanel('on_insti')

        ], heading="Visiting/On Lien"),
        FieldPanel('joining_date'),
        FieldPanel('leaving_date'),
        FieldPanel('website'),
        FieldPanel('abbreviation'),
        MultiFieldPanel([
            FieldPanel('office_address_line_1'),
            FieldPanel('office_contact_number'),

        ], heading="Office Address"),
        MultiFieldPanel([
            FieldPanel('home_address_line_1'),
            FieldPanel('home_contact_number'),
        ], heading="Residence Address"),

        ImageChooserPanel('photo'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('fac_research_categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('research_interests'),
        InlinePanel('gallery_images', label="Gallery images", max_num=10),
        InlinePanel('faculty_prev_work', label="Previous Work")
    ]
    # Creating custom tabs
    custom_tab_panels = [
        FieldPanel('additional_roles'),
        FieldPanel('laboratory_in_charge'),
        FieldPanel('faculty_in_charge'),
    ]

    announcement_tab_panels = [
        InlinePanel('faculty_announcement', label="Announcement", max_num=10),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Content"),
        ObjectList(custom_tab_panels, heading="Administration"),
        ObjectList(announcement_tab_panels, heading="Announcement"),
        ObjectList(Page.promote_panels, heading="Promote"),
        ObjectList(Page.settings_panels, heading="Settings"),
    ])

    def __str__(self):
        if self.middle_name == '':
            return self.first_name + " " + self.last_name
        return self.first_name + " " + self.middle_name + " " + self.last_name

    def get_context(self, request):
        lab_relation_list = self.faculty_lab.all()
        lab_incharge = self.faculty_incharge.all()
        lab_list = []
        for lab in lab_incharge:
            lab_list.append(lab)
        for lab_relation in lab_relation_list:
            lab = lab_relation.page
            lab_list.append(lab)

        pub_relation_list = self.faculty_pub.all()
        pub_list = []
        for pub_relation in pub_relation_list:
            pub = pub_relation.page
            if pub.pub_type == "2":
                pub_list.append(pub)
        pub_list.sort(key=lambda x: x.pub_year, reverse=True)
        try:
            pub_list = pub_list[:10]
        except:
            pass

        project_pi = self.pi.all()
        project_copi = self.copi.all()
        project_list = []
        project_list2 = []
        for project in project_pi:
            project_list.append(project.page)
        project_list.sort(key=lambda x: x.start_date, reverse=True)
        if len(project_list) < 4:
            for project in project_copi:
                project_list2.append(project.page)
        project_list += project_list2
        project_list.sort(key=lambda x: x.start_date, reverse=True)
        try:
            project_list = project_list[:4]
        except:
            pass

        course_relation_list = self.course_instructor.all()
        course_list = []
        for course_relation in course_relation_list:
            course = course_relation.page
            course_list.append(course)

        context = super().get_context(request)
        context['lab_list'] = lab_list
        context['pub_list'] = pub_list
        context['project_list'] = project_list
        context['course_list'] = course_list
        return context

    parent_page_types = ['FacultyHomePage']
    subpage_types = []

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculty"


class FacultyAnnouncement(Orderable):
    page = ParentalKey(FacultyPage, on_delete=models.CASCADE, related_name='faculty_announcement')
    link = models.URLField(max_length=250)
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    message = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    title = models.CharField(blank=True, max_length=50)
    date = models.DateTimeField(blank=True, default=timezone.now)
    panels = [
        FieldPanel('title'),
        FieldPanel('message'),
        FieldPanel('date'),
        DocumentChooserPanel('document'),
        FieldPanel('link'),
    ]


class FacultyPreviousWork(Orderable):
    page = ParentalKey(FacultyPage, on_delete=models.CASCADE, related_name='faculty_prev_work')
    about = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    title = models.CharField(blank=True, max_length=50)
    work_type = models.CharField(max_length=2, choices=FAC_PREV_WORK_TYPES, default='0')
    start_date = models.DateTimeField(blank=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, default=timezone.now)
    panels = [
        FieldPanel('title'),
        FieldPanel('about'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
    ]


class FacultyPageGalleryImage(Orderable):
    page = ParentalKey(FacultyPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('image'),
            FieldPanel('caption'),
        ]),
    ]


def faculty_interests():
    live_tags = FacultyResearchInterestTag.objects.all()
    common_tags = []
    for tag in live_tags:
        tag2 = tag.__str__().split('tagged with ', 1)
        tag3 = tag2.pop()
        if tag3 not in common_tags:
            common_tags.append(tag3)
    return common_tags


def get_hod():
    return FacultyPage.objects.filter(additional_roles='1')


######################################################
######################################################

class AbstractStudentHomePage(Page):
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    parent_page_types = ['MechHomePage']
    subpage_types = ['StudentPage']
    max_count = 1

    class Meta:
        abstract = True


class AbstractStudentPage(Page):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    roll_no = models.IntegerField(blank=True)
    enrolment_year = models.DateField(default=timezone.now)
    leaving_year = models.DateField(default=timezone.now, blank=True, null=True)
    programme = models.CharField(max_length=2, choices=STUDENT_PROGRAMME)
    is_exchange = models.BooleanField(default=False, verbose_name="International Student")
    contact_number = models.CharField(max_length=20, blank=True)
    hostel_address = models.CharField(max_length=25, blank=True)
    specialization = models.CharField(max_length=2, choices=MASTERS_SPECIALIZATION, default='0',
                                      help_text="Not Applicable - for B.Tech, PhD and PostDocs")
    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    website = models.URLField(max_length=250, blank=True)

    def __str__(self):
        if self.middle_name == '':
            return self.first_name + " " + self.last_name
        return self.first_name + " " + self.middle_name + " " + self.last_name

    def get_roll_value(self):
        return self.roll_no

    # def get_enrolment_year(self):
    # 	roll_no_str = str(self.roll_no)
    # 	enrl_yr = datetime.strptime('Aug 1 20'+roll_no[0:2]+' 12:00PM', '%b %d %Y %I:%M%p')
    # 	return enrl_yr

    parent_page_types = ['StudentHomePage']
    subpage_types = []

    def __str__(self):
        return self.first_name + "" + self.middle_name + " " + self.last_name

    class Meta:
        abstract = True


######################################################
class StudentHomePage(AbstractStudentHomePage):
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    btech_body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    mtech_body= RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    phd_body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('btech_body'),
        FieldPanel('mtech_body'),
        FieldPanel('phd_body')
    ]

    def serve(self, request):
        student_list = self.get_children().live().order_by('-studentpage__enrolment_year', 'studentpage__first_name',
                                                           'studentpage__middle_name', 'studentpage__last_name')

        # Filter by programme
        prog = request.GET.get('prog')
        if prog in ['0', '1', '2', '3']:
            student_list = student_list.filter(studentpage__programme=prog)

        # Filter by tag
        # tag = request.GET.get('tag')
        # if tag:
        #     student_list = student_list.filter(studentpage__research_interests__name=tag)
        year = request.GET.get('year')
        if year:
            student_list = student_list.filter(studentpage__enrolment_year__year=year)

        # paginator = Paginator(student_list, 50)  # Show 50 students per page
        # page_no = request.GET.get('page_no')
        # student_list = paginator.get_page(page_no)

        # all_research_interests = student_interests()
        return render(request, self.template, {
            'page': self,
            'student_list': student_list,
            # 'all_research_interests': all_research_interests,
            # 'tag': tag,
            # 'page_no': page_no,
            'prog': prog,
            'year': year,
        })

    class Meta:
        verbose_name = "Student Home"


# class StudentResearchInterestTag(TaggedItemBase):
#     content_object = ParentalKey(
#         'StudentPage',
#         related_name='tagged_items',
#         on_delete=models.CASCADE
#     )


class StudentPage(AbstractStudentPage):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='student', null=True, on_delete=models.SET_NULL)
    faculty_advisor = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Main supervisor/Faculty Advisor', related_name='faculty_advisor')
    # research_interests = ClusterTaggableManager(through=StudentResearchInterestTag, blank=True,
    #                                             verbose_name='Research Interests')

    content_panels = Page.content_panels + [
        ######################################################
        # The user should not be able to change these things from here
        FieldPanel('user'),
        FieldPanel('first_name'),
        FieldPanel('middle_name'),
        FieldPanel('last_name'),
        FieldPanel('email_id'),
        FieldPanel('roll_no'),
        FieldPanel('enrolment_year'),
        FieldPanel('leaving_year'),
        FieldPanel('programme'),
        ######################################################
        FieldPanel('specialization'),
        FieldPanel('is_exchange'),
        FieldPanel('website'),
        FieldPanel('contact_number'),
        FieldPanel('hostel_address'),

        ImageChooserPanel('photo'),
        FieldPanel('intro'),
        FieldPanel('body'),

        AutocompletePanel('faculty_advisor', target_model='mechweb.FacultyPage'),
		# shouldn't this be with faculty, so that studen't can't change faculty advisor by their own.
        # FieldPanel('research_interests'),
        InlinePanel('stud_gallery_images', label="Gallery images", max_num=2),
        InlinePanel('stud_links', label="Related Links", max_num=10),
    ]

    project_tab_panels = [
        InlinePanel('projects', label="Projects"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Content"),
        ObjectList(project_tab_panels, heading="Projects"),
        ObjectList(Page.promote_panels, heading="Promote"),
        ObjectList(Page.settings_panels, heading="Settings"),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('first_name'),
        index.FilterField('enrolment_year'),
    ]

    def get_context(self, request):
        lab_relation_list = self.student_lab.all()
        lab_list = []
        for lab_relation in lab_relation_list:
            lab = lab_relation.page
            lab_list.append(lab)

        pub_relation_list = self.student_pub.all()
        pub_list = []
        for pub_relation in pub_relation_list:
            pub = pub_relation.page
            pub_list.append(pub)
        # return lab_list
        context = super().get_context(request)
        context['lab_list'] = lab_list
        context['pub_list'] = pub_list
        return context

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class StudentProject(Orderable):
    page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(blank=True, max_length=50)
    guide = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='guide')
    co_guide = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name='co_guide')
    document = models.ForeignKey('wagtaildocs.Document', null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name='+')
    photo_1 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='+')
    photo_2 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='+')
    photo_3 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='+')
    abstract = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    link = models.URLField(max_length=250, blank=True)
    panels = [
        FieldPanel('title'),
        AutocompletePanel('guide', target_model='mechweb.FacultyPage'),
        AutocompletePanel('co_guide', target_model='mechweb.FacultyPage'),
        DocumentChooserPanel('document'),
        FieldPanel('abstract'),
        FieldPanel('link'),
        MultiFieldPanel([
            ImageChooserPanel('photo_1'),
            ImageChooserPanel('photo_2'),
            ImageChooserPanel('photo_3'),
        ], heading="Featured Photos")

    ]


class StudentPageLink(Orderable):
    page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='stud_links')
    link = models.URLField(max_length=250)
    panels = [
        FieldPanel('link'),
    ]


class StudentPageGalleryImage(Orderable):
    page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='stud_gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('image'),
            FieldPanel('caption'),
        ]),
    ]


# def student_interests():
#     live_tags = StudentResearchInterestTag.objects.all()
#     common_tags = []
#     for tag in live_tags:
#         tag2 = tag.__str__().split('tagged with ', 1)
#         tag3 = tag2.pop()
#         if tag3 not in common_tags:
#             common_tags.append(tag3)
#     return common_tags


######################################################
class StaffHomePage(Page):
    # nav_order = models.CharField(max_length=1, default=NAV_ORDER[4])
    # use_other_template = models.IntegerField(default = 3)#Find a way to remove this shit without deleting the original entry - had to delete original entry - but not because i specifically wanted to remove it, but because i had to implement user model
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        # FieldPanel('use_other_template')
    ]

    parent_page_types = ['MechHomePage']
    subpage_types = ['StaffPage']
    max_count = 1

    def serve(self, request):
        staff_list = self.get_children().live().order_by('staffpage__first_name', 'staffpage__middle_name',
                                                         'staffpage__last_name')

        # Filter by designation
        desig = request.GET.get('desig')
        if desig in ['0', '1', '2', '3']:
            staff_list = staff_list.filter(staffpage__designation=desig)

        # Filter by skills tag
        tag = request.GET.get('tag')
        if tag:
            staff_list = staff_list.filter(staffpage__skills__name=tag)

        paginator = Paginator(staff_list, 50)  # Show 10 faculty per page
        page_no = request.GET.get('page_no')
        staff_list = paginator.get_page(page_no)

        all_staff_skills = staff_skills()
        return render(request, self.template, {
            'page': self,
            'staff_list': staff_list,
            'all_staff_skills': all_staff_skills,
            'tag': tag,
            'page_no': page_no,
            'desig': desig,
        })

    # and this too
    # def get_template(self,request):
    # 	return 'mechweb/staff_home_page.html'

    class Meta:
        verbose_name = "Staff Home"


class StaffSkillag(TaggedItemBase):
    content_object = ParentalKey(
        'StaffPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class StaffPage(Page):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='staff', null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    responsibilities = models.CharField(max_length=500, null=True, blank=True)

    designation = models.CharField(max_length=2, choices=STAFF_DESIGNATION, default='15')
    joining_year = models.DateField(default=timezone.now, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    intro = models.CharField(max_length=250, blank=True)
    skills = ClusterTaggableManager(through=StaffSkillag, blank=True, verbose_name='Skills')

    # if lab staff:
    # lab = models.ForeignKey('ResearchLabPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='lab')

    content_panels = Page.content_panels + [
        ######################################################
        # The user should not be able to change these things from here
        FieldPanel('user'),
        FieldPanel('first_name'),
        FieldPanel('middle_name'),
        FieldPanel('last_name'),
        FieldPanel('email_id'),
        ######################################################
        # The user should not be able to change these things from here
        FieldPanel('designation'),
        FieldPanel('joining_year'),
        FieldPanel('contact_number'),
        FieldPanel('address'),
        FieldPanel('intro'),
        ImageChooserPanel('photo'),
        FieldPanel('skills'),
    ]

    parent_page_types = ['StaffHomePage']
    subpage_types = []

    def __str__(self):
        if self.middle_name == '':
            return self.first_name + " " + self.last_name
        return self.first_name + " " + self.middle_name + " " + self.last_name

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"


def staff_skills():
    live_tags = StaffSkillag.objects.all()
    common_tags = []
    for tag in live_tags:
        tag2 = tag.__str__().split('tagged with ', 1)
        tag3 = tag2.pop()
        if tag3 not in common_tags:
            common_tags.append(tag3)
    return common_tags


######################################################
class AlumniHomePage(AbstractStudentHomePage):
    content_panels = AbstractStudentHomePage.content_panels + [
        InlinePanel('distinguished_alumni', label="Distinguished Alumni", max_num=10),
    ]

    parent_page_types = ['MechHomePage']
    subpage_types = ['AlumnusPage']
    max_count = 1

    def serve(self, request):
        alumni_list = self.get_children().live().order_by('alumnuspage__programme', 'alumnuspage__enrolment_year')

        all_interests = alumni_interests()
        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            alumni_list = alumni_list.filter(alumnuspage__interests__name=tag)
        paginator = Paginator(alumni_list, 10)  # Show 10 alum per page
        page_no = request.GET.get('page_no')
        alumni_list = paginator.get_page(page_no)

        return render(request, self.template, {
            'page': self,
            'alumni_list': alumni_list,
            'all_interests': all_interests,
            'tag': tag,
            'page_no': page_no,
        })

    class Meta:
        verbose_name = "Alumni Home"


class AlumniInterestTag(TaggedItemBase):
    content_object = ParentalKey(
        'AlumnusPage',
        related_name='alumni_tagged_items',
        on_delete=models.CASCADE
    )


class AlumnusPage(AbstractStudentPage):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='alumnus', null=True, on_delete=models.SET_NULL)
    contact_number_2 = models.CharField(max_length=20, blank=True)
    email_id_2 = models.EmailField(blank=True)
    address_line_1 = models.CharField(max_length=100, blank=True)
    address_line_2 = models.CharField(max_length=50, blank=True)
    address_line_3 = models.CharField(max_length=25, blank=True)
    interests = ClusterTaggableManager(through=AlumniInterestTag, blank=True, verbose_name='Interests')

    content_panels = Page.content_panels + [
        ######################################################
        # The user should not be able to change these things from here
        FieldPanel('user'),
        FieldPanel('first_name'),
        FieldPanel('middle_name'),
        FieldPanel('last_name'),
        FieldPanel('programme'),
        FieldPanel('roll_no'),
        FieldPanel('enrolment_year'),
        FieldPanel('email_id'),
        ######################################################
        FieldPanel('specialization'),
        FieldPanel('is_exchange'),
        FieldPanel('website'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('contact_number'),
                FieldPanel('contact_number_2'),
            ]),
        ], heading="Contact Numbers"),
        MultiFieldPanel([
            FieldPanel('address_line_1'),
            FieldPanel('address_line_2'),
            FieldPanel('address_line_3'),
        ], heading="Current Address"),
        FieldPanel('hostel_address'),

        ImageChooserPanel('photo'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('email_id_2'),
        InlinePanel('alum_gallery_images', label="Gallery images", max_num=5),
        InlinePanel('alum_links', label="Related Links", max_num=10),
        FieldPanel('interests'),
    ]

    job_tab_panels = [
        InlinePanel('job_details', label="Job Details", max_num=3),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Content"),
        ObjectList(job_tab_panels, heading="Job Details"),
        ObjectList(Page.promote_panels, heading="Promote"),
        ObjectList(Page.settings_panels, heading="Settings"),
    ])

    parent_page_types = ['AlumniHomePage']
    subpage_types = []

    class Meta:
        verbose_name = "Alumnus"
        verbose_name_plural = "Alumni"


class AlumnusPageJobDetail(Orderable):
    page = ParentalKey(AlumnusPage, on_delete=models.CASCADE, related_name='job_details')
    title = models.CharField(max_length=20)
    company = models.CharField(max_length=20, blank=True)
    work_details = models.CharField(max_length=500, blank=True)
    link = models.URLField(max_length=250, blank=True)
    panels = [
        FieldPanel('title'),
        FieldPanel('company'),
        FieldPanel('work_details'),
        FieldPanel('link'),
    ]


class AlumnusPageLink(Orderable):
    page = ParentalKey(AlumnusPage, on_delete=models.CASCADE, related_name='alum_links')
    link = models.URLField(max_length=250)
    panels = [
        FieldPanel('link'),
    ]


class AlumnusPageGalleryImage(Orderable):
    page = ParentalKey(AlumnusPage, on_delete=models.CASCADE, related_name='alum_gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('image'),
            FieldPanel('caption'),
        ]),
    ]


class DistinguishedAlumni(Orderable):
    page = ParentalKey(AlumniHomePage, on_delete=models.CASCADE, related_name='distinguished_alumni')
    distinguished_alumnus = models.ForeignKey('AlumnusPage', null=True, blank=True, on_delete=models.SET_NULL,
                                              related_name='distinguished_alumnus')
    about = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('distinguished_alumnus', target_model='mechweb.AlumnusPage'),
        FieldPanel('about'),
    ]


def alumni_interests():
    live_tags = AlumniInterestTag.objects.all()
    common_tags = []
    for tag in live_tags:
        tag2 = tag.__str__().split('tagged with ', 1)
        tag3 = tag2.pop()
        if tag3 not in common_tags:
            common_tags.append(tag3)
    return common_tags


# # How to make this function, student_interests() and faculty_interests() into one?
######################################################
# def get_categories():
# 	return CategoriesHome.objects.all()[0].get_children().live().order_by('-categories__category')
######################################################

class ResearchHomePage(Page):
    # nav_order = models.CharField(max_length=1, default=NAV_ORDER[5])
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('featured_research', label="Featured Research", max_num=10),
    ]

    parent_page_types = ['MechHomePage']
    subpage_types = ['ResearchLabHomePage', 'PublicationHomePage', 'ProjectHomePage']
    max_count = 1

    class Meta:
        verbose_name = "Research Home"


class FeaturedResearch(Orderable):
    page = ParentalKey(ResearchHomePage, on_delete=models.CASCADE, related_name='featured_research')
    featured_research = models.ForeignKey('PublicationPage', null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='featured_research')
    panels = [
        AutocompletePanel('featured_research', target_model='mechweb.PublicationPage'),
    ]


# ------------------------------------------
class ResearchLabHomePage(Page):
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('lab_home_gallery_images', label="Gallery images", max_num=3),
    ]

    parent_page_types = ['ResearchHomePage']
    subpage_types = ['ResearchLabPage']
    max_count = 1

    def serve(self, request):
        lab_list = self.get_children().live().order_by('researchlabpage__lab_type', 'researchlabpage__name')

        # Filter by research area

        ugpg = request.GET.get('ugpg')
        if ugpg in ['0', '1']:
            lab_list = lab_list.filter(researchlabpage__lab_type=ugpg)

        return render(request, self.template, {
            'page': self,
            'lab_list': lab_list,
            'ugpg': ugpg,
        })

    class Meta:
        verbose_name = "Lab Home"


class ResearchPageGalleryImage(Orderable):
    page = ParentalKey(ResearchLabHomePage, on_delete=models.CASCADE, related_name='lab_home_gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('image'),
            FieldPanel('caption'),
        ]),
    ]


class ResearchLabPage(Page):
    name = models.CharField(max_length=100)
    lab_type = models.CharField(max_length=2, choices=LAB_TYPES, default='0')
    # When already defined in faculty model who is lab incharge... then do we need it here?
    faculty_incharge = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='faculty_incharge')
    scientific_officer = models.ForeignKey('StaffPage', null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='scientific_officer')
    intro = models.CharField(max_length=500, blank=True)
    body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    photo_1 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='+')
    photo_2 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='+')
    photo_3 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('lab_type'),
        FieldPanel('contact_number'),
        FieldPanel('address'),
        FieldPanel('intro'),
        FieldPanel('body'),
        MultiFieldPanel([
            FieldRowPanel([
                ImageChooserPanel('photo_1'),
                ImageChooserPanel('photo_2'),
                ImageChooserPanel('photo_3'),
            ]),
        ], heading="Featured Photos"),
        InlinePanel('links', label="Related Links", max_num=10),
    ]

    lab_equipment_panels = [
        InlinePanel('equipment', label="Lab Equipments"),
    ]

    people_panels = [
        AutocompletePanel('faculty_incharge', target_model='mechweb.FacultyPage'),
        AutocompletePanel('scientific_officer', target_model='mechweb.StaffPage'),
        InlinePanel('faculty', label="Faculty"),
        InlinePanel('students', label="Students"),
        InlinePanel('tech_staffs', label="Technical Staff", max_num=10),
        InlinePanel('interns', label="Intern"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Content"),
        ObjectList(people_panels, heading="People"),
        ObjectList(lab_equipment_panels, heading="Equipments"),
        ObjectList(Page.promote_panels, heading="Promote"),
        ObjectList(Page.settings_panels, heading="Settings"),
    ])

    parent_page_types = ['ResearchLabHomePage']
    subpage_types = []

    class Meta:
        verbose_name = "Lab"
        verbose_name_plural = "Labs"


class LabEquipment(Orderable):
    company = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=250, blank=True)
    page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='equipment')
    operator = models.ForeignKey('StaffPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='operator')
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    specifications = RichTextField(blank=True, features=CUSTOM_RICHTEXT, verbose_name='Description')
    cost = models.FloatField(blank=True, null=True)
    date_of_procurement = models.DateField(blank=True, null=True)
    link = models.URLField(max_length=250, blank=True)
    photo_1 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='+')
    funding_agency = models.CharField(max_length=50, blank=True)
    funding_agency_link = models.URLField(max_length=250, blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('company'),
        AutocompletePanel('operator', target_model='mechweb.StaffPage'),
        DocumentChooserPanel('document'),
        FieldPanel('specifications'),
        FieldPanel('link'),
        FieldPanel('cost'),
        FieldPanel('date_of_procurement'),
        ImageChooserPanel('photo_1'),
        MultiFieldPanel([
            FieldPanel('funding_agency'),
            FieldPanel('funding_agency_link'),

        ], heading="Funding Agency"),
    ]


class ResearchLabPageLink(Orderable):
    page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='links')
    link = models.URLField(max_length=250)
    panels = [
        FieldPanel('link'),
    ]


class ResearchLabFaculty(Orderable):
    page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='faculty')
    faculty = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='faculty_lab')
    research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('faculty', target_model='mechweb.FacultyPage'),
        FieldPanel('research_statement'),
    ]


class ResearchLabStudents(Orderable):
    page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='students')
    student = models.ForeignKey('StudentPage', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='student_lab')
    research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('student', target_model='mechweb.StudentPage'),
        FieldPanel('research_statement'),
    ]


class ResearchLabTechStaff(Orderable):
    page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='tech_staffs')
    tech_staff = models.ForeignKey('StaffPage', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='tech_staff_lab')
    responsibilities = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('tech_staff', target_model='mechweb.StaffPage'),
        FieldPanel('responsibilities'),
    ]


class ResearchLabIntern(Orderable):
    page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='interns')
    name = models.CharField(max_length=250)
    institute = models.CharField(max_length=250)
    start = models.DateField(default=timezone.now)
    end = models.DateField(default=timezone.now)

    panels = [
        FieldPanel('name'),
        FieldPanel('institute'),
        FieldPanel('start'),
        FieldPanel('end'),
    ]
    # class Meta:
    #     ordering = ['end']


# ------------------------------------------
class PublicationHomePage(Page):
    # Add featured publications
    parent_page_types = ['ResearchHomePage']
    subpage_types = ['PublicationPage']
    max_count = 1

    def serve(self, request):
        pub_list = self.get_children().live().order_by('-publicationpage__pub_year', '-publicationpage__citations')
        year_list = []
        year = timezone.now().year
        for i in range(year, 1996, -1):
            year_list.append(i)

        pub_type = request.GET.get('pub_type')
        if pub_type:
            pub_list = pub_list.filter(publicationpage__pub_type=pub_type)
        # elif year is 0:
        # 	pub_list = pub_list.filter(publicationpage__pub_year__year=year)

        # paginator = Paginator(pub_list, 50)
        # page_no = request.GET.get('page_no')
        # pub_list = paginator.get_page(page_no)

        return render(request, self.template, {
            'page': self,
            'pub_list': pub_list,
            # 'year':year,
            # 'page_no':page_no,
            'pub_type': pub_type,
            'year_list': year_list,
        })

    class Meta:
        verbose_name = "Publication Home"


class PublicationPage(Page):
    # page = ParentalKey(PublicationHomePage, on_delete=models.PROTECT, related_name='publication')
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(max_length=500)
    abstract = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    pub_type = models.CharField(max_length=2, choices=PUBLICATION_TYPES, default='0')
    download_link = models.URLField(blank=True, max_length=100)
    pub_issue = models.CharField(max_length=100, null=True, blank=True)
    pub_year = models.DateField(default=timezone.now)
    pub_journal = models.CharField(max_length=300, blank=True)
    pub_vol = models.CharField(max_length=200, blank=True)
    page_start = models.CharField(max_length=50, blank=True)
    page_end = models.CharField(max_length=50, blank=True)
    citations = models.CharField(max_length=10, blank=True)
    alt_detail_text = models.CharField(max_length=1000, blank=True,
                                       help_text="Add any other type of data, like ISBN number, publisher etc")
    alt_people_text = models.CharField(max_length=1000, blank=True,
                                       help_text="Add the exact sequence of names as in the publication")
    # pub_conference =
    # pub_patent_number =
    # pub_

    content_panels = Page.content_panels + [
        DocumentChooserPanel('document'),
        FieldPanel('name'),
        FieldPanel('pub_type'),
        FieldPanel('pub_year'),
        FieldPanel('alt_detail_text'),
        FieldPanel('pub_journal'),
        FieldPanel('pub_vol'),
        FieldPanel('pub_issue'),
        FieldPanel('page_start'),
        FieldPanel('page_end'),
        FieldPanel('citations'),
        FieldPanel('abstract'),
        FieldPanel('download_link'),
        InlinePanel('images', label="Images", max_num=2),
        InlinePanel('links', label="Links", max_num=10),
    ]

    people_panels = [

        InlinePanel('faculty', label="Faculty"),
        InlinePanel('other_authors', label="Other Authors"),
        InlinePanel('students', label="Students"),
        FieldPanel('alt_people_text'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Content"),
        ObjectList(people_panels, heading="People"),
        ObjectList(Page.promote_panels, heading="Promote"),
        ObjectList(Page.settings_panels, heading="Settings"),
    ])

    parent_page_types = ['PublicationHomePage']
    subpage_types = []

    def get_authors(self):
        l = ""
        for fac in self.faculty.select_related().all():
            l += fac.faculty.__str__() + ", "
        for other in self.other_authors.select_related().all():
            l += other.name + ", "
        for stud in self.students.select_related().all():
            l += stud.student.__str__() + ", "
        if l == "":
            return self.alt_people_text
        return l[:-2]

    # def __str__(self):
    # 	l = ""
    # 	if self.alt_people_text != "":
    # 		l = l+self.alt_people_text
    # 	if self.name != "":
    # 		l = l+', "'+self.name+'"'
    # 	if self.pub_journal != "":
    # 		l = l+", "+self.pub_journal
    # 	if pub.vol != "":
    # 		l = l+", vol. "+self.pub_vol
    # 	if self.pub_issue != "":
    # 		l = l+" : "+self.pub_issue
    # 	if self.page_start != "" && self.page_end != "":
    # 		l = l+", pp. "+self.page_start+"-"+self.page_end
    # 	if self.pub_year:
    # 		l = l+", "+str(self.pub_year.year)
    # 	return l

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"


class PublicationPageStudent(Orderable):
    page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='students')
    student = models.ForeignKey('StudentPage', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='student_pub')
    research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('student', target_model='mechweb.StudentPage'),
        FieldPanel('research_statement'),
    ]


class PublicationPageFaculty(Orderable):
    page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='faculty')
    faculty = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='faculty_pub')
    research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('faculty', target_model='mechweb.FacultyPage'),
        FieldPanel('research_statement'),
    ]


class PublicationPageOtherAuthor(Orderable):
    page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='other_authors')
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('organization'),
    ]


class PublicationPageGalleryImage(Orderable):
    page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='images')
    photo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('photo'),
            FieldPanel('caption'),
        ]),
    ]


# Is this going to be useful?
class PublicationPageLink(Orderable):
    page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='links')
    link = models.URLField(max_length=250)
    panels = [
        FieldPanel('link'),
    ]


# ------------------------------------------
class ProjectHomePage(Page):
    parent_page_types = ['ResearchHomePage']
    subpage_types = ['ProjectPage']
    max_count = 1

    def serve(self, request):
        project_list = ProjectPage.objects.all().order_by('-end_date', '-budget')
        sponsored_projs = project_list.filter(project_type=1)
        consultancy_projs = project_list.filter(project_type=0)
        return render(request, self.template,{
            'page': self,
            'sponsored_projs':sponsored_projs,
            'consultancy_projs':consultancy_projs,
        })

    class Meta:
        verbose_name = "Project Home"


class ProjectPage(Page):
    description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    name = models.CharField(max_length=500)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    budget = models.CharField(blank=True, max_length=100)
    funding_agency = models.CharField(blank=True, max_length=100)
    funding_agency_link = models.URLField(blank=True, max_length=100)
    project_type = models.CharField(max_length=20, default='1', choices=PROJECT_TYPES)
    alt_PI_text = models.CharField(max_length=1000, blank=True,
                                   help_text="Use this only if you can't add faculty and other authors above")

    content_panels = Page.content_panels + [
        FieldPanel('project_type'),
        FieldPanel('name'),
        FieldPanel('description'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('start_date'),
                FieldPanel('end_date'),
            ]),
        ], heading="Duration"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('funding_agency'),
                FieldPanel('funding_agency_link'),
                FieldPanel('budget'),
            ]),
        ], heading="Funding details"),
        InlinePanel('links', label="Links", max_num=10),
        InlinePanel('gallery_images', label="Gallery images", max_num=3),
    ]

    people_panels = [
        InlinePanel('faculty_pi', label="Principal Investigator", max_num=1),
        InlinePanel('faculty_copi', label="Co Investigator"),
        InlinePanel('oi', label="Other Investigators"),
        FieldPanel('alt_PI_text')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Content"),
        ObjectList(people_panels, heading="People"),
        ObjectList(Page.promote_panels, heading="Promote"),
        ObjectList(Page.settings_panels, heading="Settings"),
    ])

    parent_page_types = ['ProjectHomePage']
    subpage_types = []

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class ProjectPageFacultyPI(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='faculty_pi')
    faculty = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='pi')
    project_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('faculty', target_model='mechweb.FacultyPage'),
        FieldPanel('project_statement'),
    ]


class ProjectPageFacultyCoPI(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='faculty_copi')
    faculty = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='copi')
    project_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('faculty', target_model='mechweb.FacultyPage'),
        FieldPanel('project_statement'),
    ]


class ProjectPageOtherInvestigator(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='oi')
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('organization'),
    ]


class ProjectPageLink(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='links')
    link = models.URLField(max_length=250)
    panels = [
        FieldPanel('link'),
    ]


class ProjectPageGalleryImage(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('image'),
            FieldPanel('caption'),
        ]),
    ]


#####################################################
# def total_credits(sem):
# 	tc=0
# 	for course in sem:
# 		tc+=course.specific.credits
# 	return tc

class CourseStructure(Page):
    # nav_order = models.CharField(max_length=1, default=NAV_ORDER[6])

    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('featured_courses', label="Featured Courses", max_num=10),
    ]
    parent_page_types = ['MechHomePage']
    subpage_types = ['CoursePage']
    max_count = 1

    def serve(self, request):
        course_list = self.get_children().live().order_by('-coursepage__credits', 'coursepage__code')
        # Filter by programme
        prog = request.GET.get('prog')
        structure = []
        if prog == '0':
            sem1 = course_list.filter(coursepage__zero='1').filter(coursepage__zero_sem=1)
            structure.append(sem1)
            sem2 = course_list.filter(coursepage__zero='1').filter(coursepage__zero_sem=2)
            structure.append(sem2)
            sem3 = course_list.filter(coursepage__zero='1').filter(coursepage__zero_sem=3)
            structure.append(sem3)
            sem4 = course_list.filter(coursepage__zero='1').filter(coursepage__zero_sem=4)
            structure.append(sem4)
            sem5 = course_list.filter(coursepage__zero='1').filter(coursepage__zero_sem=5)
            structure.append(sem5)
            sem6 = course_list.filter(coursepage__zero='1').filter(coursepage__zero_sem=6)
            structure.append(sem6)
            sem7 = course_list.filter(coursepage__zero='1').filter(coursepage__zero_sem=7)
            structure.append(sem7)
            sem8 = course_list.filter(coursepage__zero='1').filter(coursepage__zero_sem=8)
            structure.append(sem8)
        elif prog == '1':
            sem1 = course_list.filter(coursepage__one='1').filter(coursepage__one_sem=1)
            structure.append(sem1)
            sem2 = course_list.filter(coursepage__one='1').filter(coursepage__one_sem=2)
            structure.append(sem2)
            sem3 = course_list.filter(coursepage__one='1').filter(coursepage__one_sem=3)
            structure.append(sem3)
            sem4 = course_list.filter(coursepage__one='1').filter(coursepage__one_sem=4)
            structure.append(sem4)
        elif prog == '2':
            sem1 = course_list.filter(coursepage__two='1').filter(coursepage__two_sem=1)
            structure.append(sem1)
            sem2 = course_list.filter(coursepage__two='1').filter(coursepage__two_sem=2)
            structure.append(sem2)
            sem3 = course_list.filter(coursepage__two='1').filter(coursepage__two_sem=3)
            structure.append(sem3)
            sem4 = course_list.filter(coursepage__two='1').filter(coursepage__two_sem=4)
            structure.append(sem4)
        elif prog == '3':
            sem1 = course_list.filter(coursepage__three='1').filter(coursepage__three_sem=1)
            structure.append(sem1)
            sem2 = course_list.filter(coursepage__three='1').filter(coursepage__three_sem=2)
            structure.append(sem2)
            sem3 = course_list.filter(coursepage__three='1').filter(coursepage__three_sem=3)
            structure.append(sem3)
            sem4 = course_list.filter(coursepage__three='1').filter(coursepage__three_sem=4)
            structure.append(sem4)
        elif prog == '4':
            sem1 = course_list.filter(coursepage__four='1').filter(coursepage__four_sem=1)
            structure.append(sem1)
            sem2 = course_list.filter(coursepage__four='1').filter(coursepage__four_sem=2)
            structure.append(sem2)
            sem3 = course_list.filter(coursepage__four='1').filter(coursepage__four_sem=3)
            structure.append(sem3)
            sem4 = course_list.filter(coursepage__four='1').filter(coursepage__four_sem=4)
            structure.append(sem4)
        elif prog == '5':
            sem1 = course_list.filter(coursepage__five='1').filter(coursepage__five_sem=1)
            structure.append(sem1)
            sem2 = course_list.filter(coursepage__five='1').filter(coursepage__five_sem=2)
            structure.append(sem2)
            sem3 = course_list.filter(coursepage__five='1').filter(coursepage__five_sem=3)
            structure.append(sem3)
            sem4 = course_list.filter(coursepage__five='1').filter(coursepage__five_sem=4)
            structure.append(sem4)
        elif prog == '6':
            sem1 = course_list.filter(coursepage__six='1').filter(coursepage__six_sem=1)
            structure.append(sem1)
        elif prog == '7':
            course_list = course_list.filter(coursepage__seven='1')
            # structure+=course_list
        else:
            # structure+=course_list
            pass
        # credits = []
        # for sem in structure:
        # 	credits.append(total_credits(sem))
        # credits.append(sum(credits))
        return render(request, self.template, {
            'page': self,
            'course_list': course_list,
            'prog': prog,
            'structure': structure,
            # 'credits':credits,
        })

    class Meta:
        verbose_name = "Course Structure"
        verbose_name_plural = "CourseStructure"


# class CourseProgrammes(Page):
# 	category = models.CharField(max_length=2, choices=STUDENT_PROGRAMME, default='0', unique=True)
# 	content_panels = Page.content_panels + [
# 			FieldPanel('category'),
# 		]
# 	parent_page_types=['CategoriesHome']
# 	max_count = 4

# 	def serve(self, request):
# 		course_list = self.courses.all()
# 		return render(request, self.template, {
# 			'page': self,
# 			'course_list': course_list,
# 		})

# class CourseSpecializations(Page):
# 	category = models.CharField(max_length=2, choices=MASTERS_SPECIALIZATION, default='0', unique=True)
# 	# semester = models.CharField(max_length=2, default='1')
# 	content_panels = Page.content_panels + [
# 			FieldPanel('category'),
# 			# FieldPanel('semester'),# check if this category is checked - if yes, then filling this field should be mandatory
# 		]
# 	parent_page_types=['CategoriesHome']
# 	max_count = 6

# def serve(self, request):
# 	course_list = self.courses.all()
# 	return render(request, self.template, {
# 		'page': self,
# 		'course_list': course_list,
# 	})

class CoursePage(Page):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    photo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    lectures = models.IntegerField(verbose_name="L")
    tutorials = models.IntegerField(verbose_name="T")
    practicals = models.IntegerField(verbose_name="P")
    credits = models.IntegerField(verbose_name="C")
    # semester = models.IntegerField()

    eligible_programmes = models.CharField(max_length=2, choices=STUDENT_PROGRAMME, default='0')
    course_type = models.CharField(max_length=2, choices=COURSE_TYPES, default='0')
    zero = models.BooleanField(default=True, verbose_name="B. Tech")
    zero_sem = models.IntegerField(blank=True, null=True, verbose_name="Semester")
    one = models.BooleanField(default=False, verbose_name="M.Tech: Aerodynamics & Propulsion ")
    one_sem = models.IntegerField(blank=True, null=True, verbose_name="Semester")
    two = models.BooleanField(default=False, verbose_name="M.Tech: Manufacturing Science and Engineering")
    two_sem = models.IntegerField(blank=True, null=True, verbose_name="Semester")
    three = models.BooleanField(default=False, verbose_name="M.Tech: Computational Mechanics")
    three_sem = models.IntegerField(blank=True, null=True, verbose_name="Semester")
    four = models.BooleanField(default=False, verbose_name="M.Tech: Fluids and Thermal")
    four_sem = models.IntegerField(blank=True, null=True, verbose_name="Semester")
    five = models.BooleanField(default=False, verbose_name="M.Tech: Machine Design")
    five_sem = models.IntegerField(blank=True, null=True, verbose_name="Semester")
    six = models.BooleanField(default=False, verbose_name="PhD")
    six_sem = models.IntegerField(blank=True, null=True, verbose_name="Semester")
    seven = models.BooleanField(default=False, verbose_name="PG Electives")
    seven_sem = models.IntegerField(blank=True, null=True, verbose_name="Semester")

    # eligible_programmes = ParentalManyToManyField('mechweb.CourseProgrammes', blank=True, related_name='courses')
    # eligible_specializations = ParentalManyToManyField('mechweb.CourseSpecializations', blank=True, related_name='courses')
    description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    course_page_link = models.URLField(blank=True)
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Syllabus',
    )  # if can add function to add multiple students at once, then and only then add this.
    # list_of_students =

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        MultiFieldPanel([
            FieldPanel('code'),
            FieldPanel('course_type'),
            FieldPanel('eligible_programmes'),
            # FieldPanel('eligible_programmes',widget=forms.CheckboxSelectMultiple),
            # FieldPanel('eligible_specializations', widget=forms.CheckboxSelectMultiple),
            DocumentChooserPanel('document'),
            FieldPanel('course_page_link'),
        ], heading="Course Details"),
        FieldPanel('description'),
        ImageChooserPanel('photo'),
        InlinePanel('course_instructor', label="Course Instructor"),
    ]

    eligibility_and_sem_panels = [
        FieldRowPanel([
            FieldPanel('zero'),
            FieldPanel('zero_sem'),
        ]),
        FieldRowPanel([
            FieldPanel('one'),
            FieldPanel('one_sem'),
        ]),
        FieldRowPanel([
            FieldPanel('two'),
            FieldPanel('two_sem'),
        ]),
        FieldRowPanel([
            FieldPanel('three'),
            FieldPanel('three_sem'),
        ]),
        FieldRowPanel([
            FieldPanel('four'),
            FieldPanel('four_sem'),
        ]),
        FieldRowPanel([
            FieldPanel('five'),
            FieldPanel('five_sem'),
        ]),
        FieldRowPanel([
            FieldPanel('six'),
            FieldPanel('six_sem'),
        ]),
        FieldRowPanel([
            FieldPanel('seven'),
            FieldPanel('seven_sem'),
        ]),

        FieldRowPanel([
            FieldPanel('lectures'),
            FieldPanel('tutorials'),
            FieldPanel('practicals'),
            FieldPanel('credits'),
        ]),
    ]

    announcement_tab_panels = [
        InlinePanel('course_announcements', label="Announcement"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="Content"),
        ObjectList(eligibility_and_sem_panels, heading="Eligibility and Semester"),
        ObjectList(announcement_tab_panels, heading="Announcements"),
        ObjectList(Page.promote_panels, heading="Promote"),
        ObjectList(Page.settings_panels, heading="Settings"),
    ])

    parent_page_types = ['CourseStructure']
    subpage_types = []

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class CoursePageFaculty(Orderable):
    page = ParentalKey(CoursePage, on_delete=models.CASCADE, related_name='course_instructor')
    faculty = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='course_instructor')
    session = models.DateField(verbose_name="Instruction start date", default=timezone.now)
    introduction = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    panels = [
        AutocompletePanel('faculty', target_model='mechweb.FacultyPage'),
        FieldPanel('introduction'),
        FieldPanel('session'),
    ]


class CourseAnnouncementPage(Orderable):
    page = ParentalKey(CoursePage, on_delete=models.CASCADE, related_name='course_announcements')
    announcement = RichTextField(max_length=250, blank=True, features=CUSTOM_RICHTEXT)
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        FieldPanel('announcement'),
        DocumentChooserPanel('document'),
    ]


class FeaturedCourse(Orderable):
    page = ParentalKey(CourseStructure, on_delete=models.CASCADE, related_name='featured_courses')
    featured_course = models.ForeignKey('CoursePage', null=True, blank=True, on_delete=models.SET_NULL,
                                        related_name='featured_course')
    panels = [
        AutocompletePanel('featured_course', target_model='mechweb.CoursePage'),
    ]


# def get_prog_course(cat):
# 	return CourseProgrammes.objects.all().get(category=cat).courses.all()
# def get_spec_course(cat):
# 	return CourseSpecializations.objects.all().get(category=cat).courses.all()
######################################################
class AwardHomePage(Page):
    intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    parent_page_types = ['MechHomePage']
    subpage_types = ["AwardPage"]
    max_count = 1

    def serve(self, request):
        award_list = AwardPage.objects.all().order_by('-award_time')
        return render(request, self.template,{
            'page': self,
            'award_list':award_list,
        })

    class Meta:
        verbose_name = "Awards Home"


class AwardPage(Page):
    faculty = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL,
                                related_name='award_fac')
    other_recipients = models.CharField(max_length=100, blank=True)
    award_title = models.CharField(max_length=500)
    award_description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    award_type = models.CharField(max_length=2, choices=FACULTY_AWARD_TYPES, default='0')
    award_time = models.CharField(max_length=100, blank=True)
    conferrer = models.CharField(max_length=200)
    conferrer_description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    link = models.URLField(max_length=250, blank=True)
    alt_recipient_text = models.CharField(max_length=1000, blank=True,
                                          help_text="Use this only if you can't add faculty")

    content_panels = Page.content_panels + [
        FieldPanel('award_title'),
        FieldPanel('award_description'),
        FieldPanel('award_type'),
        AutocompletePanel('faculty', target_model='mechweb.FacultyPage'),
        FieldPanel('other_recipients'),
        ImageChooserPanel('image'),
        FieldPanel('award_time'),
        FieldPanel('conferrer'),
        FieldPanel('conferrer_description'),
        FieldPanel('link'),
        FieldPanel('alt_recipient_text'),
    ]


def get_new_awards():
    a = AwardPage.objects.all().order_by('-award_time')
    if len(a) >= 5:
        a = a[0:5]
    return a
#################################################################
class CommitteeHomePage(Page):
    parent_page_types = ['MechHomePage']
    subpage_types = ['CommitteePage']
    max_count = 1


    def serve(self, request):
        com_list = self.get_children().live().order_by('-committeepage__tenure_end', '-committeepage__tenure_start')

        return render(request, self.template, {
            'page': self,
            'com_list': com_list,
        })

    class Meta:
        verbose_name = "Committee Home"

class CommitteePage(Page):
    name = models.CharField(max_length=500)
    about = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
    tenure_start = models.DateField(default=timezone.now)
    tenure_end = models.DateField(default=timezone.now)
    minutes_doc = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('tenure_start'),
        FieldPanel('tenure_end'),
        FieldPanel('about'),
        DocumentChooserPanel('minutes_doc'),
        InlinePanel('links', label="Links", max_num=10),
        InlinePanel('faculty', label="Faculty Member"),
        InlinePanel('com_other', label="Other Members"),
        InlinePanel('students', label="Student Member"),
    ]

    parent_page_types = ['CommitteeHomePage']
    subpage_types = []

    class Meta:
        verbose_name = "Committee"
        verbose_name_plural = "Committees"

class CommitteePageStudent(Orderable):
    page = ParentalKey(CommitteePage, on_delete=models.CASCADE, related_name='students')
    student = models.ForeignKey('StudentPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='student')
    designation = models.CharField(max_length=100, blank=True)
    panels = [
        AutocompletePanel('student', target_model='mechweb.StudentPage'),
        FieldPanel('designation'),
    ]

class CommitteePageFaculty(Orderable):
    page = ParentalKey(CommitteePage, on_delete=models.CASCADE, related_name='faculty')
    faculty = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='faculty')
    designation = models.CharField(max_length=100, blank=True)
    panels = [
        AutocompletePanel('faculty', target_model='mechweb.FacultyPage'),
        FieldPanel('designation'),
    ]

class CommitteePageOtherMmeber(Orderable):
    page = ParentalKey(CommitteePage, on_delete=models.CASCADE, related_name='com_other')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('designation'),
    ]

class CommitteePageLink(Orderable):
    page = ParentalKey(CommitteePage, on_delete=models.CASCADE, related_name='links')
    link = models.URLField(max_length=250)
    link_text = models.CharField(max_length=250)
    panels = [
        FieldPanel('link_text'),
        FieldPanel('link'),
    ]

# ------------------------------------------
#################################################################


# def set_date(year):
# 	return enrolment_year = datetime.strptime('Jan 1 '+year+' 12:00PM', '%b %d %Y %I:%M%p')

# Not working in sending year list to publication
# raises error:
# local variable 'year_list' referenced before assignment django
# def year_list():
# 	year_list = []
# 	year = timezone.now().year
# 	for i in  range(1996, year):
# 		year_list.append(i)
# 	return year_list

 # from mechweb.models import CourseProgrammes, CourseSpecializations, CourseTypes

# class Committees(Page):
# 	dispoc_external = models.CharField(max_length=300, blank=True) 
# 	dupc_external = models.CharField(max_length=300, blank=True) 
# 	dppc_external = models.CharField(max_length=300, blank=True) 

# 	def serve(self, request):
# 		fac_fic = FacultyPage.objects.all().exclude(faculty_in_charge="11").order_by('faculty_in_charge')
# 		fac_dispoc = FacultyPage.objects.all().exclude(disposal_committee="4").order_by('disposal_committee')

# 		fac_dupc = FacultyPage.objects.all().filter(dupc__in=["1", "2"]).order_by('dupc')
# 		stud_dupc = StudentPage.objects.all().filter(dupc__in=["4", "5"]).order_by('dupc')
		
# 		fac_dppc = FacultyPage.objects.all().filter(dppc__in=["1", "2"].order_by('dppc')
# 		stud_dppc = StudentPage.objects.all().filter(dppc__in=["5", "4"].order_by('dppc')
		
		
# 		fac_mesa = FacultyPage.objects.all().filter(mesa="5").order_by('mesa')
# 		stud_mesa = StudentPage.objects.all().exclude(mesa__in=["5", "6"]).order_by('mesa')
		
# 		fac_sae = FacultyPage.objects.all().filter(sae="2").order_by('mesa')
# 		stud_sae = StudentPage.objects.all().filter(sae__in=["1", "0"]).order_by('sae')
		
# 		fac_disco = FacultyPage.objects.all().exclude(disciplinary_committee__in=["3", "4"]).order_by('disciplinary_committee')
# 		stud_disco = StudentPage.objects.all().filter(disciplinary_committee="3").order_by('disciplinary_committee')
# 		return render(request, self.template, {
# 			'page': self,
# 			'student_list': student_list,
# 			'all_research_interests': all_research_interests,
# 			'tag':tag,
# 			'page_no':page_no,
# 			'prog':prog,
# 			fac_fic = 
# 			fac_dispoc = 
# 			fac_dupc = 
# 			stud_dupc = 
# 			fac_dppc = 
# 			stud_dppc = 
# 			fac_mesa = 
# 			stud_mesa = 
# 			fac_sae = 
# 			stud_sae = 
# 			fac_disco = 
# 			stud_disco = 
# 		})

# 	class Meta:
# 		verbose_name = "Awards Home"
