from django.conf.urls.defaults import *
from dg.views import *
from django.contrib.auth.views import login, logout
from dg.output.views import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dg/', include('dg.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^ajax_filtered_fields/', include('ajax_filtered_fields.urls')),
    (r'^feeds/persons/$', feed_person_html_on_person_group),
    (r'^feeds/person_pract/$',feed_person_prac_pg_anim),
	(r'^feeds/persons_village/(\d+)/$', feeds_persons_village),
	(r'^feeds/test/(\d+)/$', test),
	(r'^feeds/test_gwt/(\d+)/$', test_gwt),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
	(r'^animators-by-village-id/(\d+)/$', feed_animators),
    (r'/search/', search),
    (r'^dashboard/getkey/$', get_key_for_user),
    (r'^dashboard/setkey/$', set_key_for_user),
	(r'^dashboard/login/$', login_view),
    (r'^dashboard/saveregiononline/$', save_region_online),
    (r'^dashboard/getregionsonline/$', get_regions_online),
    (r'^dashboard/saveregionoffline/$', save_region_offline),
    (r'^dashboard/savestateonline/$', save_state_online),
    (r'^dashboard/getstatesonline/$', get_states_online),
    (r'^dashboard/savestateoffline/$', save_state_offline),
    (r'^dashboard/savefieldofficeronline/$', save_fieldofficer_online),
    (r'^dashboard/getfieldofficersonline/$', get_fieldofficers_online),
    (r'^dashboard/savefieldofficeroffline/$', save_fieldofficer_offline),
    (r'^dashboard/savepracticeonline/$', save_practice_online),
    (r'^dashboard/getpracticesonline/$', get_practices_online),
    (r'^dashboard/savepracticeoffline/$', save_practice_offline),
    (r'^dashboard/savelanguageonline/$', save_language_online),
    (r'^dashboard/getlanguagesonline/$', get_languages_online),
    (r'^dashboard/savelanguageoffline/$', save_language_offline),
    (r'^dashboard/savepartneronline/$', save_partner_online),
    (r'^dashboard/getpartnersonline/$', get_partners_online),
    (r'^dashboard/savepartneroffline/$', save_partner_offline),
    (r'^dashboard/savevideoonline/$', save_video_online),
    (r'^dashboard/getvideosonline/$', get_videos_online),
    (r'^dashboard/savevideooffline/$', save_video_offline),
    (r'^dashboard/savedevelopmentmanageronline/$', save_developmentmanager_online),
    (r'^dashboard/getdevelopmentmanagersonline/$', get_developmentmanagers_online),
    (r'^dashboard/savedevelopmentmanageroffline/$', save_developmentmanager_offline),
    (r'^dashboard/saveequipmentonline/$', save_equipment_online),
    (r'^dashboard/getequipmentsonline/$', get_equipments_online),
    (r'^dashboard/saveequipmentoffline/$', save_equipment_offline),    
    (r'^dashboard/savedistrictonline/$', save_district_online),
    (r'^dashboard/getdistrictsonline/$', get_districts_online),
    (r'^dashboard/savedistrictoffline/$', save_district_offline),
    (r'^dashboard/saveblockonline/$', save_block_online),
    (r'^dashboard/getblocksonline/$', get_blocks_online),
    (r'^dashboard/saveblockoffline/$', save_block_offline),
    (r'^dashboard/savevillageonline/$', save_village_online),
    (r'^dashboard/getvillagesonline/$', get_villages_online),
    (r'^dashboard/savevillageoffline/$', save_village_offline),
    (r'^dashboard/saveanimatoronline/$', save_animator_online),
    (r'^dashboard/getanimatorsonline/$', get_animators_online),
    (r'^dashboard/saveanimatoroffline/$', save_animator_offline),
    (r'^dashboard/saveanimatorassignedvillageonline/$', save_animatorassignedvillage_online),
    (r'^dashboard/getanimatorassignedvillagesonline/$', get_animatorassignedvillages_online),
    (r'^dashboard/saveanimatorassignedvillageoffline/$', save_animatorassignedvillage_offline),
    (r'^dashboard/savepersongrouponline/$', save_persongroup_online),
    (r'^dashboard/getpersongroupsonline/$', get_persongroups_online),
    (r'^dashboard/savepersongroupoffline/$', save_persongroup_offline),
    (r'^dashboard/savepersononline/$', save_person_online),
    (r'^dashboard/getpersonsonline/$', get_persons_online),
    (r'^dashboard/savepersonoffline/$', save_person_offline),
    (r'^dashboard/savescreeningonline/$', save_screening_online),
    (r'^dashboard/getscreeningsonline/$', get_screenings_online),
    (r'^dashboard/savescreeningoffline/$', save_screening_offline),
    (r'^dashboard/savetrainingonline/$', save_training_online),
    (r'^dashboard/gettrainingsonline/$', get_trainings_online),
    (r'^dashboard/savetrainingoffline/$', save_training_offline),
    (r'^dashboard/gettraininganimatorstrainedonline/$', get_traininganimatorstrained_online),
    (r'^dashboard/savemonthlycostpervillageonline/$', save_monthlycostpervillage_online),
    (r'^dashboard/getmonthlycostpervillagesonline/$', get_monthlycostpervillages_online),
    (r'^dashboard/savemonthlycostpervillageoffline/$', save_monthlycostpervillage_offline),
    (r'^dashboard/saveanimatorsalarypermonthonline/$', save_animatorsalarypermonth_online),
    (r'^dashboard/getanimatorsalarypermonthsonline/$', get_animatorsalarypermonths_online),
    (r'^dashboard/saveanimatorsalarypermonthoffline/$', save_animatorsalarypermonth_offline),
    (r'^dashboard/savepersonrelationonline/$', save_personrelation_online),
    (r'^dashboard/getpersonrelationsonline/$', get_personrelations_online),
    (r'^dashboard/savepersonrelationoffline/$', save_personrelation_offline),
    (r'^dashboard/savepersonmeetingattendanceonline/$', save_personmeetingattendance_online),
    (r'^dashboard/getpersonmeetingattendancesonline/$', get_personmeetingattendances_online),
    (r'^dashboard/savepersonmeetingattendanceoffline/$', save_personmeetingattendance_offline),
    (r'^dashboard/savepersonadoptpracticeonline/$', save_personadoptpractice_online),
    (r'^dashboard/getpersonadoptpracticesonline/$', get_personadoptpractices_online),
    (r'^dashboard/savepersonadoptpracticeoffline/$', save_personadoptpractice_offline),
    (r'^dashboard/saveequipmentholderonline/$', save_equipmentholder_online),
    (r'^dashboard/getequipmentholdersonline/$', get_equipmentholders_online),
    (r'^dashboard/saveequipmentholderoffline/$', save_equipmentholder_offline),
    (r'^dashboard/saverevieweronline/$', save_reviewer_online),
    (r'^dashboard/getreviewersonline/$', get_reviewers_online),
    (r'^dashboard/saverevieweroffline/$', save_reviewer_offline),          
    (r'^dashboard/language/add/$', add_language),
	(r'^dashboard/languages/(?P<language>[^/]+)/$',language),
	(r'^dashboard/region/add/$',add_region),
	(r'^dashboard/regions/$',region),
	(r'^dashboard/state/add/$',add_state),
	(r'^dashboard/states/$',state),
	(r'^dashboard/district/add/$', add_district),
	(r'^dashboard/districts/$', district),
	(r'^dashboard/block/add/$', add_block),
	(r'^dashboard/blocks/$', block),
	(r'^dashboard/persongroup/add/$', add_person_group),
	(r'^dashboard/persongroups/$', person_group),
	(r'^dashboard/developmentmanager/add/$', add_development_manager),
	(r'^dashboard/developmentmanagers/$', development_manager),
	(r'^dashboard/animatorassignedvillage/add/$', add_animator_assigned_village),
	(r'^dashboard/animatorassignedvillages/$', animator_assigned_village),
	(r'^dashboard/animator/add/$', add_animator),
	(r'^dashboard/animators/$', animator),
	(r'^dashboard/fieldofficer/add/$', add_field_officer),
	(r'^dashboard/fieldofficers/$', field_officer),
	(r'^dashboard/partner/add/$', add_partner),
	(r'^dashboard/partners/$', partner),
	(r'^dashboard/person/add/$', add_person),
	(r'^dashboard/persons/$', person),
	(r'^dashboard/practice/add/$', add_practice),
	(r'^dashboard/practices/$', practice),
	(r'^dashboard/village/add/$', add_village),
	(r'^dashboard/villages/$', village),
	(r'^dashboard/video/add/$', add_video),
	(r'^dashboard/videos/', video),
	(r'^dashboard/screening/add/$', add_screening),
	(r'^dashboard/screenings/$', screening),
	(r'^dashboard/login/$', login),
	(r'^dashboard/logout/$', logout),    
    (r'^output/test1/(country|state|district|block|village)/(\d+)$',test_output),
    (r'^output/dropdownval/$',overview_drop_down),
    (r'^output/overview/(country|state|district|block|village)/(\d+)/$',overview),
    (r'^output/overview/line/(country|state|district|block|village)/(\d+)/$',overview_line_graph),
    (r'^output/video/module/(country|state|district|block|village)/(\d+)/$',video_module),
    (r'^output/video/mfpie/(country|state|district|block|village)/(\d+)/$',video_pie_graph_mf_ratio),
    (r'^output/video/actorpie/(country|state|district|block|village)/(\d+)/$',video_actor_wise_pie),
    (r'^output/video/typepie/(country|state|district|block|village)/(\d+)/$',video_type_wise_pie),
    (r'^output/video/geogpie/(country|state|district|block|village)/(\d+)/$',video_geog_pie_data),
    (r'^output/video/practicescatter/(country|state|district|block|village)/(\d+)/$',video_practice_wise_scatter),
    (r'^output/video/languagescatter/data/(country|state|district|block|village)/(\d+)/$',video_language_wise_scatter_data),
    (r'^output/video/monthbar/data/(country|state|district|block|village)/(\d+)/$',video_monthwise_bar_data),
    (r'^output/video/monthbar/settings/(country|state|district|block|village)/(\d+)/$',video_monthwise_bar_settings),
        
)
