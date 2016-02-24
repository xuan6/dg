from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from tastypie.api import Api
from qacoco.api import QaReviewerResource, VideoResource, VideoContentApprovalResource

qa_api = Api(api_name = "v1")
qa_api.register(QaReviewerResource())
qa_api.register(VideoResource())
qa_api.register(VideoContentApprovalResource())

urlpatterns = patterns('',
	(r'^api/', include(qa_api.urls)),
	)