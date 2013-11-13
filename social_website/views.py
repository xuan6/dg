import ast
import datetime
import json
import os
import urllib2

from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from dashboard.models import PracticeSector, PracticeSubSector, PracticeTopic, PracticeSubtopic, PracticeSubject
from elastic_search import get_related_collections, get_related_videos
from social_website.models import  Collection, Partner, FeaturedCollection, Video, VideoChunk, VideoData, VideoFile
from django.views.decorators.csrf import csrf_exempt

import dg.settings
from social_website.scripts.combine_upload import combine

def social_home(request):
    language = Collection.objects.exclude(language = None).values_list('language',flat=True) # only using those languages that have collections 
    language = sorted(set(language))
    context= {
        'header': {
            'jsController':'Home',
            'loggedIn':False
             },
        'language':language,
        }
    return render_to_response('home.html', context, context_instance = RequestContext(request))

def collection_view(request, partner, state, language, title, video=1):
    try:
        collection = Collection.objects.get(partner__name__iexact = partner, state__iexact = state, language__iexact = language, title__iexact = title)
    except Collection.DoesNotExist:
        return HttpResponseRedirect(reverse('discover'))
    try:
        video_index = int(video)
        video = collection.videos.all()[video_index - 1]
    except (IndexError, AssertionError):
        video_index = 1
        video = collection.videos.all()[video_index - 1]    
    tags = [x for x in [video.category,video.subcategory,video.topic,video.subtopic,video.subject] if x is not u'']
    duration = sum([v.duration for v in collection.videos.all()])
    related_collection_dict = get_related_collections(collection)
    context= {
              'header': {
                         'jsController':'ViewCollections',
                         'currentPage':'Discover',
                         'loggedIn':False
                         },
              'collection': collection,
              'duration' : duration,
              'video' : video,
              'video_index' : video_index,
              'tags' : tags,
              'related_collections' : related_collection_dict[:4], # restricting to 4 related collections for now
              }
    return render_to_response('collections-view.html' , context, context_instance = RequestContext(request)) 

def partner_view(request, partner):
    try:
        partner = Partner.objects.get(name__iexact = partner)
    except Partner.DoesNotExist:
        return HttpResponseRedirect(reverse('connect'))
    context= {
        'header': {
            'jsController':'Profile',
            'loggedIn':False,
            'currentPage':'Connect',
            },
        'partner': partner,
        }
    return render_to_response('profile.html', context, context_instance = RequestContext(request))

def search_view(request):
    searchString = request.GET.get('searchString', None)
    partner = request.GET.get('partner', None)
    title = request.GET.get('title', None)
    state = request.GET.get('state', None)
    context= {
              'header': {
                         'jsController':'Collections',
                         'currentPage':'Discover',
                         'loggedIn'    : False
                         },
              'searchString' : searchString,
              'partner' : partner,
              'title' : title,
              'state' : state,
        }
    return render_to_response('collections.html', context, context_instance=RequestContext(request))
    
def make_sub_filter(filters, field, active_filter_list, facet_dict):
    kwargs = {}
    kwargs[field] = ''
    filters[field] = {}
    filters[field]['title'] = field.title()
    filters[field]['options'] = []
    for obj in set(Collection.objects.exclude(**kwargs).values_list(field, flat=True)): #works same as .exclude(field = '')
        facet_count = facet_dict[obj] if facet_dict.has_key(obj) else 0
        if facet_count or facet_dict == {}:
            filters[field]['options'].append({"title" : obj,"value" : obj, "filterActive" : obj in active_filter_list, "count" : facet_count})
    return filters

def searchFilters(request):
    params = request.GET
    facets = params.get('facets', None)
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
    for obj in Partner.objects.all():
        facet_count = facet_dict[obj.name] if facet_dict.has_key(obj.name) else 0
        if facet_count or facet_dict == {}:
            filters['partner']['options'].append({"title" : obj.name,"value" : obj.name, "filterActive" : obj.name in partner, "count" : facet_count })
        
    filters = make_sub_filter(filters, 'category', category, facet_dict)
    filters = make_sub_filter(filters, 'subcategory', subcategory, facet_dict)
    filters = make_sub_filter(filters, 'topic', topic, facet_dict)
    filters = make_sub_filter(filters, 'state', state, facet_dict)
    filters = make_sub_filter(filters, 'subject', subject, facet_dict)
    filters = make_sub_filter(filters, 'language', language, facet_dict)

    data = json.dumps({"categories" : filters})
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
    collection= featured_collection.collection
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
    footer_dict={
        'likes':data['likes'],
        }
    context= {
        'header': {
            'jsController':'Footer',
            'loggedIn':False},
        'footer_dict':footer_dict
        }
    return render_to_response('footer.html' , context,context_instance = RequestContext(request))


def logout_view(request):
    next_url = request.GET.get('next', None)
    logout(request)
    return HttpResponseRedirect(next_url)

def video_view(request, partner, state, language, title):
    try:
        video = Video.objects.get(partner__name__iexact = partner, state__iexact = state, language__iexact = language, title__iexact = title)
    except Video.DoesNotExist:
        return HttpResponseRedirect(reverse('discover'))

    tags = [x for x in [video.category, video.subcategory, video.topic, video.subtopic, video.subject] if x is not u'']
    related_collection = Collection.objects.filter(partner=video.partner)
    related_collection_list = []
    for collection in related_collection:
        duration = sum([v.duration for v in collection.videos.all()])
        related_collection_list.append([collection, duration])
    related_videos_dict = get_related_videos(video)
    context = {
              'header': {
                         'jsController':'ViewCollections',
                         'currentPage':'Discover',
                         },
              'video': video,
              'related_videos': related_videos_dict,
              'tags': tags,
              'related_collections': related_collection_list[:4], # restricting to 4 related collections for now
              }
    return render_to_response('video_view.html' , context, context_instance = RequestContext(request))


def collection_add_view(request):
    try:
        video = Video.objects.get(uid=1)
    except Video.DoesNotExist:
        return HttpResponseRedirect(reverse('discover'))
    print "here"
    tags = [x for x in [video.category, video.subcategory, video.topic, video.subtopic, video.subject] if x is not u'']
    related_collection = Collection.objects.filter(partner=video.partner)
    related_collection_list = []
    for collection in related_collection:
        duration = sum([v.duration for v in collection.videos.all()])
        related_collection_list.append([collection, duration])
    related_videos_dict = get_related_videos(video)
    print related_videos_dict
    context = {
              'header': {
                         'jsController':'CollectionAdd',
                         },
              'video': video,
              'related_videos': related_videos_dict,
              'tags': tags,
              'related_collections': related_collection_list[:4], # restricting to 4 related collections for now
              }
    return render_to_response('collection_add.html' , context, context_instance = RequestContext(request))

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
            return HttpResponse(status=201) # any number other than 200 to notify client chunk exist
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
            video_title = request.POST.get('video_title', None)
            video_desc = request.POST.get('video_desc', None)
            date = request.POST.get('date', None)
            partner_id = request.POST.get('partner', None)
            state = request.POST.get('state', None)
            language = request.POST.get('language', None)

            try:
                video_data = VideoData.objects.get(video_file__file_identifier=file_identifier)
                video_data.video_title = video_title
                video_data.video_desc = video_desc
                video_data.date = date
                video_data.partner_id = partner_id
                video_data.state = state
                video_data.language = language
                video_data.save()
            except VideoData.DoesNotExist:
                video_data = VideoData(video_file=VideoFile.objects.get(file_identifier=file_identifier), video_title=video_title, video_desc=video_desc, date=date, state=state, partner_id=partner_id, language=language)
                video_data.save()
        else:
            chunk_number = request.POST.get('resumableChunkNumber')
            file_identifier = request.POST.get('resumableIdentifier')
            file_name = dg.settings.MEDIA_ROOT + 'videos/' + request.POST.get('resumableChunkNumber') + request.POST.get('resumableFilename')
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


def videoadddropdown(request):
    video = Video.objects.all()
    language = video.values_list('language',flat=True)
    language = sorted(set(language))
    partner = Partner.objects.values('name', 'uid')
    partner = sorted(partner)
    state = video.values_list('state',flat=True)
    state = sorted(set(state))
    sector = PracticeSector.objects.values_list('name', flat=True)
    sector = sorted(set(sector))
    subsector = PracticeSubSector.objects.values_list('name', flat=True)
    subsector = sorted(set(subsector))
    subject = PracticeSubject.objects.values_list('name', flat=True)
    subject = sorted(set(subject))
    topic = PracticeTopic.objects.values_list('name', flat=True)
    topic = sorted(set(topic))
    subtopic = PracticeSubtopic.objects.values_list('name', flat=True)
    subtopic = sorted(set(subtopic))
    video_dropdown_dict = {
        'language': language,
        'partner': partner,
        'state': state,
        'sector': sector,
        'subsector': subsector,
        'topic': topic,
        'subtopic': subtopic,
        'subject': subject,
    }
    resp = json.dumps({"video_dropdown": video_dropdown_dict})
    return HttpResponse(resp)
