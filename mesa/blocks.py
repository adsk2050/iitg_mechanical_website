from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class AnnouncementCardBlock(blocks.StructBlock):
    info = blocks.TextBlock(required=False,help_text="Add more information about the announcement")
    button_link = blocks.URLBlock(required=False,help_text = "Add the related url")
    button_text = blocks.CharBlock(required=False,help_text = "Add text for the button")
    button_tooltip = blocks.CharBlock(required=False,help_text = "Add text for the tooltip of the button")
    last_updated = blocks.DateTimeBlock(required=True,auto_now=True)
    card_image = ImageChooserBlock(required=True,help_text = "Add image for the announcement card")
    tag = blocks.ChoiceBlock(required=False,choices=[
        ('new', 'New'),
        ('important', 'Important'),
        ('outdated','outdated'),
    ], icon='cup',null=True)
    class Meta:
        template = "streams/announcement_card.html"
        icon = "edit"
        label = "Announcement Card"

class TeamMemberBlock(blocks.StructBlock):
    name = blocks.CharBlock(help_text="Full name of the team member")
    email = blocks.CharBlock(help_text="Email of the team member",required =False)
    por = blocks.CharBlock(help_text="Position of responsibility of the team member")
    linkedin_url = blocks.URLBlock(help_text = "Url of the linkedin profile",required=False)
    facebook_url = blocks.URLBlock(help_text = "Url of the facebook profile",required=False)
    profile_picture = ImageChooserBlock(required=False,help_text = "Profile picture of the team member")
    class Meta:
        template = "streams/team_member.html"
        icon = "user"
        label = "Team Member"
