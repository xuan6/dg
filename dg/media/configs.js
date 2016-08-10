﻿define([],
function() {
    
    /*
    var dummy_config = {
        entity_name : 
        //string = key of this object in all_config, name of objectstore in IDB
        //for - accessing this object 
        
        'rest_api_url': '/coco/api/v2/village/',
        //string - the rest url for this entity
    
        'dashboard_display': {
            listing: false,         //whether to provide listing option for this entity on dashboard
            add: false              //whether to provide add option for this entity on dashboard
        },
    
        -----------------------------------Listing configs---------------------------------
        page_header: 'Village',  
        //string = The name that needs to shown in headers 

        list_table_header_template: 'village_table_template',  
        //HTML template - The id of template used as coloumn headers in list page

        list_table_row_template: 'village_list_item_template',  
        //HTML template - The id of template used to create rows of list table. 
        //This template is passed the model json.
        -----------------------------------------------------------------------------------
    
        ----------------------------------Form configs-------------------------------------
        foreign_entities: {
            f_entity_name:{         //the entity_name of foreign element
                attribute_name:{    //the attribute name of this foreign element in json
                    
                    'placeholder': 'string - the id of element in form's html where the dropdown of this f_entity is inserted',
                    
                    'name_field': 'string - the attribute name in f_entity's json which needs to be shown in its dropdown',
                    
                    'dependency': [{    // whether this elements's dropdown depends on value of other form elements
                        'source_form_element': 'village',   // attribute name of source element in json
                        'dep_attr': 'village'   //the attribute name in json of dependent f_entity which refers to source f_entity
                        'src_attr' : //to compare dep_attr of dependent element with a particular attribute in source f_entity
                    }],
                    
                    'filter': { //whether to filter the objects of foreign entity before rendering into dropdown
                        attr: 'group',  //the attribute name in f_entity's json to filter on
                        value: null     //desired value of the attr
                    },
    
                    id_field: "person_id", // the name of id field for this f_entity in denormalised json                         
                }
            },
    
            f_entity_name:{         //the entity_name of foreign element
                attribute_name:{    //the attribute name of this foreign element in json
                    
                    'dependency': [{    // whether this elements's dropdown depends on value of other form elements
                        'source_form_element': 'village',   // attribute name of source element in json
                        'dep_attr': 'village'   //the attribute name in json of dependent f_entity which refers to source f_entity
                    }],

                    id_field: "person_id", // the name of id field for this f_entity in denormalised json     

                    //would not use options template to render its objects - would use the specfied template    
                    // won't be denormalised, wud be converted offline to online, 
                    //any field to be denormalised or converted offline to online can be declared - 
                    //this shd be clubbed and put as foreign entity of expanded.   
                    'expanded': { 
                        template: 'person_pma_template', // the template to use instead of options
                        placeholder: 'pmas',    // the id of placeholder in form's HTML
                        TODO: the following two should be merged and converted to same format as foreign_entities
                        denormalize: { // any field in expanded template to be denormalised     
                            "expressed_adoption_video": {
                                name_field: 'title' //used as key for name in denormalised object
                            }
                        },
                        foreign_fields: { // any more field in expanded template for offline to online conv
                            "expressed_adoption_video": {
                                entity_name: "video"  //the entity_name for this f_entity element
                            }
                        },
                        extra_fields: ["expressed_question", "interested", "expressed_adoption_video"]
                    }
                }
            }
        },    
        //object - describes the foreign keys in the json of this entity's model.
        //To convert between online offline namespaces, denormalize-normalize json    
    
        inline: {
            'entity': 'person',     //entity name of inline
    
            'default_num_rows': 10,         //default num of rows to show
    
            "template": "person_inline",    //id of template used to render inline
            //Include any jquery validation desired inside html of rows 
            //TODO: need to explain the <%index%> tags required in inlines
    
            "foreign_attribute": {
                'host_attribute': ["id", "group_name"],
                'inline_attribute': "group"
            },
            "header": "person_inline_header",
            'borrow_attributes': [{
                'host_attribute': 'village',
                'inline_attribute': 'village'
            }]
        },      
        //object - describes inlines to be included in this entity's form

        bulk:{},     
        //object - if multiple objects of this entity type can be saved through its add form, describe configs of object 
        ------------------------------------------------------------------------------------
    }
    */
    
    // //This template would be passed the json of inline model and shall produce the desired row
//     TODO: maybe instead of relying on users to use templating lang we should fill the rows ourselves in js code, like we are doing in form!

    var village_configs = {
        'page_header': 'Village',
        'config_English': 'Villages',
        'config_हिन्दी': 'विलेजस',
        'list_elements_English': [{'header':'ID','element':'online_id'},{'header':'Name','element':'village_name'},{'element':'block_name'},{'element':'start_date'},{'header':'State','element':'state_name'}],
        'list_elements_हिन्दी': [{'header':'आइडी','element':'online_id'},{'header':'नाम','element':'village_name'},{'header':'ब्लॉक','element':'block_name'},{'header':'स्टार्ट डटे','element':'start_date'},{'header':'स्टेट','element':'state_name'}],
        'rest_api_url': '/coco/api/v2/village/',
        'entity_name': 'village',
        'dashboard_display': {
            listing: true,
            add: false
        },
        'sort_field': 'village_name'
    };

    var mediator_configs = {
        'page_header': 'Mediator',
        'config_English': 'Mediators',
        'config_हिन्दी': 'मीडियेटर',
        'labels_हिन्दी': {mediator: "मीडियेटर", name: "नाम", district: "जिला", gender: "लिंग", phone_number: "फोन नंबर", assigned_villages: "Assigned Villages"},
        'labels_English': {mediator: "Mediator",name: "Name", district: "District", gender: "Gender", phone_number: "Phone Number", assigned_villages: "Assigned Villages"},
        'list_elements_हिन्दी': [{'header':'आइडी', 'element':'online_id'},{'header':'नाम','element':'name'},{'header':'विलेजस','subelement':'village_name','element':'assigned_villages'}],
        'list_elements_English': [{'header':'ID', 'element':'online_id'},{'element':'name'},{'subelement':'village_name','element':'assigned_villages'}],
        'add_template_name': 'mediator_add_edit_template',
        'edit_template_name': 'mediator_add_edit_template',
        'rest_api_url': '/coco/api/v2/mediator/',
        'entity_name': 'mediator',
        'unique_together_fields': ['name', 'gender', 'district.id'],
        'sort_field': 'name',
        'inc_table_name': 'animator',
        'foreign_entities': {
            'village': {
                "assigned_villages": {
                    'placeholder': 'id_ass_villages',
                    'name_field': 'village_name'
                }, //name of html element in form/ attribute name in json: {placeholder: "id of html element in form", name_field: "attribute in foreign entity's json "} 
            },
            district: {
                district :{
                    placeholder : 'id_district',
                    name_field : 'district_name' 
                }
            }
        },
        'form_field_validation': {
            ignore: [],
            rules: {
                name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    allowedChar: true
                },
                gender: "required",
                phone_no: {
                    digits: true,
                    maxlength: 10
                },
                assigned_villages: "required",
                district: "required"
            },
            messages: {
                name: {
                    required: 'Mediator name is required',
                    minlength: 'Mediator name should contain at least 2 characters',
                    maxlength: 'Mediator name should contain at most 100 characters',
                    allowedChar: 'Mediator name should contain only english and local language characters'
                },
                gender: "Gender is required",
                phone_no: {
                    digits: 'Phone number should contain only digits',
                    maxlength: "Phone number should not contain more than 10 digits"
                },
                assigned_villages: "Assigned villages are required",
                district: "District is required"
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

    };

    var video_configs = {
        'page_header': 'Video',
        'config_English': 'Videos',
        'config_हिन्दी': 'वीडियो',
        'labels_हिन्दी': {video:"वीडियो", title: "शीर्षक", video_type: "Video Type", production_date: "Production Date", language: "Language", benefit: "Benefit", village: "Village", production_team: "Production Team", category: "Category", subcategory: "Sub Category", videopractice:"Video Practice", approval_date: "Approval Date", youtubeid: "Youtube Id", add_row:"खाली पंक्तियाँ जोड़े"},
        'labels_English': {video:"Video", title: "Title", video_type: "Video Type", production_date: "Production Date", language: "Language", benefit: "Benefit", village: "Village", production_team: "Production Team", category: "Category", subcategory: "Sub Category", videopractice:"Video Practice", approval_date: "Approval Date", youtubeid: "Youtube Id", add_row:"Add Empty Rows"},
        'list_elements_हिन्दी': [{'header':'आइडी', 'element':'online_id'},{'header':'टाइटल', 'element':'title'},{'header':'विलेज','element':'village.village_name'},{'header':'प्रोडक्षन डटे','element':'production_date'}],
        'list_elements_English': [{'header':'ID','element':'online_id'},{'element':'title'},{'header':'Village','element':'village.village_name'},{'header':'Production Date','element':'production_date'}],
        'add_template_name': 'video_add_edit_template',
        'edit_template_name': 'video_add_edit_template',
        'rest_api_url': '/coco/api/v2/video/',
        'entity_name': 'video',
        'unique_together_fields': ['title', 'production_date', 'village.id'],
        'sort_field': 'title',
        'foreign_entities': {
            'mediator': {
                "production_team": {
                    'placeholder': 'id_production_team',
                    'name_field': 'name'
                },
            },
            'village': {
                "village": {
                    'placeholder': 'id_village',
                    'name_field': 'village_name'
                },
            },
            'language': {
                "language": {
                    'placeholder': 'id_language',
                    'name_field': 'language_name'
                }
            },
            'category': {
                "category": {
                    'placeholder': 'id_category',
                    'name_field': 'category_name'
                }
            },
            'subcategory': {
                "subcategory": {
                    'placeholder': "id_subcategory",
                    'name_field': "subcategory_name",
                    'dependency': [{
                        'source_form_element': 'category',
                        'dep_attr': 'category'
                    }]
                }
            },
            'videopractice': {
                "videopractice": {
                    'placeholder': "id_videopractice",
                    'name_field': "videopractice_name",
                    'dependency': [{
                        'source_form_element': 'subcategory',
                        'dep_attr': 'subcategory'
                    }]
                }
            }
        },
        'inline': {
            'entity': 'nonnegotiable',
            'validation_chk': '#non_negotiable0',
            'default_num_rows': 5,
            'add_row' : 1,
            'req_nonnegotiable' : 1, 
            'error_message' : 'Add Non-negotiable',
            'template': 'nonnegotiable_inline',
            'joining_attribute': {
                'host_attribute': ["id", "title"],
                'inline_attribute': "video"
            },
            'header': 'nonnegotiable_inline_header',
            'borrow_attributes': [],
            foreign_entities: {
                video: {
                    video: {
                        placeholder: 'id_video',
                        name_field: 'title'
                    }
                }
            }
        },

        'form_field_validation': {
            ignore: ".donotvalidate",
            rules: {
                title: {
                    required: true,
                    minlength: 2,
                    maxlength: 200,
                    // allowedChar: true
                },
                video_type: "required",
                production_date: {
                    required: true,
                    // validateDate: true
                },
                language: "required",
                benefit: {
                    minlength: 2,
                    maxlength: 500,
                    // allowedChar: true
                },
                village: "required",
                production_team: "required",
                category: "required",
                subcategory: "required",
                videopractice: "required",
                approval_date: {
					dateOrder: {production_date : "production_date"}
                    // validateDate: true
                },
                youtubeid: {
                    maxlength: 20
                }
            },
            messages: {
                title: {
                    required: 'Video title is required',
                    minlength: 'Video title should contain at least 2 characters',
                    maxlength: 'Video title should contain at most 200 characters',
                    // allowedChar: 'Video title should only contain alphabets and local language characters'
                },
                video_type: "Video type is required",
                production_date: {
                    required: 'Video production date is required',
                    validateDate: "Enter video production date in the form of YYYY-MM-DD"
                },
                language: "Language is required",
                benefit: {
                    minlength: "Benefit should contain at least 2 characters",
                    maxlength: "Benefit should contain at most 500 characters",
                    // allowedChar: "summary should not contain special characters"
                },
                village: "Village is required",
                production_team: "Production team is required",
                category: "Category is required",
                subcategory: "Subcategory is required",
                videopractice: "Videopractice is required",
                approval_date: {
                    validateDate: "Enter Approval Date in the form of YYYY-MM-DD",
					dateOrder: "Approval date should be later than production date"
                },
                youtubeid: {
                    maxlength: "YoutubeID should contain at most 20 characters"
                }
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
    };

    var language_configs = {
        'config_English': 'Languages',
        'config_हिन्दी': 'लॅंग्वेजस',
        'rest_api_url': '/coco/api/v2/language/',
        'entity_name': 'language',
        'sort_field': 'language_name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };

    var category_configs = {
        'config_English': 'Categories',
        'config_हिन्दी': 'केटेगरीस',
        'rest_api_url': '/coco/api/v2/category/',
        'entity_name': 'category',
        'sort_field': 'category_name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };

    var subcategory_configs = {
        'config_English': 'Sub Categories',
        'config_हिन्दी': 'सब केटेगरीस',
        'rest_api_url': '/coco/api/v2/subcategory/',
        'entity_name': 'subcategory',
        'sort_field': 'subcategory_name',
        'foreign_entities': {
            'category': {
                'category': {
                    'placeholder': 'id_category',
                    'name_field': 'category_name'
                }
            }
        },
        'dashboard_display': {
            listing: false,
            add: false
        }
    };

    var videopractice_configs = {
        'config_English': 'Video Practices',
        'config_हिन्दी': 'वीडियो प्रॅक्टिसस',
        'rest_api_url': '/coco/api/v2/videopractice/',
        'entity_name': 'videopractice',
        'sort_field': 'videopractice_name',
        'foreign_entities': {
            'subcategory': {
                'subcategory': {
                    'placeholder': 'id_subcategory',
                    'name_field': 'subcategory_name'
                }
            }
        },
        'dashboard_display': {
            listing: false,
            add: false
        }
    };

    var nonnegotiable_configs = {
        'config_English': 'Non Negotiables',
        'config_हिन्दी': 'नों नेगोटियब्लेस',
        'rest_api_url': '/coco/api/v2/nonnegotiable/',
        'entity_name': 'nonnegotiable',
        'sort_field': 'non_negotiable',
        'foreign_entities': {
                'video': {
                    'video': {
                        'placeholder': 'id_video',
                        'name_field': 'title'
                    }
                }
            },
        'dashboard_display': {
            listing: false,
            add: false
        }
    };

    var district_configs = {
        'config_English': 'Districts',
        'config_हिन्दी': 'डिस्ट्रिक्ट्स',
        'rest_api_url': '/coco/api/v2/district/',
        'entity_name': 'district',
        'sort_field': 'district_name',
        'dashboard_display': {
            listing: false,
            add: false
        }
    };

    var group_configs = {
        'page_header': 'Group',
        'config_English': 'Groups',
        'config_हिन्दी': 'ग्रूप्स',
        'labels_हिन्दी': {group: "ग्रूप्स", name: "नाम", village: "Village", person_name: "Person Name", father_name: "Father Name", age: "Age", gender: "Gender", phone_no: "Phone No"},
        'labels_English': {group:"Group", name: "Name", village: "village", person_name: "Person Name", father_name: "Father Name", age: "Age", gender: "Gender", phone_no: "Phone No"},
        'list_elements_हिन्दी': [{'header':'आइडी','element':'online_id'},{'header':'नाम','element':'group_name'},{'header':'विलेज','element':'village.village_name'}],
        'list_elements_English': [{'header':'ID','element':'online_id'},{'header':'Name','element':'group_name'},{'header':'Village','element':'village.village_name'}],
        'add_template_name': 'group_add_edit_template',
        'edit_template_name': 'group_add_edit_template',
        'rest_api_url': '/coco/api/v2/group/',
        'entity_name': 'group',
        'inc_table_name': 'persongroup',
        'unique_together_fields': ['group_name', 'village.id'],
        'sort_field': 'group_name',
        'foreign_entities': {
            'village': {
                'village': {
                    'placeholder': 'id_village',
                    'name_field': 'village_name'
                },
            },
        },
        'inline': {
            'entity': 'person',
            'default_num_rows': 10,
            'add_row' : 5,
            "template": "person_inline",
            "joining_attribute": {
                'host_attribute': ["id", "group_name"],
                'inline_attribute': "group"
            },
            "header": "person_inline_header",
            'borrow_attributes': [{
                'host_attribute': 'village',
                'inline_attribute': 'village'
            }],
            foreign_entities: { //used at convert_namespace, denormalize only
                village: {
                    village: {
                        placeholder: 'id_village',
                        name_field: 'village_name'
                    },
                },
                group: {
                    group: {
                        placeholder: 'id_group',
                        name_field: 'group_name'
                    }
                }
            }
        },
        'form_field_validation': {
            ignore: ".donotvalidate",
            rules: {
                group_name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    allowedChar: true
                },
                village: "required"
            },
            messages: {
                name: {
                    required: 'Group name is required',
                    minlength: 'Group name  should contain at least 2 characters',
                    maxlength: 'Group name should contain at most 100 characters',
                    allowedChar: 'Group name should contain only english and local language characters'
                },
                village: "Village is required"
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


    };
    var screening_configs = {
        'page_header': 'Screening',
        'config_English': 'Screenings',
        'config_हिन्दी': 'सक्रीनिंग्स',
        'labels_हिन्दी': {screening:"सक्रीनिंग्स", date: "Date", start_time: "Start Time", village: "Village", mediator: "mediator",
            videos_screened: "Videos Screened", groups_attended: "Groups Attended", person: "Person", questions_asked: "Questions Asked",
            del: "Delete", sr_no: "Sr. No.", person: "Person"},
        'labels_English': {screening:"Screening",date: "Date", start_time: "Start Time", village: "Village", mediator: "mediator",
            videos_screened: "Videos Screened", groups_attended: "Groups Attended", person: "Person", questions_asked: "Questions Asked",
            del: "Delete", sr_no: "Sr. No.", person: "Person"},
        'list_elements_हिन्दी': [{'header':'आइडी','element':'online_id'},{'header':'सक्रीनिंग डटे','element':'date'},{'header':'मीडियेटर','element':'animator.name'},{'header':'विलेज','element':'village.village_name'},{'header':'ग्रूप्स आटएंडेड','subelement':'group_name','element':'farmer_groups_targeted'},{'header':'वीडियोस सक्रींड','subelement':'title','element':'videoes_screened'}],
        'list_elements_English': [{'header':'ID','element':'online_id'},{'header':'Screening Date','element':'date'},{'header':'Mediator','element':'animator.name'},{'header':'Village','element':'village.village_name'},{'header':'Groups Attended','subelement':'group_name','element':'farmer_groups_targeted'},{'header':'Videos Screened','subelement':'title','element':'videoes_screened'}],
        'add_template_name': 'screening_add_edit_template',
        'edit_template_name': 'screening_add_edit_template',
        'rest_api_url': '/coco/api/v2/screening/',
        'entity_name': 'screening',
        download_chunk_size: 1000,
        'unique_together_fields': ['date', 'start_time', 'village.id', 'animator.id'],
        afterSave: function(off_json, Offline){
            var dfd = new $.Deferred();
            var videos_shown = off_json.videoes_screened;
            console.log("recvd off_json in afterSave - "+JSON.stringify(off_json));
            update_attendees()
                .done(function(){
                    dfd.resolve();
                })
                .fail(function(){
                    dfd.reject();
                });
            return dfd.promise();

            function update_attendees(){
                var all_update_dfds = [];
                $.each(off_json.farmers_attendance, function(index, per){
                    all_update_dfds.push(update_attendee(per));    
                });
                return $.when.apply($,all_update_dfds);
            }
            
            function update_attendee(per){
                var p_dfd = new $.Deferred();
                Offline.fetch_object("person", "id", parseInt(per.person_id))
                    .done(function(p_model){
                        console.log("old p -"+JSON.stringify(p_model));
                        var videos_seen = p_model.get("videos_seen");
                        if(videos_seen)
                        {
                            var videos_seen_ids = _.pluck(videos_seen, 'id');
                            $.each(videos_shown, function(index, vid){
                                if($.inArray(vid.id, videos_seen_ids)==-1)
                                    videos_seen.push(vid);
                            });
                        }
                        else
                            videos_seen = videos_shown;
                        p_model.set("videos_seen", videos_seen);
                        Offline.save(p_model, "person", p_model.toJSON())
                            .done(function(p_model){
                                console.log("new p -"+JSON.stringify(p_model));
                                p_dfd.resolve();
                            })
                            .fail(function(error){
                                console.log("error updating person in after save - "+error);
                                p_dfd.reject(error);
                            });
                    })
                    .fail(function(error){
                        console.log("error fetching person in after save - "+error);
                        p_dfd.reject(error);
                    });
                return p_dfd;    
            };
        },
        'foreign_entities': {
            'village': {
                'village': {
                    'placeholder': 'id_village',
                    'name_field': 'village_name'
                },
            },
            'video': {
                'videoes_screened': {
                    'placeholder': 'id_videoes_screened',
                    'name_field': 'title'
                },
            },
            'mediator': {
                'animator': {
                    'placeholder': 'id_animator',
                    'name_field': 'name',
                    'dependency': [{
                        'source_form_element': 'village',
                        'dep_attr': 'assigned_villages'
                    }]
                }
            },
            'group': {
                farmer_groups_targeted: {
                    'placeholder': 'id_group',
                    'name_field': 'group_name',
                    'dependency': [{
                        'source_form_element': 'village',
                        'dep_attr': 'village'
                    }]
                }
            },
            'person': {
                person: {
                    'placeholder': 'id_person',
                    'name_field': 'person_name',
                    'name_field_father_name':'father_name',
                    'name_field_extra_info':'group',
                    'name_field_group_name':'group_name',
                    'name_field_person_id':'online_id',

                    'dependency': [{
                        'source_form_element': 'village',
                        'dep_attr': 'village'
                    }],
                },
                farmers_attendance: {
                    dependency: [{
                        'source_form_element': 'farmer_groups_targeted',
                        'dep_attr': 'group'
                    }, {
                        'source_form_element': 'person',
                        'dep_attr': 'id'
                    }],
                    id_field: "person_id", // for convert_namespace conversion      
                    'expanded': { // won't be denormalised, wud be converted offline to online, render wud use a template declared and nt options template, any field to be denormalised or converted offline to online can be declared - this shd be clubbed and put as foreign entity of expanded.  
                        template: 'person_pma_template',
                        placeholder: 'pmas',
                        denormalize: { // any field in expanded template to be denormalised     
                            "expressed_adoption_video": {
                                name_field: 'title'
                            }
                        },
                        foreign_entities: { // any more field in expanded template for offline to online conv
                            video:{
                                "expressed_adoption_video": {
                                    entity_name: "video",
                                    name_field: 'title'
                                }
                            }
                        },
                        extra_fields: ["expressed_question", "interested", "expressed_adoption_video"]
                    }
                }
            }
        },
        'form_field_validation': {
            ignore: [],
            rules: {
                date: {
                    required: true,
                    validateDate: true,
                },
                start_time: {
                    required: true,
                    validateTime: true
                },
                animator: "required",
                village: "required",
                videoes_screened: "required",
                farmer_groups_targeted: "required"

            },
            messages: {
				date: {
					required: 'Screening date is required',
					validateDate: 'Enter screening date in the form of YYYY-MM-DD',
				},
				start_time: {
					required: 'Screening start time is required',
					validateTime: 'Enter the start time in the form of HH:MM. Use 24 hour format',
				},
				animator: "Mediator is required",
				village:"Village is required",
				videoes_screened:"Videos screened is required",
				farmer_groups_targeted: "Groups attended is required"
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
    };

    var adoption_configs = {
        'page_header': 'Adoption',
        'config_English': 'Adoptions',
        'config_हिन्दी': 'अडॉप्षन्स',
        'labels_हिन्दी': {adoption:"अडॉप्षन्", village: "Village", mediator: "Mediator", video: "Video", groups_attended: "Groups Attended", person: "Person", del: "Delete", sr_no: "Sr. No.", video:"Video", date_of_adoption: "तिथि", date_of_verification: "Date of Verification"},
        'labels_English': {adoption:"Adoption", village: "Village", mediator: "Mediator", video: "Video", groups_attended: "Groups Attended", person: "Person", del: "Delete", sr_no: "Sr. No.", video: "Video", date_of_adoption: "Date of Adoption", date_of_verification: "Date of Verification"},
        'list_elements_हिन्दी': [{'header':'आइडी','element':'online_id'},{'header':'अडॉप्षन डटे','element':'date_of_adoption'},{'header':'पर्सन आइडी','element':'person.online_id'},{'header':'पर्सन','element':'person.person_name'},{'header':'ग्रूप','element':'group.group_name'},{'header':'विलेज','element':'village.village_name'},{'header':'वीडियो','element':'video.title'}],
        'list_elements_English': [{'header':'ID','element':'online_id'},{'header':'Adoption Date','element':'date_of_adoption'},{'header':'Person ID','element':'person.online_id'},{'header':'Person','element':'person.person_name'},{'header':'Group','element':'group.group_name'},{'header':'Village','element':'village.village_name'},{'header':'Video','element':'video.title'}],
        'add_template_name': 'adoption_add_template',
        'edit_template_name': 'adoption_edit_template',
        'rest_api_url': '/coco/api/v2/adoption/',
        'entity_name': 'adoption',
        'inc_table_name': 'personadoptpractice',
        'unique_together_fields': ['person.id', 'video.id', 'date_of_adoption'],
        form_field_validation: {
            ignore: [],
			rules: {
                person: {
                    required: true,
                    
                },
                video: {
                    required: true,                    
                },
                animator: {
                    required: true,
                },                
                date_of_adoption: {
                    required: true,
					validateDate: true,
                }
            },
            messages: {
				person: {
					required: "person is required"
				},
				video: {
					required: "video is required"
				},
                animator: {
                    required: "Mediator is required"
                },
				date_of_adoption: {
					required: "Date of Adoption is required"
				}
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
            errorClass: "help-block red-color",
            errorPlacement: function(label, element) {
                element.parent().append(label);
            },
            display: "block"
        },
        add: {
            'foreign_entities': {
                'village': {
                    'village': {
                        'placeholder': 'id_village',
                        'name_field': 'village_name'
                    },
                },
                'video':{
                    'video':{
                        'placeholder': 'id_video',
                        'name_field': 'title'
                    },
                },
                'group': {
                    'group': {
                        'placeholder': 'id_group',
                        'name_field': 'group_name',
                        'dependency': [{
                            'source_form_element': 'village',
                            'dep_attr': 'village'
                        }]
                    }
                },
                'mediator': {
                    'animator': {
                        'placeholder': 'id_animator',
                        'name_field': 'name',
                        'dependency': [{
                            'source_form_element': 'village',
                            'dep_attr': 'assigned_villages'
                        }]
                    }
                },
                'person': {
                    float_person: {
                        'placeholder': 'id_person',
                        'name_field': 'person_name',
                        'name_field_father_name':'father_name',
                        'name_field_extra_info':'group',
                        'name_field_group_name':'group_name',
                        'name_field_person_id':'online_id',
                        'dependency': [{
                            'source_form_element': 'village',
                            'dep_attr': 'village'
                        }],
                    },
                    farmers_attendance: {
                        dependency: [{
                            'source_form_element': 'group',
                            'dep_attr': 'group'
                        }, {
                            'source_form_element': 'float_person',
                            'dep_attr': 'id'
                        }],
                        filter_dependency: [{
                            'source_form_element':'video',
                            'dep_attr':'videos_seen'
                        }],
                        id_field: "person_id", // for convert_namespace conversion      
                        'expanded': { // won't be denormalised, wud be converted offline to online, render wud use a template declared and nt options template, any field to be denormalised or converted offline to online can be declared - this shd be clubbed and put as foreign entity of expanded.  
                            template: 'adoption_inline',
                            placeholder: 'bulk'
                        },
                    }
                }
            },
            'bulk': {
                foreign_fields: { //foreign fields in the individual objects
                    "video": {
                        video: {
                            'name_field': 'title'
                        }
                    },
                    "person": {
                        person: {
                            'name_field': 'person_name'
                        }
                    },
                    village: {
                        village:{
                            'name_field': 'village_name'
                        }
                    },
                    group: {
                        group:{
                            'name_field': 'group_name'
                        }
                    },
                    mediator: {
                        animator: {
                            'name_field': 'name'
                        }
                    },
                },
                borrow_fields: ['village', 'group','video','animator']
            }
        },
        edit: {
            'foreign_entities': {
                'person': {
                    'person': {
                        'placeholder': 'id_person',
                        'name_field': 'person_name'
                    },
                },
                'video': {
                    'video': {
                        'placeholder': 'id_video',
                        // 'sub_attr': 'videos_seen',
                        'name_field': 'title',
                        'dependency': [{
                            'source_form_element': 'person',
                            'dep_attr': 'id',
                            'src_attr': 'videos_seen',
                        }]
                    }
                },
                'mediator': {
                    'animator': {
                        'placeholder': 'id_animator',
                        'name_field': 'name',
                        'dependency': [{
                            'source_form_element': 'village',
                            'dep_attr': 'assigned_villages'
                        }] 
                    }
                }
            }
        }

    };

    var person_configs = {
        'page_header': 'Person',
        'config_English': 'Persons',
        'config_हिन्दी': 'पर्सन्स',
        'labels_हिन्दी': {person:"पर्सन", name:"नाम", father_name:"पिता का नाम", village: "विलेज", gender:"जेंडर", age:"उम्र", phone_no:"नंबर",group:"ग्रूप"},
        'labels_English': {person: "Person", name:"Name", father_name:"Father Name", village: "Village", gender:"Gender", age:"Age", phone_no:"Phone Number",group:"Group"},
        'list_elements_हिन्दी': [{'header':'आइडी','element':'online_id'},{'header':'पर्सन नेम','element':'person_name'},{'header':'फादर नेम','element':'father_name'},{'header':'विलेज','element':'village.village_name'},{'header':'ग्रूप','element':'group.group_name'}],
        'list_elements_English': [{'header':'ID','element':'online_id'},{'element':'person_name'},{'element':'father_name'},{'element':'village.village_name'},{'element':'group.group_name'}],
        'add_template_name': 'person_add_edit_template',
        'edit_template_name': 'person_add_edit_template',
        'rest_api_url': '/coco/api/v2/person/',
        'entity_name': 'person',
        'foreign_entities': {
            'village': {
                'village': {
                    'placeholder': 'id_village',
                    'name_field': 'village_name'
                },
            },
            'group': {
                'group': {
                    'placeholder': 'id_group',
                    'name_field': 'group_name',
					'dependency': [{
                        'source_form_element': 'village',
                        'dep_attr': 'village'
                    }]
                }
            }
        },
        'unique_together_fields': ['person_name', 'father_name', 'village.id'],
        'sort_field': 'person_name',
        'form_field_validation': {
            ignore: [],
            rules: {
                person_name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    // allowedChar:true
                },

                father_name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    // allowedChar:true
                },
                age: {
                    digits: true,
                    min: 1,
                    max: 100
                },
                gender: "required",
                phone_no: {
                    digits: true,
                    maxlength: 10
                },
                village: {
                    required: true
                }
            },
            messages: {
				person_name: {
					required: 'Person name is required',
					minlength: 'Person name  should contain at least 2 characters',
					maxlength: 'Person Name should contain at most 100 characters',
					allowedChar: 'Person name should contain only english and local language characters'
				},
				father_name: {
					required: "Father's name is required",
					minlength: "Father's name should contain at least 2 characters",
					maxlength: "Father's name should contain at most 100 characters",
					allowedChar: "Father's name should contain only english and local language characters"
				},
				age: {
					digits: "Age should contain only digits",
					min:"Age should not be less than 1 year",
					max:"Age should not be more than 100 years"
				},
				gender:{
					required: "Gender is required"
				},
				phone_number_person: {
					digits: 'Phone number should contain digits only',
					maxlength: "Phone number should not contain more than 10 digits"
				},
				village: {
					required: "Village is required"
				}
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

    };

    var misc = {
        download_chunk_size: 2000,
        languages: ['हिन्दी', 'English'],
        meta_default: 'English',
        meta_English: {stop: "Stop",close:"close", sync: "Sync", save: "Save and Add Another", help:"Help", logout:"Logout", download:"Downloading...",upload:"Uploading...", inprogress:"In Progress", done:"Done", edit:"Edit", 
                       delete_download:"Delete and Download Database", save_again:"Save Again", discard:"Discard", upload_total:"Data items to be uploaded", upload_done:"Data Uploaded", upload_pending:"Data pending to be uploaded",
                       error:"Error", upload_error:"Internet connectivity lost. Please try after sometime!"},
        meta_हिन्दी: {stop: "रोकें",close:"बंद करे", sync:"सिंक", save: "सवे करें", help:"हेल्प", logout:"लोगौट", download:"डाउनलोडिंग...", upload:"अपलोडिंग...",inprogress:"इन प्रोग्रेस", done:"समाप्त", edit:"एडिट",
                       delete_download:"डिलीट एंड डाउनलोड डेटबेस", save_again:"सेव अगेन", discard:"डिसकार्ड", upload_total:"कुल डेटा अपलोडिंग के लिए", upload_done:"डेटा अपलोडेड", upload_pending:"डेटा अपूर्ण",
                       error: "त्रुटि", upload_error:"इंटरनेट कनेक्टिविटी खो दिया है। कृपया कुछ देर बाद प्रयास करें!"},
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
        village: village_configs,
        mediator: mediator_configs,
        video: video_configs,
        group: group_configs,
        person: person_configs,
        screening: screening_configs,
        adoption: adoption_configs,
        language: language_configs,
        category: category_configs,
        subcategory: subcategory_configs,
        videopractice: videopractice_configs,
        district: district_configs,
        nonnegotiable: nonnegotiable_configs,
        misc: misc
    }

});
