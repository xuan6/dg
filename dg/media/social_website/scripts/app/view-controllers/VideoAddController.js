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
    var CollectionDropDownDataFeed = require('app/libs/CollectionDropDownDataFeed');
    var videoFormTemplate = require('text!app/views/video-add-form.html');
    
    var Chosen = require('libs/external/chosen.jquery.min')
    var draggable = require('libs/external/jquery-ui');
    require('libs/external/resumable');

    var VideoAddController = Controller.extend({

        /**
         * Controller constructor
         * @return {Controller} this
         */
        constructor: function($referenceBase) {
            this.base($referenceBase);
            this.getDropDown();
            
            
            
            return this;
        },

        _initReferences: function($referenceBase) {
            this.base();
            
            var references = this._references;
            
//            references.dataFeed = new FeaturedCollectionDataFeed($language);
            
            references.$videoAddWrapper = $referenceBase;
            references.$videoAddContainer = $referenceBase.find('.js-video-add-container');
            references.$videoAddMoreButton = $referenceBase.find('.js-add-more-videos-btn');
            references.$uploadButton = $referenceBase.find('.js-upload-video-btn');
            references.dataFeed = new CollectionDropDownDataFeed();
            
            
            references.resumable = new Resumable({
          	  										target:'/social/api/postvideo/',
          	  										//testChunks:false,
          	  										simultaneousUploads:4,
          	  										query:{
          	  											upload_token:'my_token'
        		  
          	  										}
        										});
            
        },

        _initEvents: function() {
            this.base();
            
            var boundFunctions = this._boundFunctions;
            var references = this._references;
            
            boundFunctions.onDataProcessed = this._onDataProcessed.bind(this);
            references.dataFeed.on('dataProcessed', boundFunctions.onDataProcessed);
            
            /*// input param changed alert from data feed
            boundFunctions.onInputParamChanged = this._onInputParamChanged.bind(this);
            references.dataFeed.on('inputParamChanged', boundFunctions.onInputParamChanged)*/
            
            //adding another video form
            boundFunctions.onAddMoreVideoFormClick = this._onAddMoreVideoFormClick.bind(this);
            references.$videoAddMoreButton.on("click", boundFunctions.onAddMoreVideoFormClick);
            
            boundFunctions.onUploadVideoClick = this._onUploadVideoClick.bind(this);
            references.$uploadButton.on("click", boundFunctions.onUploadVideoClick);
            
            boundFunctions.onFileAdded = this._onFileAdded.bind(this);
            references.resumable.on('fileAdded', boundFunctions.onFileAdded);
            
            boundFunctions.fileProgress = this._fileProgress.bind(this);
            references.resumable.on('fileProgress', boundFunctions.fileProgress);
        	
            boundFunctions.onFileSuccess = this._onFileSuccess.bind(this);
            references.resumable.on('fileSuccess', boundFunctions.onFileSuccess);
            
            
        },

        _dropdownChosen: function(){
            $(".chosen-select").chosen({no_results_text: "No results match", width: "90%"});
        },
        
        getDropDown: function() {
            var dropdownData = this._references.dataFeed.getCollectionDropDown();
            if (dropdownData == false) {
                return false;
            }
            this._renderVideoFormItems(dropdownData);
            this._dropdownChosen();
            this._references.resumable.assignBrowse(document.getElementById('addButton'));
            this._references.resumable.assignDrop(document.getElementById('video-dropzone'));
        },

        _onDataProcessed: function() {
            this.getDropDown();
        },

        /*_renderCollectionDropDown: function(collectiondropdownData) {
            var renderedCollectionDropDown = viewRenderer.render(collectionDropDownTemplate, collectiondropdownData);
            this._references.$collectionDropDownContainer.html(renderedCollectionDropDown);
            this._dropdownChosen();
        },*/


        _renderVideoFormItems: function(dropdownData) {

            viewRenderer.renderAppend(this._references.$videoAddContainer, videoFormTemplate, dropdownData);
            /*var r = new Resumable({
            	  target:'/social/api/postvideo/',
            	  //testChunks:false,
            	  simultaneousUploads:1,
            	  query:{
            		  upload_token:'my_token'
            		  
            	  }
            	});
            r.assignBrowse(document.getElementById('browseButton'));
            r.assignDrop(document.getElementById('video-dropzone'));
            r.on('fileAdded', function(file){
            	alert("file added");
            	
            	
                r.upload();
              });
            
            r.on('fileSuccess', function(file,message){
                alert(message)
              });*/

        },
        
        _onFileAdded: function(file){      
            $('#video-innerwrapper').hide();
            document.getElementById('fileInfo').innerHTML=file.fileName;
            $('#progressbar').show();
            this._references.file = file;
        	
        		/*alert("posting")
        	  .done(function( data ) {
        	    alert( "Data Loaded: " + data );
        	  });*/
        },
        
        _fileProgress: function(file){
            var progress = Math.floor(file.progress() * 100);
            $("#progressbar-inner").css({"width": progress});
            //alert('Progress :' + progress)
            console.log(progress);
        },
        
        _onFileSuccess: function(file, message){
        	alert(message);
        	$.post( '/social/api/postvideo/', { 
        		file: file.fileName,
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
        
        _onUploadVideoClick: function(event){
        	var references = this._references
        	var video_title = $('#video_title').val();
        	var video_desc = $('#video_desc').val();
        	var state = $('#statelist').val();
        	var partner = $('#partnerlist').val();
        	var language = $('#langlist').val();
        	var date = $('#date').val();
            if (video_title == "" || state == "" || partner == "" || language == "" || video_desc == "") {
                throw new Error('ViewCollectionsController._onCommentButtonClick: Video Title is required parameter');
            }

            //sending the first post query to make an entry
        	$.post( '/social/api/postvideo/', { 
        		file: this._references.file.fileName,
        		num_chunks: this._references.file.chunks.length,
        		make_entry: 1,
        		video_title: video_title,
        		video_desc: video_desc,
        		state: state,
        		partner: partner,
        		language: language,
        		date: date})
        		
        		.done(function( data ) {
        		    if (data==1){
        		    	alert("File with this name already uploaded")
        		    }
        		    else{
        		    	references.resumable.upload();
        		    }
        		    
        		  });
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
