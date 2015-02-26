import ast
import datetime
import json
import random
import urllib2

from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import login as django_login_view
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from dg.settings import PERMISSION_DENIED_URL, MEDIA_ROOT

from elastic_search import get_related_collections, get_related_videos
from geographies.models import State
from programs.models import Partner as COCO_Partner
from social_website.models import  Collection, Partner, FeaturedCollection, Video, VideoChunk, VideoFile
from social_website.utils.combine_upload import combine
from videos.models import Practice, Language, Video as Dashboard_Video


from mezzanine.blog.models import BlogPost

class CustomUserCreationForm(UserCreationForm):
    username = forms.EmailField(label=("Username"), help_text=("Enter Email Address"))


def social_home(request):
    language = Collection.objects.exclude(language=None).values_list('language', flat=True) # only using those languages that have collections 
    language = sorted(set(language))
    blog = BlogPost.objects.all()[:3]
    context= {
        'header': {
            'jsController':'Home',
            'currentPage':'Home',
            'loggedIn':False,
            'random':random.randint(0, 1),
             },
        'language':language,
        'blog_posts':blog,
                }
    return render_to_response('home.html', context, context_instance = RequestContext(request))

def collection_view(request, partner, state, language, title, video=1):
    try:
        collection = Collection.objects.get(partner__name__iexact=partner, state__iexact=state, language__iexact=language, title__iexact=title)
    except Collection.DoesNotExist:
        return HttpResponseRedirect(reverse('discover'))
    try:
        video_index = int(video)
    except (IndexError, AssertionError):
        video_index = 1
    finally:
        video = collection.videoincollection_set.all()[video_index - 1].video
    tags = [x for x in [video.category, video.subcategory, video.topic, video.subtopic, video.subject] if x is not u'']
    duration = sum([v.duration for v in collection.videos.all()])
    related_collections = get_related_collections(collection)
    video_list = [i.video for i in collection.videoincollection_set.all()]
    context = {
              'header': {
                         'jsController': 'ViewCollections',
                         'currentPage': 'Discover',
                         'loggedIn': False
                         },
              'is_collection': True,
              'object': collection,
              'video_list': video_list,
              'collection_duration': duration,
              'video': video,
              'video_index': video_index,
              'tags': tags,
              'related_collections': related_collections[:4],  # restricting to 4 related collections for now
              }
    return render_to_response('collections-view.html', context, context_instance=RequestContext(request)) 


def video_view(request, uid):
    try:
        video = Video.objects.get(uid=uid)
    except Video.DoesNotExist:
        return HttpResponseRedirect(reverse('discover'))

    tags = [x for x in [video.category, video.subcategory, video.topic, video.subtopic, video.subject] if x is not u'']
    if Collection.objects.filter(partner=video.partner).count():
        collection = Collection.objects.filter(partner=video.partner)[0]
    else:
        collection = Collection.objects.all()[0]
    related_collections = get_related_collections(collection)
    related_videos = get_related_videos(video)
    context = {
               'header': {
                          'jsController': 'ViewCollections',
                          'currentPage': 'Discover',
                          },
              'is_collection': False,
              'object': video,
              'video_list': related_videos,
              'video': video,
              'video_index': 1,
              'tags': tags,
              'related_collections': related_collections[:4],   # restricting to 4 related collections for now
               }
    return render_to_response('collections-view.html', context, context_instance=RequestContext(request))


def partner_view(request, partner):
    try:
        partner = Partner.objects.get(name__iexact=partner)
    except Partner.DoesNotExist:
        return HttpResponseRedirect(reverse('connect'))
    context = {
        'header': {
            'jsController': 'Profile',
            'loggedIn': False,
            'currentPage': 'Connect',
            },
        'partner': partner,
        }
    return render_to_response('profile.html', context, context_instance=RequestContext(request))


def search_view(request):
    searchString = request.GET.get('searchString', None)
    partner = request.GET.get('partner', None)
    title = request.GET.get('title', None)
    state = request.GET.get('state', None)
    language = request.GET.get('language', None)
    category = request.GET.get('category', None)
    subcategory = request.GET.get('subcategory', None)
    topic = request.GET.get('topic', None)
    subject = request.GET.get('subject', None)
    context= {
              'header': {
                         'jsController': 'Collections',
                         'currentPage': 'Discover',
                         'loggedIn': False
                         },
              'searchString' : searchString,
              'partner' : partner,
              'title' : title,
              'state' : state,
              'language' : language,
              'category' : category,
              'subcategory' : subcategory,
              'topic' : topic,
              'subject': subject,
        }
    return render_to_response('collections.html', context, context_instance=RequestContext(request))


def make_sub_filter(filters, field, active_filter_list, facet_dict):
    kwargs = {}
    kwargs[field] = ''
    filters[field] = {}
    filters[field]['title'] = field.title()
    filters[field]['options'] = []
    for obj in sorted(set(Collection.objects.exclude(**kwargs).values_list(field, flat=True))): #works same as .exclude(field = '')
        facet_count = facet_dict[obj] if facet_dict.has_key(obj) else 0
        if facet_count or facet_dict == {}:
            filters[field]['options'].append({"title": obj, "value": obj, "filterActive": obj in active_filter_list, "count": facet_count})
    return filters


@csrf_exempt
def searchFilters(request):
    if request.method == 'GET':
        params = request.GET
        facets = params.get('facets', None)
    else:
        params = request.POST
        facets_json = json.loads(request.body)
        facets = facets_json['facets']
    facet_dict = {}
    if facets:
        facet_dict = {}
        facets = ast.literal_eval(facets)
        for row in facets:
            facet_dict[row['term']] = int(row['count'])

    language = params.getlist('filters[language][]', None)
    subcategory = params.getlist('filters[subcategory][]', None)
    category = params.getlist('filters[category][]', None)
    partner = params.getlist('filters[partner][]', None)
    state = params.getlist('filters[state][]', None)
    topic = params.getlist('filters[topic][]', None)
    subject = params.getlist('filters[subject][]', None)

    filters = {}
    filters['partner'] = {}
    filters['partner']['title'] = 'Partner'
    filters['partner']['options'] = []
    for obj in Partner.objects.all().order_by('name'):
        facet_count = facet_dict[obj.name] if facet_dict.has_key(obj.name) else 0
        if facet_count or facet_dict == {}:
            filters['partner']['options'].append({"title": obj.name, "value": obj.name, "filterActive" : obj.name in partner, "count" : facet_count })

    filters = make_sub_filter(filters, 'category', category, facet_dict)
    filters = make_sub_filter(filters, 'subcategory', subcategory, facet_dict)
    filters = make_sub_filter(filters, 'topic', topic, facet_dict)
    filters = make_sub_filter(filters, 'state', state, facet_dict)
    filters = make_sub_filter(filters, 'subject', subject, facet_dict)
    filters = make_sub_filter(filters, 'language', language, facet_dict)

    data = json.dumps({"categories": filters})
    return HttpResponse(data)


def featuredCollection(request):
    language_name = request.GET.get('language__name', None)
    featured_collections = FeaturedCollection.objects.filter(collection__language=language_name, show_on_language_selection=True).order_by('-uid')
    if len(featured_collections) == 0:
        featured_collections = FeaturedCollection.objects.filter(collection__language=language_name).order_by('-uid')
        if len(featured_collections) == 0:
            # This code should be triggered on
            # homepage without language selection
            # language sent is all_languages or None
            # there is no featured collection with the chosen language
            featured_collections = FeaturedCollection.objects.filter(show_on_homepage = True).order_by('-uid')
            if len(featured_collections) == 0:
                featured_collections = FeaturedCollection.objects.all().order_by('-uid')
    featured_collection = featured_collections[0]
    collection = featured_collection.collection
    collage_url = featured_collection.collageURL
    time = 0
    for video in collection.videos.all():
        time = time + video.duration
    featured_collection_dict = {
        'title': collection.title,
        'state': collection.state,
        'likes': collection.likes,
        'views': collection.views,
        'adoptions': collection.adoptions,
        'language': collection.language,
        'partner_name': collection.partner.name,
        'partner_logo': collection.partner.logoURL.url,
        'partner_url': collection.partner.get_absolute_url(),
        'video_count': collection.videos.all().count(),
        'link': collection.get_absolute_url(),
        'collageURL': collage_url.url,
        'duration': str(datetime.timedelta(seconds=time)),
    }
    resp = json.dumps({"featured_collection": featured_collection_dict})
    return HttpResponse(resp)


def footer_view(request):
    response = urllib2.urlopen('https://graph.facebook.com/digitalgreenorg')
    data = data = json.loads(response.read())
    footer_dict = {
        'likes': data['likes'],
        }
    context = {
        'header': {
            'jsController': 'Footer',
            'loggedIn': False},
        'footer_dict': footer_dict
        }
    return render_to_response('footer.html', context, context_instance=RequestContext(request))


@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Collection Czars').count() > 0, login_url=PERMISSION_DENIED_URL)
def collection_edit_view(request, collection):
    try:
        collection = Collection.objects.get(uid=collection)
    except Collection.DoesNotExist:
        return HttpResponseRedirect(reverse('create_collection'))
    collection_videos = [i.video_id for i in collection.videoincollection_set.all()]
    video = Video.objects.all()
    language = video.values_list('language',flat=True)
    language = sorted(set(language))
    partner = Partner.objects.values('name', 'uid')
    partner = sorted(partner)
    state = video.values_list('state', flat=True)
    state = sorted(set(state))
    context= {
              'header': {
                         'jsController': 'CollectionAdd',
                         },
              'collection': collection,
              'collection_videos': collection_videos,
              'language': language,
              'partner': partner,
              'state': state,
              }
    return render_to_response('collection_add.html' , context, context_instance = RequestContext(request))


@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Collection Czars').count() > 0, login_url=PERMISSION_DENIED_URL)
def collection_add_view(request):
    video = Video.objects.all()
    language = video.values_list('language',flat=True)
    language = sorted(set(language))
    partner = Partner.objects.values('name', 'uid')
    partner = sorted(partner)
    state = video.values_list('state', flat=True)
    state = sorted(set(state))
    context = {
              'header': {
                         'jsController': 'CollectionAdd',
                         },
              'language': language,
              'partner': partner,
              'state': state,
              }
    return render_to_response('collection_add.html', context, context_instance=RequestContext(request))


@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Collection Czars').count() > 0, login_url=PERMISSION_DENIED_URL)
def video_add_view(request):
    language = Language.objects.values('language_name', 'id')
    language = sorted(language, key=lambda k: k['language_name'])
    partner = COCO_Partner.objects.values('partner_name', 'id')
    partner = sorted(partner, key=lambda k: k['partner_name'])
    state = State.objects.values('state_name', 'id')
    context = {
              'header': {
                         'jsController': 'VideoAdd',
                         },
              'language': language,
              'partner': partner,
              'state': state,
              }
    return render_to_response('video_add.html', context, context_instance=RequestContext(request))


def mapping(request):
    practice_dictionary = {}

    query = Dashboard_Video.objects.values_list('related_practice', flat=True).distinct()
    for a in Practice.objects.select_related('practice_topic', 'practice_subtopic', 'practice_sector', 'practice_subsector', 'practice_subject').filter(id__in=query).order_by('practice_subtopic').order_by('practice_topic').order_by('practice_subsector').order_by('practice_sector'):

        if a.practice_sector.name not in practice_dictionary: #sector will be key
            practice_dictionary[a.practice_sector.name] = {'subject': []}
        sector_dictionary = practice_dictionary[a.practice_sector.name]
        if a.practice_subject:
            subject_list = practice_dictionary[a.practice_sector.name]['subject']
            if a.practice_subject.name not in subject_list:
                subject_list.append(a.practice_subject.name)
        if a.practice_subsector:
            if a.practice_subsector.name not in sector_dictionary:
                sector_dictionary[a.practice_subsector.name] = {}
            subsector_dictionary = sector_dictionary[a.practice_subsector.name]
            if a.practice_topic:
                if a.practice_topic.name not in subsector_dictionary:
                    subsector_dictionary[a.practice_topic.name] = []
                topic_list = subsector_dictionary[a.practice_topic.name]
                if a.practice_subtopic:
                    if a.practice_subtopic.name not in topic_list:
                        topic_list.append(a.practice_subtopic.name)

    resp = json.dumps({"mapping_dropdown": practice_dictionary})
    return HttpResponse(resp)


def login_view(request, template_name='registration/login.html',
                      redirect_field_name=REDIRECT_FIELD_NAME,
                      authentication_form=AuthenticationForm,
                      current_app=None, extra_context=None):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return django_login_view(request, template_name, redirect_field_name, authentication_form, current_app, extra_context)


def signup_view(request, template_name='social_website/signup.html',
                redirect_field_name=REDIRECT_FIELD_NAME,
                signup_form=CustomUserCreationForm,
                current_app=None, extra_context=None):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = signup_form(data=request.POST)
        if form.is_valid():
            a = form.save()
            a.email = a.username
            a.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return HttpResponseRedirect(redirect_to)
    else:
        form = signup_form(None)

    context = {
        'form': form,
    }

    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


# Check if Video Already Exist or Not in the DB If so return appropriate message
# Check if Video Chunk exist or not
@csrf_exempt
def video_combine_view(request):
    if request.method == 'GET':
        chunk_number = request.GET.get('resumableChunkNumber')
        file_identifier = request.GET.get('resumableIdentifier')
        try:
            video_chunk = VideoChunk.objects.get(video_file__file_identifier=file_identifier, chunk_number=chunk_number)
            return HttpResponse(status=200)
        except VideoChunk.DoesNotExist:
            return HttpResponse(status=201)  # any number other than 200 to notify client chunk exist
    elif request.method == 'POST':
        make_entry = request.POST.get('make_entry', None)
        combine_flag = request.POST.get('combine', None)
        save_flag = request.POST.get('save', None)
        if make_entry:
            file_identifier = request.POST.get('fileidentifier', None)
            total_chunks = request.POST.get('num_chunks', None)
            file_name = request.POST.get('filename', None)
            try:
                video = VideoFile.objects.get(file_identifier=file_identifier)
                if video.upload:
                    return HttpResponse(1)
                else:
                    return HttpResponse(0)
            except VideoFile.DoesNotExist:
                video = VideoFile(file_identifier=file_identifier, total_chunks=total_chunks, file_name=file_name)
                video.save()
                return HttpResponse(0)
        elif combine_flag:
            file_identifier = request.POST.get('fileidentifier', None)
            res = combine(request.POST.get('fileidentifier'))
            return HttpResponse(res)
        elif save_flag:
            file_identifier = request.POST.get('fileidentifier', None)
            video_id = request.POST.get('video_id', None)
            title = request.POST.get('title', None)
            desc = request.POST.get('desc', None)
            category = request.POST.get('category', None)
            sub_category = request.POST.get('sub_category', None)
            topic = request.POST.get('topic', None)
            sub_topic = request.POST.get('sub_topic', None)
            subject = request.POST.get('subject', None)

            category = category if category != '' else None
            sub_category = sub_category if sub_category != '' else None
            topic = topic if topic != '' else None
            sub_topic = sub_topic if sub_topic != '' else None
            subject = subject if subject != '' else None
            practice_object = Practice.objects.filter(practice_sector__name=category, practice_subsector__name=sub_category, practice_topic__name=topic, practice_subtopic__name=sub_topic, practice_subject__name=subject)[0]
            videofile = VideoFile.objects.get(file_identifier=file_identifier)
            videofile.coco_video_id = video_id
            videofile.save()
            coco_video = Dashboard_Video.objects.get(id=video_id)
            coco_video.title = title
            coco_video.summary = desc
            coco_video.related_practice_id = practice_object.id
            coco_video.save()
            return HttpResponse(1)
        else:
            chunk_number = request.POST.get('resumableChunkNumber')
            file_identifier = request.POST.get('resumableIdentifier')
            file_name = MEDIA_ROOT + '/videos/' + request.POST.get('resumableChunkNumber') + request.POST.get('resumableFilename')
            try:
                video_chunk = VideoChunk.objects.get(video_file__file_identifier=file_identifier, chunk_number=chunk_number)
                return HttpResponse(request.POST.get('resumableChunkNumber'))
            except VideoChunk.DoesNotExist:
                f = request.FILES['file']
                destination = open(file_name, 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
                video_chunk = VideoChunk(video_file=VideoFile.objects.get(file_identifier=file_identifier) ,chunk_number=chunk_number)
                video_chunk.save()
                print "chunk saved"
                return HttpResponse(request.POST.get('resumableChunkNumber'))


def videodropdown(request):
    partner = request.GET.get('partner', None)
    state = request.GET.get('state', None)
    language = request.GET.get('language', None)
    videos = Dashboard_Video.objects.filter(youtubeid='', partner_id=partner, village__block__district__state_id=state, language_id=language).select_related('related_practice')
    videos_list = []

    for v in videos:

        if v.related_practice:
            mapping_dictionary = {
                                  'category': v.related_practice.practice_sector.name if v.related_practice.practice_sector else 'Null',
                                  'subcategory': v.related_practice.practice_subsector.name if v.related_practice.practice_subsector else 'Null',
                                  'topic': v.related_practice.practice_topic.name if v.related_practice.practice_topic else 'Null',
                                  'subtopic': v.related_practice.practice_subtopic.name if v.related_practice.practice_subtopic else 'Null',
                                  'subject': v.related_practice.practice_subject.name if v.related_practice.practice_subject else 'Null',
                              }
        else:
            mapping_dictionary = "Null"

        obj = {'title': v.title,
               'uid': v.id,
               'desc': v.summary,
               'practice': mapping_dictionary,
               }
        videos_list.append(obj)
    resp = json.dumps({"objects": videos_list})
    return HttpResponse(resp)
