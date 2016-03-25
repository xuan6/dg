from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from tastypie.api import Api
from qacoco.api import QaReviewerResource, VideoResource, BlockResource, VillageResource, MediatorResource, PersonResource, PersonGroupResource, VideoContentApprovalResource, VideoQualityReviewResource, DisseminationQualityResource, AdoptionVerificationResource
from views import qacoco_v1, debug, login, logout, record_full_download_time, reset_database_check

qa_api = Api(api_name = "v1")
qa_api.register(QaReviewerResource())
qa_api.register(VideoResource())
qa_api.register(VillageResource())
qa_api.register(BlockResource())
qa_api.register(PersonGroupResource())
qa_api.register(MediatorResource())
qa_api.register(PersonResource())
qa_api.register(VideoContentApprovalResource())
qa_api.register(VideoQualityReviewResource())
qa_api.register(DisseminationQualityResource())
qa_api.register(AdoptionVerificationResource())

urlpatterns = patterns('',
	(r'^api/', include(qa_api.urls)),
	(r'^$', qacoco_v1),
	(r'^login/', login),
    (r'^logout/', logout),
    (r'^record_full_download_time/', record_full_download_time),
    (r'^reset_database_check/', reset_database_check),
	)