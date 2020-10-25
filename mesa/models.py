from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import fields
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *

class MesaHomePage(Page):
    about = models.TextField(null=True,blank = True)
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    max_count=1
    our_aim = models.TextField(null=True,blank = True)
    our_aim_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    scrolling_text = models.TextField(null=True,blank = True)
    gallery_images = StreamField(
        [
            ("GalleryImages",ImageChooserBlock())
        ],
        null = True,
        blank = True,
    )
    announcement_cards = StreamField(
        [
            ("announcement_card",AnnouncementCardBlock() )
        ],
        null=True,
        blank = True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("about"),
        ImageChooserPanel('about_image'),
        FieldPanel("our_aim"),
        ImageChooserPanel('our_aim_image'),
        FieldPanel("scrolling_text"),
        StreamFieldPanel("gallery_images"),
        StreamFieldPanel("announcement_cards"),

    ]
    # class Meta:
        # verbose_name = "Mesa"

class Team(Page):
    max_count = 1
    team_bg_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    team_members = StreamField(
        [
            ("team_members",TeamMemberBlock()),

        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel('team_bg_image'),
        StreamFieldPanel("team_members")
    ]
