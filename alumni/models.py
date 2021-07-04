import datetime
import mechweb
import pytz

from django.core import paginator
from django.db import models
from django.db.models.fields import Field
from django.core.paginator import Paginator

from wagtail.core.models import Page, Orderable, get_default_page_content_type
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey
from django.utils import timezone
from mechweb.constants import *
import mechweb.models as mech

from .helpers import checkInt


class AlumniHome(Page):
    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]
    parent_page_types = ["mechweb.MechHomePage"]
    subpage_types = [
        "AlumniEventsHomePage",
    ]
    max_count = 1

    class Meta:
        verbose_name = "Alumni Home Page"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        events_count = AlumniEventPage.objects.count()
        context["events"] = AlumniEventPage.objects.live().order_by("-start_at", "-end_by")[: min(events_count, 10)]
        context["events_home_page"] = AlumniEventsHomePage.objects.first()
        program_id = request.GET.get("prog")
        batch_id = request.GET.get("batch")
        students = node_children = program = batch = siblings = node_child_type = node_parents = node_parent_type = node_parent_id = node_child_id = None
        if batch_id != None:
            try:
                batch = mech.StudentBatch.objects.get(id=batch_id)
                if batch.alumni_batch == False:
                    batch = None
            except:
                batch = None
                batch_id = None
            if batch:
                students = batch.get_children_order_by_title()
                program = batch.get_program()
                siblings = batch.get_parent().specific.alumni_batches
        elif program_id != None:
            try:
                program = mech.Program.objects.get(id=program_id)
            except:
                try:
                    program = mech.ProgramSpecialization.objects.get(id=program_id)
                except:
                    program = None
                    program_id = None
            if program:
                studentsPage = mech.Students.objects.child_of(program).first()
                siblings = program.get_siblings_with_alumni_details()
                if studentsPage:
                    node_children = studentsPage.alumni_batches
                    node_child_type = "batch"
                    students = studentsPage.get_children().type(mech.Student).order_by("title")

        if program and (batch_id or program.specific_class != mech.Program):
            program_parent = program
            if not batch_id:
                program_parent = program.get_parent()
            node_parent_id = program_parent.id
            parent_class = program_parent.specific_class
            if parent_class == mech.Program:
                node_parents = mech.Program.objects.sibling_of(program_parent).filter(has_alumni_details=True)
                node_parent_type = "prog"
            elif parent_class == mech.ProgramSpecialization:
                node_parents = mech.ProgramSpecialization.objects.sibling_of(program_parent).filter(has_alumni_details=True)
                node_parent_type = "prog_spc"

        if program and not node_children:
            node_children = program.specific.get_specializations()
            node_child_type = "prog"
        if node_child_type == "batch" and len(node_children):
            students = node_children[0].get_children().type(mech.Student).order_by("title")
            node_child_id = node_children[0].id
        if students:
            paginator = Paginator(students, 15)
            page = request.GET.get("page")
            offset = (int(page) - 1) * 15 if (page and checkInt(page)) else 0
            alumni_list = paginator.get_page(page)
            context["alumni_list"] = alumni_list
            context["offset"] = offset
        context["program"] = program
        context["node_parents"] = node_parents
        context["node_parent_id"] = node_parent_id
        context["node_parent_type"] = node_parent_type
        context["siblings"] = siblings
        context["node_children"] = node_children
        context["node_child_id"] = node_child_id
        if program_id:
            context["program_id"] = int(program_id)
        if batch_id:
            context["batch_id"] = int(batch_id)
        context["node_child_type"] = node_child_type
        if not program:
            context["programs"] = mech.Program.objects.all().filter(has_alumni_details=True)
        url = self.url + "?"
        if program_id:
            url += "prog=" + program_id
        if batch_id:
            url += "batch=" + batch_id
        context["url"] = url

        return context


class AlumniEventsHomePage(Page):

    content_panels = Page.content_panels + []
    parent_page_types = ["AlumniHome"]
    subpage_types = [
        "AlumniEventPage",
    ]
    max_count = 1

    class Meta:
        verbose_name = "Alumni Events Home Page"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        events = AlumniEventPage.objects.live().order_by("-start_at", "-end_by")
        paginator = Paginator(events, 9)
        page = request.GET.get("page")
        events = paginator.get_page(page)
        context["events"] = events
        return context


class AlumniEventPage(Page):
    description = models.TextField(blank=True, null=True)
    start_at = models.DateTimeField(default=timezone.now)
    end_by = models.DateTimeField(blank=True, null=True)
    venue = models.CharField(blank=True, max_length=50, choices=LOCATIONS, default="3")
    poster = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    event_type = models.CharField(max_length=50, choices=ALUMNI_EVENTS, default="0")
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel("event_speakers", label="Speaker", max_num=4),
            ],
            heading="Speaker",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("start_at"),
                        FieldPanel("end_by"),
                    ]
                ),
                FieldPanel("event_type"),
                FieldPanel("venue"),
                FieldPanel("description"),
                ImageChooserPanel("poster"),
            ],
            heading="Event details",
        ),
        MultiFieldPanel(
            [
                InlinePanel("event_urls", label="Link", max_num=10),
                InlinePanel("event_documents", label="Document", max_num=2),
                InlinePanel("gallery_images", label="Gallery Image", max_num=2),
            ],
            heading="Others",
        ),
    ]

    class Meta:
        verbose_name = "Alumni Event"
        verbose_name_plural = "Alumni Event Plural"

    parent_page_types = ["AlumniEventsHomePage"]
    subpage_types = []

    def is_past_due(self):
        if self.start_at == None:
            return True
        now = datetime.datetime.now().astimezone(self.start_at.tzinfo)
        return now > self.start_at


class EventPageGalleryImage(Orderable):
    page = ParentalKey(AlumniEventPage, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ForeignKey("wagtailimages.Image", on_delete=models.CASCADE, related_name="+")
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        ImageChooserPanel("image"),
                        FieldPanel("caption"),
                    ]
                ),
            ],
            heading="Event gallery",
        )
    ]


class EventPageDocument(Orderable):
    page = ParentalKey(AlumniEventPage, on_delete=models.CASCADE, related_name="event_documents")
    document = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    title = models.CharField(max_length=40, blank=False, null=True)
    panels = [
        FieldRowPanel(
            [
                FieldPanel("title"),
                DocumentChooserPanel("document"),
            ]
        )
    ]


class EventPageUrl(Orderable):
    page = ParentalKey(AlumniEventPage, on_delete=models.CASCADE, related_name="event_urls")
    title = models.CharField(max_length=264, blank=False)
    url = models.URLField(blank=False, max_length=2083)
    panels = [FieldRowPanel([FieldPanel("title"), FieldPanel("url")])]


class EventSpeaker(Orderable):
    page = ParentalKey(AlumniEventPage, on_delete=models.CASCADE, related_name="event_speakers")
    name = models.CharField(blank=True, verbose_name="Full Name", max_length=264)
    about = models.CharField(
        blank=True,
        verbose_name="About",
        help_text="batch and current affiliation/designation",
        max_length=264,
    )
    bio = models.TextField(blank=True, verbose_name="Bio-sketch")
    photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="profile picture",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("about"),
                FieldPanel("bio"),
                ImageChooserPanel("photo"),
            ],
            heading="Speaker",
        )
    ]
