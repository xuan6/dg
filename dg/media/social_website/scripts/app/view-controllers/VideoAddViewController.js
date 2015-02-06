/**
 * VideoAddController Class File
 *
 * @author aadish
 * @version $Id$
 * @requires require.js
 * @requires jQuery
 */

define(function(require) {
    'use strict';

    var Controller = require('framework/controllers/Controller');
    var viewRenderer = require('framework/ViewRenderer');
    var jQuery = require('jquery');
    var Select2 = require('libs/external/select2');
    
    var draggable = require('libs/external/jquery-ui');
    require('libs/external/resumable');
    
    var PracticeMappingDataFeed = require('app/libs/PracticeMappingDataFeed');
    var CollectionVideoDropDownDataFeed = require('app/libs/CollectionVideoDropDownDataFeed');
    var practiceMappingTemplate = require('text!app/views/practice-mapping.html');
    var collectionVideoDropDownTemplate = require('text!app/views/collection-add-video-dropdown.html');

    var VideoAddController = Controller.extend({

        /**
         * Controller constructor
         * @return {Controller} this
         */
        constructor: function($referenceBase) {
            this.base($referenceBase);
            this.getPracticeMapping();
            this.initSelect2();
            return this;
        },

        _initReferences: function($referenceBase) {
            this.base();
            
            var references = this._references;

            references.$videoAddWrapper = $referenceBase;
            references.$videoAddContainer = $referenceBase.find('.js-video-add-container');
            references.$practiceMappingContainer = $referenceBase.find('.js-collection-mapping-container');
            references.$videoDropDownContainer = $referenceBase.find('.js-collection-video-dropdown-container');
            references.$videoAddMoreButton = $referenceBase.find('.js-add-more-videos-btn');
            references.$uploadButton = $referenceBase.find('.js-upload-video-btn');
            references.$dropDown = $referenceBase.find('.js-video-criteria');
            references.$partnerList = $referenceBase.find('.js-partnerlist');
            references.$stateList = $referenceBase.find('.js-statelist');
            references.$langList = $referenceBase.find('.js-langlist');
            references.dataFeed = new PracticeMappingDataFeed();
            references.videodataFeed = new CollectionVideoDropDownDataFeed('/jcndj/djcdn/');
            
            references.resumable = new Resumable({
          	  										target:'/social/api/postvideo/',
          	  										//testChunks:false,
          	  										simultaneousUploads:4,
          	  										query:{
          	  											upload_token:'my_token'
        		  
          	  										}
        										});
            references.$saveButton = jQuery('.js-save-video-btn');
            references.resumable.assignBrowse(document.getElementById('addButton'));
            references.resumable.assignDrop(document.getElementById('video-dropzone'));
        },

        _initEvents: function() {
            this.base();
            
            var boundFunctions = this._boundFunctions;
            var references = this._references;
            
            boundFunctions.onDataProcessed = this._onDataProcessed.bind(this);
            references.dataFeed.on('dataProcessed', boundFunctions.onDataProcessed);
            
            boundFunctions.onVideoDataProcessed = this._onVideoDataProcessed.bind(this);
            references.videodataFeed.on('dataProcessed', boundFunctions.onVideoDataProcessed);

            //adding another video form
            boundFunctions.onAddMoreVideoFormClick = this._onAddMoreVideoFormClick.bind(this);
            references.$videoAddMoreButton.on("click", boundFunctions.onAddMoreVideoFormClick);
            
            boundFunctions.onUploadVideoClick = this._onUploadVideoClick.bind(this);
            references.$uploadButton.on("click", boundFunctions.onUploadVideoClick);
            
            boundFunctions.onSaveVideoClick = this._onSaveVideoClick.bind(this);
            references.$saveButton.on("click", boundFunctions.onSaveVideoClick);
            
            boundFunctions.onFileAdded = this._onFileAdded.bind(this);
            references.resumable.on('fileAdded', boundFunctions.onFileAdded);
            
            boundFunctions.fileProgress = this._fileProgress.bind(this);
            references.resumable.on('fileProgress', boundFunctions.fileProgress);
        	
            boundFunctions.onFileSuccess = this._onFileSuccess.bind(this);
            references.resumable.on('fileSuccess', boundFunctions.onFileSuccess);
            
            this._boundFunctions.onDropDownChosen = this._onDropDownChosen.bind(this);
            references.$dropDown.on('change', this._boundFunctions.onDropDownChosen);
            
            
        },

        _dropdownChosen: function(){
            $(".chosen-select").chosen({no_results_text: "No results match", width: "90%"});
        },
        
        selectCollectionMapping: function(){
            var references = this._references;
            if (references.$collectionUid && references.$practiceMappingContainer.data('category').trim()){
                references.$catList.val(references.$practiceMappingContainer.data('category').trim()).change();
                references.$subCatList.val(references.$practiceMappingContainer.data('subcategory').trim()).change();
                references.$topicList.val(references.$practiceMappingContainer.data('topic').trim()).change();
                references.$subTopicList.val(references.$practiceMappingContainer.data('subtopic').trim());
                references.$subjectList.val(references.$practiceMappingContainer.data('subject').trim());
            }
        },
        
        getPracticeMapping: function() {
            var practicemappingData = this._references.dataFeed.getPracticeMapping();
            if (practicemappingData == false) {
                return false;
            }
            this._references.mapping = practicemappingData;
            this._renderPracticeMapping(practicemappingData);
            
            this.selectCollectionMapping();
            this.initSelect2();
        },

        _onDataProcessed: function() {
            this.getPracticeMapping();
        },
        
        _onVideoDataProcessed: function() {
            this.getCollectionVideoDropDown();
        },

        _renderVideoFormItems: function(dropdownData) {
            viewRenderer.renderAppend(this._references.$videoAddContainer, videoFormTemplate, dropdownData);
        },
        
        _renderPracticeMapping: function(practicemappingData) {
            var references = this._references;
            var category = [];
            var arr;
            for (arr in practicemappingData){
                category.push(arr);
            }
            var renderData = {
                    category: category.sort()
                };
            var renderedPracticeMapping = viewRenderer.render(practiceMappingTemplate, renderData);
            this._references.$practiceMappingContainer.html(renderedPracticeMapping);
            this._references.category = category.sort();
            
            references.$catList = jQuery('.js-catlist');
            references.$subCatList = jQuery('.js-subcatlist');
            references.$topicList = jQuery('.js-topiclist');
            references.$subTopicList = jQuery('.js-subtopiclist');
            references.$subjectList = jQuery('.js-subjectlist');
            
            this._boundFunctions.onCategoryChosen = this._onCategoryChosen.bind(this);
            references.$catList.on('change', this._boundFunctions.onCategoryChosen);
            
            this._boundFunctions.onsubCategoryChosen = this._onsubCategoryChosen.bind(this);
            references.$subCatList.on('change', this._boundFunctions.onsubCategoryChosen);
            
            this._boundFunctions.onTopicChosen = this._onTopicChosen.bind(this);
            references.$topicList.on('change', this._boundFunctions.onTopicChosen);
        },
        
        _renderVideoCollectionDropDown: function(collectionvideodropdownData) {
            var references = this._references;
            
            var renderData = {
                     video: collectionvideodropdownData
            };
            
            var renderedCollectionVideoDropDown = viewRenderer.render(collectionVideoDropDownTemplate, renderData);
            
            references.$videoDropDownContainer.html(renderedCollectionVideoDropDown);
            
            references.$vidList = jQuery('.js-vidlist')
            
            //this._boundFunctions.onVideoChosen = this._onVideoChosen.bind(this);
            //references.$vidList.on('change', this._boundFunctions.onVideoChosen);
            
            this.initSelect2();
        },
        
        initSelect2: function(){
            var references = this._references;
            try{
                $(".chosen-select").select2({no_results_text: "No results match", width: "90%"});
               }
            catch(err){
                $("select.chosen-select").select2({no_results_text: "No results match", width: "90%"});
            }
            
        },
        
        _onDropDownChosen: function(){
            var references = this._references;
            
            if( references.$partnerList.val()!="" && references.$stateList.val()!="" && references.$langList.val()!=""){
                references.videodataFeed.addInputParam('limit', false, 0);
                references.videodataFeed.setInputParam('limit', 0, false);
                references.videodataFeed.addInputParam('state', false, references.$stateList.val());
                references.videodataFeed.setInputParam('state', references.$stateList.val(), false);
                references.videodataFeed.addInputParam('partner', false, references.$partnerList.val());
                references.videodataFeed.setInputParam('partner', references.$partnerList.val(), false);
                references.videodataFeed.addInputParam('language', false, references.$langList.val());
                references.videodataFeed.setInputParam('language', references.$langList.val(), false);
                this.getCollectionVideoDropDown();
            }
            else{
            //TODO: What happens if value becomes default again
            }
        },
        
        _onCategoryChosen: function(){
            var references = this._references;
            var category_name = references.$catList.val();
            
            var mapping_data = this._references.mapping;
            
            references.$subCatList.find('option:not(:first)').remove();
            references.$topicList.find('option:not(:first)').remove();
            references.$subTopicList.find('option:not(:first)').remove();
            references.$subjectList.find('option:not(:first)').remove();
            
            var subcategory = mapping_data[category_name]
            var arr;
            for (arr in subcategory){
                if (arr != 'subject'){
                    references.$subCatList.append(new Option(arr,arr));
                }
            }
            
            var subject = (mapping_data[category_name]['subject']).sort();
            var i;
            for (i in subject){
                references.$subjectList.append(new Option(subject[i],subject[i]));
            }
            
            this.initSelect2();

        },
        
        _onsubCategoryChosen: function(){
            var references = this._references;
            
            var category_name = references.$catList.val();
            var subcategory_name = references.$subCatList.val();
            var mapping_data = references.mapping;
            
            references.$topicList.find('option:not(:first)').remove();
            references.$subTopicList.find('option:not(:first)').remove();
            
            var topic=[];
            var arr;
            for (arr in mapping_data[category_name][subcategory_name]){
                topic.push(arr);
                references.$topicList.append(new Option(arr,arr));
            }
            this.initSelect2();
        },
        
        _onTopicChosen: function(){
            var references = this._references;
            
            var category_name = references.$catList.val();
            var subcategory_name = references.$subCatList.val();
            var topic_name = references.$topicList.val();
            var mapping_data = references.mapping;
            
            var subtopic=mapping_data[category_name][subcategory_name][topic_name];
            subtopic=subtopic.sort()
            
            references.$subTopicList.find('option:not(:first)').remove();
            
            var i;
            for (i in subtopic){
                references.$subTopicList.append(new Option(subtopic[i],subtopic[i]));
            }
            this.initSelect2();
        },
        
        _onFileAdded: function(file){      
            $('#video-innerwrapper').hide();
            document.getElementById('fileInfo').innerHTML=file.fileName;
            $('#progressbar').show();
            $('#video-btns').show();
        	var references = this._references
            $( "#v-pause" ).click(function() {
                if ($("#v-pause").html() == "Pause"){
                    references.resumable.pause();
                    $("#v-pause").html("Resume");
                }
                else if ($("#v-pause").html() == "Resume"){
                    references.resumable.upload();
                	//file.retry()
                    $("#v-pause").html("Pause");
                }
            });
            
            $( "#v-cancel" ).click(function() {
                var conf = confirm("Are you sure you want to cancel upload?");
                if (conf == true){
                    references.resumable.removeFile(file);
                    $("#progressbar-inner").css({"width": "0"});
                    $("#progress-percent").text("Upload cancelled");
                }
            });
            
            this._references.file = file;
            this._onUploadVideoClick();
        },
        
        _fileProgress: function(file){
            var progress = (Math.floor(file.progress() * 100))*3;
            $("#progressbar-inner").css({"width": progress});
            $("#progress-percent").text(progress/3 + "%")
        },
        
        _onFileSuccess: function(file, message){
        	alert(message);
        	$.post( '/social/api/postvideo/', { 
        		fileidentifier: file.uniqueIdentifier,
        		combine: 1})
        		
        		.done(function( data ) {
        		    alert(data);
        		  });
        },

        _onAddMoreVideoFormClick: function(event){
            //event.preventDefault();
            //event.stopPropagation();
            this.getDropDown();
        },
        
        _onSaveVideoClick: function(event){
        	var references = this._references
        	var video_title = $('#video_title').val();
        	var video_desc = $('#video_desc').val();
        	var state = $('#statelist').val();
        	var partner = $('#partnerlist').val();
        	var language = $('#langlist').val();
        	var date = $('#date').val();
            /*if (video_title == "" || state == "" || partner == "" || language == "" || video_desc == "") {
                throw new Error('ViewCollectionsController._onCommentButtonClick: Video Title is required parameter');
            }*/
        	
        	$.post( '/social/api/postvideo/', { 
        		fileidentifier: this._references.file.uniqueIdentifier,
        		save: 1,
        		video_title: video_title,
        		video_desc: video_desc,
        		state: state,
        		partner: partner,
        		language: language,
        		date: date})
        		
        		.done(function( data ) {
        		    alert("file associated data saved");
        		    
        		  });
        },
        _onUploadVideoClick: function(event){
        	var references = this._references
        	

            //sending the first post query to make an entry
        	$.post( '/social/api/postvideo/', { 
        		fileidentifier: this._references.file.uniqueIdentifier,
        		filename: this._references.file.fileName,
        		num_chunks: this._references.file.chunks.length,
        		make_entry: 1})
        		
        		.done(function( data ) {
        		    if (data==1){
        		    	alert("File with this name already uploaded")
        		    }
        		    else{
        		    	references.resumable.upload();
        		    }
        		    
        		  });
        },
        
        getCollectionVideoDropDown: function() {
            var references = this._references
            var collectionvideodropdownData = references.videodataFeed.getCollectionVideoDropDown();
            if (collectionvideodropdownData == false) {
                return false;
            }
            references.videoArray = collectionvideodropdownData;
            this._renderVideoCollectionDropDown(collectionvideodropdownData);
            
            references.$partnerList.prop("disabled", true);
            references.$stateList.prop("disabled", true);
            references.$langList.prop("disabled", true);
            
            if (references.$collectionUid){
            var videos_collection = references.$videoDropDownContainer.data('videos');
            var a;
            for (a in videos_collection){
                console.log(videos_collection[a]);
                references.$vidList.val(videos_collection[a]).change();
            }
            
            }
            
        },
        
        setInputParam: function(key, value, disableCacheClearing) {
            this._references.dataFeed.setInputParam(key, value, disableCacheClearing);
        },

        _onInputParamChanged: function() {
            this.getFeaturedCollection();
        },
        /**
         * Controller destructor
         * @return {void}
         */
        destroy: function() {
            this.base();

            // TODO: clean up
        }
    });

    return VideoAddController;
});
