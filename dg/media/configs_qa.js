define([],
function() {
	var VideoContentApproval_configs = {
		'page_header': 'Video Content Approval',
		'add_template_name': 'Video_Content_Approval_add_edit_template',
        'edit_template_name': 'Video_Content_Approval_add_edit_template',
        'rest_api_url': '/qacoco/api/v1/VideoContentApproval/',
        'list_elements': [{'header':'Video','element':'video'},{'header':'Reviewer','element':'reviewer'},{'header':'Comment','element':'comment'}],
        'entity_name': 'VideoContentApproval',
        'dashboard_display': {
            listing: true,
            add: true
        },
        'sort_field': 'video',
        'foreign_entities':{
            'video':{
                "video":{
                    'placeholder': 'id_video',
                    'name_field': 'title'
                },
            },
            'reviewer':{
                "reviewer":{
                'placeholder' : 'id_reviewed_by',
                'name_field' : 'name'
            }
        }
    }
};
    
    
    /*'form_field_validation': {
            ignore: [],
            rules: {
                video: "required",
                reviewer: "required",
                comment:{
                	required: true,
                    minlength: 2,
                    maxlength: 100,
                    allowedChar: true
            	},
            messages: {
                video: "Video name is required"
                reviewer: "Reviewer name is required",
                comment: {
                	required: 'Comment is required',
                    minlength: 'Comment should contain at least 2 characters',
                    maxlength: 'Comment should contain at most 100 characters',
                    allowedChar: 'Comment should contain only english and local language characters'

                },
            },
             highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline red-color",
            errorPlacement: function(label, element) {
                element.parent().append(label);
            }
        }

    };*/

    var VideoQualityReview_configs = {
        'page_header': 'Video Quality Review',
        'add_template_name': 'Video_Quality_Review_add_edit_template',
        'edit_template_name': 'Video_Quality_Review_add_edit_template',
        'rest_api_url': '/qacoco/api/v1/VideoQualityReview/',
        'list_elements': [{'header':'Video','element':'video'},{'header':'Reviewer','element':'reviewer'},{'header':'Total Score','element':'total_score'},{'header':'Video Grade','element':'video_grade'}],
        'entity_name': 'VideoQualityReview',
        'dashboard_display': {
            listing: true,
            add: true
        },
        'sort_field': 'video',
        'foreign_entities':{
            'video':{
                "video":{
                    'placeholder': 'id_video',
                    'name_field': 'title'
                },
            },
            'reviewer':{
                "reviewer":{
                    'placeholder' : 'id_reviewed_by',
                    'name_field' : 'name'
                }
            }
        }
    };

var DisseminationQuality_configs = {
        'page_header': 'Dissemination Quality',
        'add_template_name': 'Dissemination_Quality_add_edit_template',
        'edit_template_name': 'Dissemination_Quality_add_edit_template',
        'rest_api_url': '/qacoco/api/v1/DisseminationQuality/',
        'list_elements': [{'header':'Video','element':'video'},{'header':'Date','element':'date'}],
        'entity_name': 'DisseminationQuality',
        'dashboard_display': {
            listing: true,
            add: true
        },
        'sort_field': 'video',
        'foreign_entities':{
            'video':{
                "video":{
                    'placeholder': 'id_video',
                    'name_field': 'title'
                },
            },
            'village':{
                "village":{
                    'placeholder': 'id_village',
                    'name_field': 'village_name'
                },
            },
            'mediator':{
                "mediator":{
                    'placeholder': 'id_mediator',
                    'name_field': 'mediator_name'
                },
            },
            'block':{
                "block":{
                'placeholder' : 'id_block',
                'name_field' : 'block_name'
            }
        }
    }
};

var AdoptionVerification_configs = {
        'page_header': 'Adoption Verification',
        'add_template_name': 'Adoption_Verification_add_edit_template',
        'edit_template_name': 'Adoption_Verification_add_edit_template',
        'rest_api_url': '/qacoco/api/v1/AdoptionVerification/',
        'list_elements': [{'header':'Video','element':'video'},{'header':'Village','element':'village'},{'header':'Block','element':'block'}],
        'entity_name': 'AdoptionVerification',
        'dashboard_display': {
            listing: true,
            add: true
        },
        'sort_field': 'video',
        'foreign_entities':{
            'video':{
                "video":{
                    'placeholder': 'id_video',
                    'name_field': 'video_name'
                },
            },
            'village':{
                "village":{
                    'placeholder': 'id_village',
                    'name_field': 'village_name'
                },
            },
            'mediator':{
                "mediator":{
                    'placeholder': 'id_mediator',
                    'name_field': 'mediator_name'
                },
            },
            'group':{
                "group":{
                    'placeholder': 'id_group',
                    'name_field': 'group_name'
                },
            },
            'person':{
                "person":{
                    'placeholder': 'id_person',
                    'name_field': 'person_name'
                },
            },
            'block':{
                "block":{
                'placeholder' : 'id_block',
                'name_field' : 'block_name'
            }
        }
    }
};

     var video_configs = {
        'rest_api_url': '/qacoco/api/v1/video/',
        'entity_name': 'video',
        'sort_field': 'title',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };
    var reviewed_by_configs = {
        'rest_api_url': '/qacoco/api/v1/reviewer/',
        'entity_name': 'reviewer',
        'sort_field': 'name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };
    var block_configs = {
        'rest_api_url': '/qacoco/api/v1/block/',
        'entity_name': 'block',
        'sort_field': 'name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };
    var village_configs = {
        'rest_api_url': '/qacoco/api/v1/village/',
        'entity_name': 'village',
        'sort_field': 'name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };
    var mediator_configs = {
        'rest_api_url': '/qacoco/api/v1/mediator/',
        'entity_name': 'mediator',
        'sort_field': 'name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };
    var group_configs = {
        'rest_api_url': '/qacoco/api/v1/group/',
        'entity_name': 'group',
        'sort_field': 'name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };
    var person_configs = {
        'rest_api_url': '/qacoco/api/v1/person/',
        'entity_name': 'person',
        'sort_field': 'name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };


    var misc = {
        download_chunk_size: 2000,
        background_download_interval: 5 * 60 * 1000,
        inc_download_url: "/get_log/",
        afterFullDownload: function(start_time, download_status){
            return saveTimeTaken();
            function saveTimeTaken(){
                var record_endpoint = "/coco/record_full_download_time/"; 
                return $.post(record_endpoint, {
                    start_time : start_time,
                    end_time : new Date().toJSON().replace("Z", "")
                })    
            }
        },
        reset_database_check_url: '/coco/reset_database_check/',
        onLogin: function(Offline, Auth){
            getLastDownloadTimestamp()
                .done(function(timestamp){
                    askServer(timestamp);
                });
            var that = this;    
            function askServer(timestamp){
                $.get(that.reset_database_check_url,{
                    lastdownloadtimestamp: timestamp
                })
                    .done(function(resp){
                        console.log(resp);
                        if(resp=="1")
                        {
                            alert("Your database will be redownloaded because of some changes in data.");
                            Offline.reset_database();
                        }
                    });
            }   
            function getLastDownloadTimestamp()
            {
                var dfd = new $.Deferred();
                Offline.fetch_object("meta_data", "key", "last_full_download_start")
                    .done(function(model){
                        dfd.resolve(model.get("timestamp"));
                    })
                    .fail(function(model, error){
                    
                    });
                return dfd;    
            } 
        }
    };
   

    return {
        VideoContentApproval : VideoContentApproval_configs,
        video : video_configs,
        VideoQualityReview : VideoQualityReview_configs,
        DisseminationQuality : DisseminationQuality_configs,
        AdoptionVerification : AdoptionVerification_configs,
        reviewer : reviewed_by_configs,
        block : block_configs,
        village : village_configs,
        mediator : mediator_configs,
        group : group_configs,
        person : person_configs,

        misc: misc

    }

});
