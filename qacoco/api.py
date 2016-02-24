from tastypie.resources import ModelResource
from videos.models import VideoContentApproval,Video
from tastypie.authentication import SessionAuthentication, Authentication
from tastypie.authorization import Authorization
from tastypie import fields
from functools import partial
from django.forms.models import model_to_dict
#from coco.models import CocoUser
from people.models import QaReviewer
from coco.api import BaseResource

def foreign_key_to_id(bundle, field_name,sub_field_names):
    field = getattr(bundle.obj, field_name)
    if(field == None):
        dict = {}
        for sub_field in sub_field_names:
            dict[sub_field] = None 
    else:
        dict = model_to_dict(field, fields=sub_field_names, exclude=[])
    return dict

def dict_to_foreign_uri(bundle, field_name, resource_name=None):
    field_dict = bundle.data.get(field_name)
    if field_dict.get('id'):
        bundle.data[field_name] = "/qa/api/v1/%s/%s/"%(resource_name if resource_name else field_name, 
                                                    str(field_dict.get('id')))
    else:
        bundle.data[field_name] = None
    return bundle

class QaReviewerResource(BaseResource):
	class Meta:
                max_limit = None
                queryset = QaReviewer.objects.all()
                resource_name = 'reviewer'
                authentication = Authentication()
                authorization = Authorization()

class VideoResource(BaseResource):
	class Meta:
                max_limit = None
                queryset = Video.objects.all()
                resource_name = 'video'
                authentication = Authentication()
                authorization = Authorization()



class VideoContentApprovalResource(BaseResource):
        video = fields.ForeignKey(VideoResource, 'video')
        reviewer = fields.ForeignKey(QaReviewerResource, 'reviewer')
        class Meta:
                queryset = VideoContentApproval.objects.all()
                resource_name = 'VideoContentApproval'
                authorization = Authorization()
                authentication = Authentication()
        dehydrate_video = partial(foreign_key_to_id, field_name = 'video', sub_field_names=['id','title'])
        hydrate_video = partial(dict_to_foreign_uri, field_name ='video')
        dehydrate_reviewer = partial(foreign_key_to_id, field_name = 'reviewer', sub_field_names=['id','partner_name'])
        hydrate_reviewer = partial(dict_to_foreign_uri, field_name ='reviewer')