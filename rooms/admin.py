from django.contrib import admin
from .import models

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """
    list_display = ("name","used_by")

    def used_by(self, obj):
        return obj.rooms.count()

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
         (
             "Basic Info",
             {"fields":("name","description","country","address","price")}
         ),
         (
             "Times",
             {"fields":("check_in","check_out","instant_book")}
         ),
         (
             "Spaces",
             {"fields":("guests","beds","bedrooms","baths")}
         ),
         (
             "More About Space",
             {
                 "classes":("collapse",),
                 "fields":("amenities","facilities","house_rule"),
             }
         ),         
         (
             "Last Details",
             {"fields":("host",)}
         ),
    )

    list_display = (
        "name" ,
        "beds",
        "price",
        "address",
        "guests",
        "city",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name","price","bedrooms")

    list_filter = ("instant_book",
                   "host__superhost",
                   "room_type",                    
                   "amenities",
                   "facilities",
                   "house_rule",
                   "city",
                   "country",
                  )

    search_fields = ("=city","^host__username")

    filter_horizontal = ("amenities","facilities","house_rule",)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()        



@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass    