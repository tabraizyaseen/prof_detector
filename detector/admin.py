from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(Upload)
class imagesAdmin(admin.ModelAdmin):

	def image_tag(self, obj):
		return format_html('<img src="{}" style="max-width: 250px; max-height: 250px;"/>'.format(obj.image.url))

	image_tag.short_description = 'Image'

	list_display = ['id','image_tag']
	empty_value_display = '-empty-'
	search_fields = ('id','image')

# Admin Customization
admin.site.site_header = "Profession Detection Administration"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to Admin Panel"

# Removing Group Model
admin.site.unregister(Group)