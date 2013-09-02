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
    var featuredCollectionTemplate = require('text!app/views/video_add.html');

    var VideoAddController = Controller.extend({

        /**
         * Controller constructor
         * @return {Controller} this
         */
        constructor: function($referenceBase) {
            this.base($referenceBase);
            return this;
        },

        _initReferences: function($referenceBase) {
            this.base();
            
            var references = this._references;
            
            references.dataFeed = new FeaturedCollectionDataFeed($language);
            
            references.$featuredCollectionContainer = $referenceBase;
        },

        _initEvents: function() {
            this.base();
            
            var boundFunctions = this._boundFunctions;
            var references = this._references;
            
            boundFunctions.onDataProcessed = this._onDataProcessed.bind(this);
            references.dataFeed.on('dataProcessed', boundFunctions.onDataProcessed);
            
            // input param changed alert from data feed
            boundFunctions.onInputParamChanged = this._onInputParamChanged.bind(this);
            references.dataFeed.on('inputParamChanged', boundFunctions.onInputParamChanged)
        },

        getFeaturedCollection: function() {
            var featuredcollectionData = this._references.dataFeed.getFeaturedCollection();
            if (featuredcollectionData == false) {
                return false;
            }
            this._renderFeaturedCollection(featuredcollectionData);
        },

        _onDataProcessed: function() {
            this.getFeaturedCollection();
        },

        _renderFeaturedCollection: function(featuredcollectionData) {
            var renderedFeaturedCollection = viewRenderer.render(featuredCollectionTemplate, featuredcollectionData);
            this._references.$featuredCollectionContainer.html(renderedFeaturedCollection);
        },

        setInputParam: function(key, value, disableCacheClearing) {
            this._references.dataFeed.setInputParam(key, value, disableCacheClearing);
        },

        _onInputParamChanged: function() {
            this.getFeaturedCollection();
        },
        console.log("Nikita");
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
