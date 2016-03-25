from tastypie.resources import ModelResource
from videos.models import VideoContentApproval,Video,VideoQualityReview
from tastypie.authentication import SessionAuthentication, Authentication
from tastypie.authorization import Authorization
from tastypie import fields
from functools import partial
from django.forms.models import model_to_dict
from coco.models import CocoUser
from people.models import QaReviewer,Animator,Person,PersonGroup
from geographies.models import Block,Village
from activities.models import DisseminationQuality,AdoptionVerification
from qacoco.models import QaCocoUser


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

class VillageAuthorization(Authorization):
    def __init__(self, field):
        self.village_field = field
    
    def read_list(self, object_list, bundle):
        villages = QaCocoUser.objects.get(user_id= bundle.request.user.id).get_villages()
        kwargs = {}
        kwargs[self.village_field] = villages
        return object_list.filter(**kwargs).distinct()

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        kwargs = {}
        kwargs[self.village_field] = QaCocoUser.objects.get(user_id= bundle.request.user.id).get_villages()
        obj = object_list.filter(**kwargs).distinct()
        if obj:
            return True
        else:
            raise NotFound( "Not allowed to download Village" )


class BaseResource(ModelResource):
    
    def full_hydrate(self, bundle):
        bundle = super(BaseResource, self).full_hydrate(bundle)
        bundle.obj.user_modified_id = bundle.request.user.id
        return bundle
    
    def obj_create(self, bundle, **kwargs):
        """
        A ORM-specific implementation of ``obj_create``.
        """
        bundle.obj = self._meta.object_class()

        for key, value in kwargs.items():
            setattr(bundle.obj, key, value)

        self.authorized_create_detail(self.get_object_list(bundle.request), bundle)
        bundle = self.full_hydrate(bundle)
        bundle.obj.user_created_id = bundle.request.user.id
        return self.save(bundle)

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
                authorization = VillageAuthorization('id__in')

class MediatorResource(BaseResource):
    class Meta:
                max_limit = None
                queryset = Animator.objects.all()
                resource_name = 'mediator'
                authentication = Authentication()
                authorization = Authorization()

class PersonResource(BaseResource):
    class Meta:
                max_limit = None
                queryset = Person.objects.all()
                resource_name = 'person'
                authentication = Authentication()
                authorization = Authorization()

class PersonGroupResource(BaseResource):
    class Meta:
                max_limit = None
                queryset = PersonGroup.objects.all()
                resource_name = 'group'
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
        dehydrate_reviewer = partial(foreign_key_to_id, field_name = 'reviewer', sub_field_names=['id','name'])
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
        dehydrate_reviewer = partial(foreign_key_to_id, field_name = 'reviewer', sub_field_names=['id','name'])
        hydrate_reviewer = partial(dict_to_foreign_uri, field_name ='reviewer')

class DisseminationQualityResource(BaseResource):
        block = fields.ForeignKey(BlockResource, 'block')
        village = fields.ForeignKey(VillageResource, 'village')
        mediator = fields.ForeignKey(MediatorResource, 'mediator')
        video = fields.ForeignKey(VideoResource, 'video')
        reviewed_by = fields.ForeignKey(QaReviewerResource, 'reviewer')
        class Meta:
                queryset = DisseminationQuality.objects.all()
                resource_name = 'DisseminationQuality'
                authorization = Authorization()
                authentication = Authentication()
        dehydrate_video = partial(foreign_key_to_id, field_name = 'video', sub_field_names=['id','title'])
        hydrate_video = partial(dict_to_foreign_uri, field_name ='video')
        dehydrate_reviewer = partial(foreign_key_to_id, field_name = 'reviewer', sub_field_names=['id','partner_name'])
        hydrate_reviewer = partial(dict_to_foreign_uri, field_name ='reviewer')
        dehydrate_block = partial(foreign_key_to_id, field_name = 'block', sub_field_names=['id','block_name'])
        hydrate_block = partial(dict_to_foreign_uri, field_name ='block')
        dehydrate_village = partial(foreign_key_to_id, field_name = 'village', sub_field_names=['id','village_name'])
        hydrate_village = partial(dict_to_foreign_uri, field_name ='village')
        dehydrate_mediator = partial(foreign_key_to_id, field_name = 'mediator', sub_field_names=['id','name'])
        hydrate_mediator = partial(dict_to_foreign_uri, field_name ='mediator')


class AdoptionVerificationResource(BaseResource):
        block = fields.ForeignKey(BlockResource, 'block')
        village = fields.ForeignKey(VillageResource, 'village')
        mediator = fields.ForeignKey(MediatorResource, 'mediator')
        video = fields.ForeignKey(VideoResource, 'video')
        reviewed_by = fields.ForeignKey(QaReviewerResource, 'reviewer')
        person = fields.ForeignKey(PersonResource, 'person')
        group = fields.ForeignKey(PersonGroupResource, 'group')
        class Meta:
                queryset = AdoptionVerification.objects.all()
                resource_name = 'AdoptionVerification'
                authorization = Authorization()
                authentication = Authentication()
        dehydrate_video = partial(foreign_key_to_id, field_name = 'video', sub_field_names=['id','title'])
        hydrate_video = partial(dict_to_foreign_uri, field_name ='video')
        dehydrate_reviewer = partial(foreign_key_to_id, field_name = 'reviewer', sub_field_names=['id','partner_name'])
        hydrate_reviewer = partial(dict_to_foreign_uri, field_name ='reviewer')
        dehydrate_block = partial(foreign_key_to_id, field_name = 'block', sub_field_names=['id','block_name'])
        hydrate_block = partial(dict_to_foreign_uri, field_name ='block')
        dehydrate_village = partial(foreign_key_to_id, field_name = 'village', sub_field_names=['id','village_name'])
        hydrate_village = partial(dict_to_foreign_uri, field_name ='village')
        dehydrate_mediator = partial(foreign_key_to_id, field_name = 'mediator', sub_field_names=['id','name'])
        hydrate_mediator = partial(dict_to_foreign_uri, field_name ='mediator')
        dehydrate_group = partial(foreign_key_to_id, field_name = 'group', sub_field_names=['id','group_name'])
        hydrate_group = partial(dict_to_foreign_uri, field_name ='group')



