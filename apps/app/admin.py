from django.contrib import admin

from apps.app.models.category import Category
from apps.app.models.item import Item
from apps.app.models.menu import Menu
from apps.app.models.restaurant import Restaurant
from apps.app.models.section import Section
from apps.app.models.variation import Variation

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Restaurant)
admin.site.register(Section)
admin.site.register(Variation)
