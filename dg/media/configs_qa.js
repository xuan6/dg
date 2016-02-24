define([],
function() {
	var VideoContentApproval_configs = {
		'page_header': 'Video Content Approval',
		'add_template_name': 'Video_Content_Approval_add_edit_template',
        'edit_template_name': 'Video_Content_Approval_add_edit_template',
        'rest_api_url': '/coco/api/v2/VideoContentApproval/',
        'list_elements': [{'header':'Video','element':'video'},{'header':'Reviewer','element':'reviewer'},{'header':'Comment','element':'comment'}],
        'entity_name': 'VideoContentApproval',
        'dashboard_display': {
            listing: true,
            add: true
        },
        'sort_field': 'video'
    };
    'form_field_validation': {
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

    };
