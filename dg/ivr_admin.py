from django.contrib.admin.sites import AdminSite

from ivr.models import Call, Broadcast, Audio, UsaidData
from ivr.admin import CallAdmin, BroadcastAdmin, AudioAdmin, UsaidAdmin

class IvrAdmin(AdminSite):
    pass

ivr_admin = IvrAdmin(name="ivrsadmin")

ivr_admin.register(Call, CallAdmin)
ivr_admin.register(Broadcast, BroadcastAdmin)
ivr_admin.register(Audio, AudioAdmin)
ivr_admin.register(UsaidData, UsaidAdmin)
