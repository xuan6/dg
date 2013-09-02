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
    var VideoAddController = require('app/controllers/VideoAddController')
    var jQuery = require('jquery');

    var CollectionsController = DigitalGreenPageController.extend({

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
            
         // filters changed
            boundFunctions.onFilterChanged = this._onFilterChanged.bind(this);
            references.collectionFiltersViewController.on('filterChanged', boundFunctions.onFilterChanged);

            // collections updated
            boundFunctions.onCollectionDataProcessed = this._onCollectionDataProcessed.bind(this);
            references.collectionViewController.on('collectionsUpdated', boundFunctions.onCollectionDataProcessed);

            // order changed
            boundFunctions.onOrderChanged = this._onOrderChanged.bind(this);
            references.collectionMostFiltersViewController.on('orderChanged', boundFunctions.onOrderChanged);

            // filters cleared
            boundFunctions.onFiltersCleared = this._onFiltersCleared.bind(this);
            references.collectionFiltersViewController.on('filtersCleared', boundFunctions.onFiltersCleared);
        },

        _onCollectionDataProcessed: function(broadcastData) {
            var set_filters = this._references.collectionFiltersViewController._references.dataFeed;
            var filter_object = this._references.collectionViewController._references.dataFeed._state.inputParams.filters.value;
            var facets = this._references.collectionViewController._references.dataFeed._dataModel._data.facets;
            if (filter_object){
                set_filters.addInputParam('filters', true, 0, true);
                set_filters.setInputParam('filters', filter_object, true);
            }
            set_filters.addInputParam('facets', true, 0, true);
            set_filters.setInputParam('facets', facets, true);
            this._references.collectionFiltersViewController._fetchFilters();
            this._references.collectionFiltersViewController.updateTotalCount(broadcastData.totalCount);
            // Only if data attributes are to be used, go inside this loop
            if (this._references.collectionFiltersViewController._references.filters_cleared == 0){
                if ($(".js-collections-wrapper").attr('data-partner') != 'None' ){
                    this._references.collectionFiltersViewController._setFilterStatus('partner', $(".js-collections-wrapper").attr('data-partner'), true);
                }
                if ($(".js-collections-wrapper").attr('data-title') != 'None'){
                    this._references.collectionFiltersViewController._setFilterStatus('topic', $(".js-collections-wrapper").attr('data-title'), true);
                    this._references.collectionFiltersViewController._setFilterStatus('subject', $(".js-collections-wrapper").attr('data-title'), true);
                }
                if ($(".js-collections-wrapper").attr('data-state') != 'None'){
                    this._references.collectionFiltersViewController._setFilterStatus('state', $(".js-collections-wrapper").attr('data-state'), true);
                }
            }
        },

        _onOrderChanged: function(orderCriteria) {
            this._references.collectionViewController.setInputParam('order_by', orderCriteria);
        },

        _onFilterChanged: function(filterParam, filterValue, active) {
            this._references.collectionViewController.setFilterStatus(filterParam, filterValue, active);
        },

        _onFiltersCleared: function() {
            this._references.collectionFiltersViewController._references.filters_cleared = 1; // remove usage of data-attributes
            this._references.collectionViewController._references.dataFeed.setInputParam('filters',0,true);
            this._references.collectionFiltersViewController._references.dataFeed.setInputParam('filters',0,true);
            this._references.collectionViewController._references.dataFeed.setInputParam('searchString','None');
            this._references.collectionViewController._references.dataFeed._fetch();
            this._references.collectionViewController.clearFilters();
            
        },

        _getCollections: function() {
            this._references.collectionViewController.getCollections();
        },

        /**
         * Controller destructor
         * @return {void}
         */
        destroy: function() {
            this.base();
        }
    });

    return CollectionsController;
});
