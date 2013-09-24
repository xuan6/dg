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
    var Chosen = require('libs/external/chosen.jquery.min');
    var Dropzone = require('libs/external/dropzone-amd-module');
    
    var VideoAddController = Controller.extend({

        /**
         * Controller constructor
         * @return {Controller} this
         */
        constructor: function($referenceBase) {
            this.base($referenceBase);
            this._renderVideoFormItems();
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
        },

        _dropdownChosen: function(){
            $(".chosen-select").chosen({no_results_text: "No results match", width: "90%"});
        },

        _onDataProcessed: function() {
            
        },

        _renderVideoFormItems: function() {

            viewRenderer.renderAppend(this._references.$videoAddContainer, videoFormTemplate);

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
