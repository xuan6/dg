from tastypie.resources import ModelResource
from videos.models import VideoContentApproval,Video,VideoQualityReview
from tastypie.authentication import SessionAuthentication, Authentication
from tastypie.authorization import Authorization
from tastypie import fields
from functools import partial
from django.forms.models import model_to_dict
from coco.models import CocoUser
from people.models import QaReviewer,Animator
from geographies.models import Block,Village
from activities.models import DisseminationQuality
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

class BlockResource(BaseResource):
    class Meta:
                max_limit = None
                queryset = Block.objects.all()
                resource_name = 'block'
                authentication = Authentication()
                authorization = Authorization()

class VillageResource(BaseResource):
    class Meta:
                max_limit = None
                queryset = Village.objects.all()
                resource_name = 'village'
                authentication = Authentication()
                authorization = Authorization()

class MediatorResource(BaseResource):
    class Meta:
                max_limit = None
                queryset = Animator.objects.all()
                resource_name = 'mediator'
                authentication = Authentication()
                authorization = Authorization()





class VideoContentApprovalResource(BaseResource):
        video = fields.ForeignKey(VideoResource, 'video')
        reviewed_by = fields.ForeignKey(QaReviewerResource, 'reviewer')
        class Meta:
                queryset = VideoContentApproval.objects.all()
                resource_name = 'VideoContentApproval'
                authorization = Authorization()
                authentication = Authentication()
        dehydrate_video = partial(foreign_key_to_id, field_name = 'video', sub_field_names=['id','title'])
        hydrate_video = partial(dict_to_foreign_uri, field_name ='video')
        dehydrate_reviewer = partial(foreign_key_to_id, field_name = 'reviewer', sub_field_names=['id','partner_name'])
        hydrate_reviewer = partial(dict_to_foreign_uri, field_name ='reviewer')

class VideoQualityReviewResource(BaseResource):
        video = fields.ForeignKey(VideoResource, 'video')
        reviewed_by = fields.ForeignKey(QaReviewerResource, 'reviewer')
        class Meta:
                queryset = VideoQualityReview.objects.all()
                resource_name = 'VideoQualityReview'
                authorization = Authorization()
                authentication = Authentication()
        dehydrate_video = partial(foreign_key_to_id, field_name = 'video', sub_field_names=['id','title'])
        hydrate_video = partial(dict_to_foreign_uri, field_name ='video')
        dehydrate_reviewer = partial(foreign_key_to_id, field_name = 'reviewer', sub_field_names=['id','partner_name'])
        hydrate_reviewer = partial(dict_to_foreign_uri, field_name ='reviewer')

class DisseminationQualityResource(BaseResource):
        block = fields.ForeignKey(BlockResource, 'block')
        village = fields.ForeignKey(VillageResource, 'village')
        mediator = fields.ForeignKey(MediatorResource, 'mediator')
        video = fields.ForeignKey(VideoResource, 'video')
        reviewed_by = fields.ForeignKey(QaReviewerResource, 'reviewer')
        class Meta:
                queryset = VideoQualityReview.objects.all()
                resource_name = 'VideoQualityReview'
                authorization = Authorization()
                authentication = Authentication()
        dehydrate_video = partial(foreign_key_to_id, field_name = 'video', sub_field_names=['id','title'])
        hydrate_video = partial(dict_to_foreign_uri, field_name ='video')
        dehydrate_reviewer = partial(foreign_key_to_id, field_name = 'reviewer', sub_field_names=['id','partner_name'])
        hydrate_reviewer = partial(dict_to_foreign_uri, field_name ='reviewer')


def get_partner_videos(user_id):
    ###Videos produced by partner with in the same state
    coco_user = CocoUser.objects.get(user_id = user_id)
    villages = coco_user.get_videos()
    user_states = State.objects.filter(district__block__village__in = villages).distinct().values_list('id', flat=True)
    user_videos = coco_user.get_videos().values_list('id', flat = True)
    ###FIRST GET VIDEOS PRODUCED IN STATE WITH SAME PARTNER
    videos = Video.objects.filter(village__block__district__state__in = user_states, partner_id = coco_user.partner_id).values_list('id', flat = True)
    ###Get videos screened to allow inter partner sharing of videos
    videos_seen = set(Person.objects.filter(village__in = villages, partner_id = coco_user.partner_id).values_list('screening__videoes_screened', flat=True))
    return set(list(videos) + list(videos_seen) + list(user_videos))

class VideoAuthorization(Authorization):
    def read_list(self, object_list, bundle):        
        return object_list.filter(id__in= get_partner_videos(bundle.request.user.id))
    
    def read_detail(self, object_list, bundle):
        if bundle.obj.id in get_partner_videos(bundle.request.user.id):
            return True
        else:
            raise NotFound( "Not allowed to download video")