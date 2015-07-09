from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from tastypie.api import Api

from api import DistrictResource, LanguageResource, MediatorResource, NonNegotiableResource, PartnerResource, PersonAdoptVideoResource, PersonGroupResource, PersonResource, ScreeningResource, VideoResource, VillageResource
from api_mcoco import DistrictResource as mDistrictResource, LanguageResource as mLanguageResource, MediatorResource as mMediatorResource, NonNegotiableResource as mNonNegotiableResource, PartnerResource as mPartnerResource, PersonAdoptVideoResource as mPersonAdoptVideoResource, PersonGroupResource as mPersonGroupResource, PersonResource as mPersonResource, ScreeningResource as mScreeningResource, VideoResource as mVideoResource, VillageResource as mVillageResource
from views import coco_v2, debug, login, logout, record_full_download_time, reset_database_check, mlogin

v1_api = Api(api_name='v2')
v1_coco_api = Api(api_name='v3')

v1_api.register(DistrictResource())
v1_api.register(LanguageResource())
v1_api.register(PartnerResource())
v1_api.register(VillageResource())

v1_api.register(MediatorResource())
v1_api.register(PersonAdoptVideoResource())
v1_api.register(PersonResource())
v1_api.register(PersonGroupResource())
v1_api.register(ScreeningResource())
v1_api.register(VideoResource())
v1_api.register(NonNegotiableResource())


v1_coco_api.register(mDistrictResource())
v1_coco_api.register(mLanguageResource())
v1_coco_api.register(mPartnerResource())
v1_coco_api.register(mVillageResource())

v1_coco_api.register(mMediatorResource())
v1_coco_api.register(mPersonAdoptVideoResource())
v1_coco_api.register(mPersonResource())
v1_coco_api.register(mPersonGroupResource())
v1_coco_api.register(mScreeningResource())
v1_coco_api.register(mVideoResource())
v1_coco_api.register(mNonNegotiableResource())


urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    (r'^mcocoapi/',include(v1_coco_api.urls)),
    (r'^login/', login),
    (r'^mlogin/', mlogin),
    (r'^logout/', logout),
    (r'^debug/', debug),
    (r'^$', coco_v2),
    url(r'^faq/$', TemplateView.as_view(template_name='faq.html'), name="faq"),
    (r'^record_full_download_time/', record_full_download_time),
    (r'^reset_database_check/', reset_database_check),
)
