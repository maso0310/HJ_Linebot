from django.contrib import admin

# Register your models here.
from HJ_LineBot.models import *

class usersAdmin(admin.ModelAdmin):
    list_display = ('p_name','p_picture','souce_type','gid','uid','mid','mtext','rtk','mdt')
admin.site.register(user_message,usersAdmin)

class PostbackAdmin(admin.ModelAdmin):
    list_display = ('uid','mdt','mPostBack')
admin.site.register(postback_record,PostbackAdmin)

class eventAdmin(admin.ModelAdmin):
    list_display = ('uid','mdt','event_type','message_type')
admin.site.register(event_happening,eventAdmin)

class FarmerAdmin(admin.ModelAdmin):
    list_display = ('uid','mdt','name','crop','area','birth','email','phone','addr')
admin.site.register(Farmer_member,FarmerAdmin)

class PilotAdmin(admin.ModelAdmin):
    list_display = ('uid','mdt','exp','drone','name','birth','email','phone','addr')
admin.site.register(Drone_Piloter,PilotAdmin)

class Farmer_Order_completedAdmin(admin.ModelAdmin):
    list_display = ('uid','mdt','order_number','name','phone','mission_date','mission_crop','mission_area','mission_item','mission_addr','mission_latitude','mission_longitude')
admin.site.register(Farmer_Order_completed,Farmer_Order_completedAdmin)

class Farmer_Order_TempAdmin(admin.ModelAdmin):
    list_display = ('uid','mdt','order_number','mission_date','mission_crop','mission_area','mission_item')
admin.site.register(Farmer_Order_Temp,Farmer_Order_TempAdmin)
