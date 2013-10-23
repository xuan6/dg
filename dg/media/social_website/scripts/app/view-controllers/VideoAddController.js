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
    //var FeaturedCollectionDataFeed = require('app/libs/FeaturedCollectionDataFeed');
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
            
            this._dropdownChosen();
            
            
            return this;
        },

        _initReferences: function($referenceBase) {
            this.base();
            
            var references = this._references;
            
//            references.dataFeed = new FeaturedCollectionDataFeed($language);
            
            references.$videoAddWrapper = $referenceBase;
            references.$videoAddContainer = $referenceBase.find('.js-video-add-container');
            references.$videoAddMoreButton = $referenceBase.find('.js-add-more-videos-btn');
            references.$dropZone = $referenceBase.find('#video-dropzone');
            this._renderVideoFormItems()
            references.resumable = new Resumable({
          	  										target:'/social/api/postvideo/',
          	  										//testChunks:false,
          	  										simultaneousUploads:1,
          	  										query:{
          	  											upload_token:'my_token'
        		  
          	  										}
        										});
            references.resumable.assignBrowse(document.getElementById('browseButton'));
            references.resumable.assignDrop(document.getElementById('video-dropzone'));
        },

        _initEvents: function() {
            this.base();
            
            var boundFunctions = this._boundFunctions;
            var references = this._references;
            
            /*boundFunctions.onDataProcessed = this._onDataProcessed.bind(this);
            references.dataFeed.on('dataProcessed', boundFunctions.onDataProcessed);*/
            
            /*// input param changed alert from data feed
            boundFunctions.onInputParamChanged = this._onInputParamChanged.bind(this);
            references.dataFeed.on('inputParamChanged', boundFunctions.onInputParamChanged)*/
            
            //adding another video form
            boundFunctions.onAddMoreVideoFormClick = this._onAddMoreVideoFormClick.bind(this);
            references.$videoAddMoreButton.on("click", boundFunctions.onAddMoreVideoFormClick);
            
            boundFunctions.onFileAdded = this._onFileAdded.bind(this);
            references.resumable.on('fileAdded', boundFunctions.onFileAdded);
        },

        _dropdownChosen: function(){
            $(".chosen-select").chosen({no_results_text: "No results match", width: "90%"});
        },

        _onDataProcessed: function() {
            
        },

        _renderVideoFormItems: function() {

            viewRenderer.renderAppend(this._references.$videoAddContainer, videoFormTemplate);
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
        	alert(file.fileName);
        	//sending the first post query to make an entry
        	$.post( '/social/api/postvideo/', { 
        		file: file.fileName,
        		num_chunks: file.chunks.length,
        		make_entry: 1});
        		/*alert("posting")
        	  .done(function( data ) {
        	    alert( "Data Loaded: " + data );
        	  });*/
        },

        _onAddMoreVideoFormClick: function(event){
            event.preventDefault();
            event.stopPropagation();
            this._renderVideoFormItems();
            this._dropdownChosen();
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
