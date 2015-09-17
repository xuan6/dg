from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from tastypie.api import Api
from training.api import TrainerResource, LanguageResource, AssessmentResource, QuestionResource, MediatorResource, DistrictResource, VillageResource, PartnerResource
from views import login

api = Api(api_name = "v1")
api.register(TrainerResource())
api.register(LanguageResource())
api.register(AssessmentResource())
api.register(QuestionResource())
api.register(MediatorResource())
api.register(DistrictResource())
api.register(VillageResource())
api.register(PartnerResource())

urlpatterns = patterns('',
	(r'^login/', login),
	(r'^api/', include(api.urls)),
	)
