/**
 * CollectionsController Class File
 *
 * @author rdeluca
 * @version $Id$
 * @requires require.js
 * @requires jQuery
 */

define(function(require) {
    'use strict';

    var DigitalGreenPageController = require('app/controllers/DigitalGreenPageController');
    var VideoAddController = require('app/view-controllers/VideoAddController')
    var jQuery = require('jquery');

    var VideoController = DigitalGreenPageController.extend({

        /**
         * Controller constructor
         * @return {CollectionsController} this
         */
        constructor: function(bootstrapConfig, globalHelpers) {
            this.base(bootstrapConfig, globalHelpers);

            var references = this._references;
            return this;
        },

        _initReferences: function() {
            this.base();

            var references = this._references;
            
            var $videoWrapper = jQuery('.js-video-outer-wrapper');
            //var $filtersWrapper = jQuery('.js-filters-wrapper');

            // helpers
            var $languageCookie = -1
            references.videoAddController = new VideoAddController($videoWrapper);
            //references.collectionViewController = new CollectionViewController($collectionsContainer, $languageCookie);
            //references.collectionMostFiltersViewController = new CollectionMostFiltersViewController($collectionsContainer);
        },

        _initEvents: function() {
            this.base();

            var references = this._references;
            var boundFunctions = this._boundFunctions;
            
         
        },

        

        /**
         * Controller destructor
         * @return {void}
         */
        destroy: function() {
            this.base();
        }
    });

    return VideoController;
});
