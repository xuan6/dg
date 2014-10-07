define("app/libs/CollectionsDataFeed",["require","app/libs/DigitalGreenDataFeed","app/libs/DataModel","framework/Util"],function(e){var t=e("app/libs/DigitalGreenDataFeed"),n=e("app/libs/DataModel"),r=e("framework/Util"),i=t.extend({_filters:undefined,constructor:function(e){this.base("api/elasticSearch/"),this._filters={};var t=this._dataModel,n=t.addSubModel("collections",!0);this.addInputParam("searchString",!1,0,!0),this.addInputParam("offset",!0,0,!0),this.addInputParam("limit",!0,0,!0),this.addInputParam("filters",!1,null,!0,n),this.addInputParam("order_by",!1,null,!0,n),e!=-1&&this.addInputParamCacheClear("language__name",n)},fetch:function(e,t){e==undefined&&(e=0),t==undefined&&(t=12),this.setInputParam("offset",e*t,!0),this.setInputParam("limit",t,!0),this.base()},_processData:function(e){this.base(e);var t=this._dataModel,n=t.get("collections"),r=e.meta.limit,i=e.meta.offset/e.meta.limit;t.set("totalCount",e.meta.total_count);var s=e.objects,o=i*r,u=e.facets;return t.set("facets",e.facets),n.addSubset(s,o),s},setFilterStatus:function(e,t,n){var i=this._filters;i[e]==undefined&&(i[e]=[]);var s=i[e].indexOf(t),o=s!=-1;if(n&&o||!n&&!o)return!1;n?i[e].push(t):i[e].splice(s,1);var u=r.Object.clone(i);return this.setInputParam("filters",u),!0},clearFilters:function(){var e=!1,t=this._filters,n;for(n in t){var r=t[n],i=r.length;if(i>0){e=!0;break}}return this._filters={},e},getTotalCount:function(){return this._dataModel.get("totalCount")},getCollections:function(){var e=this.getInputParam("offset"),t=this.getInputParam("limit"),n=this._dataModel.get("collections").getSubset(e*t,t);return n?n:(this.fetch(e,t),!1)}});return i}),define("text!app/views/collection.html",[],function(){return'                            <li>\r\n                                <div class="vid-cat-selected">\r\n                                    <div class="vid-cat">\r\n                                        <a href={{url}}>\r\n                                            <img height=124  width=217  src="{{thumbnailURL}}" />\r\n                                        </a>\r\n                                        <div class="vid-flag">\r\n                                            <ul class="copy-sm copy-white h-list h-list-sm h-list-divided">\r\n                                                <li>{{videos.length}} Video{{#_plural}}s{{/_plural}}</li>\r\n                                                <li>{{_collectionStats.time}}</li>\r\n                                            </ul>\r\n                                        </div>\r\n                                        <div class="vid-cat-inner js-collection-item" data-collection-item-index="{{_index}}">\r\n                                            <div class="vid-cat-hd">\r\n                                                <h3 class="hdg-green hdg-f hdg-bold hdg-trunc">{{title}}</h3>\r\n                                            </div>\r\n                                            <div class="vid-cat-bd">\r\n                                                <p class="copy copy-sm layout-vr-tiny">{{state}} | {{language}}</p>\r\n                                                <p class="copy copy-sm">By: {{partner}}</p>\r\n                                            </div>\r\n                                            <div class="vid-cat-ft">\r\n                                                <ul class="h-list h-list-sm copy-sm copy-lt vid-cat-list">\r\n                                                    <li class="like"><span class="text-hide">Likes</span> {{_collectionStats.likes}}</li>\r\n                                                    <li class="view"><span class="text-hide">Viewed</span> {{_collectionStats.views}}</li>\r\n                                                    <li class="check"><span class="text-hide">Adopted</span> {{_collectionStats.adoptions}}</li>\r\n                                                </ul>\r\n                                            </div>\r\n                                        </div> <!-- End .vid-inner -->\r\n                                    </div> <!-- End .vid-cat -->\r\n                                </div>\r\n                            </li>'}),define("text!app/views/collection-video-drawer.html",[],function(){return'                        <li class="vidDrawer-wrapper {{_videoDrawerClasses}}">\r\n                            <div class="vidDrawer-container js-video-container">\r\n                                {{#_videoDrawers}}\r\n                                <div class="vidDrawer-wrapper-inner js-video-drawer" data-parent-collection-item-index="{{_index}}">\r\n                                    <div class="collection-video-carousel carousel-wrapper js-carousel-wrapper">\r\n                                        <div class="carousel-container js-carousel-container">\r\n                                            <ul class="carousel-list">\r\n                                                <!-- Each slide will be in a li here -->\r\n                                                {{#carouselSlides}}\r\n                                                <li>\r\n                                                    <ul class="vidDrawer clearfix">\r\n                                                        {{#videos}}\r\n                                                        <!-- Implementation Note: -->\r\n                                                        <!-- The "show-playing" and "show-progress" classes toggle display of the respective overlays -->\r\n                                                        <!-- <li class="vidDrawer-video show-playing show-progress js-vidDrawer-video"> -->\r\n                                                        <!-- <li class="vidDrawer-video show-playing js-vidDrawer-video"> -->\r\n                                                        <li class="vidDrawer-video show-progress js-vidDrawer-video">\r\n                                                        <!-- <li class="vidDrawer-video js-vidDrawer-video"> -->\r\n                                                            <div class="vidDrawer-image">\r\n                                                                <a href="{{videoURL}}">\r\n                                                                    <img src="{{thumbnailURL}}" alt="" />\r\n                                                                    <!--<div class="overlay now-playing">\r\n                                                                        Now Playing\r\n                                                                    </div>\r\n                                                                    <div class="overlay progress">\r\n                                                                        <div class="progress-inner">\r\n                                                                            <span class="amount">{{percentWatched}}</span>\r\n                                                                            <span class="percent">%</span>\r\n                                                                            <div class="watched">watched</div>\r\n                                                                        </div>\r\n                                                                    </div>-->\r\n                                                                </a>\r\n                                                            </div>\r\n                                                            <div class="vidDrawer-flag copy-white">\r\n                                                                {{_time}}\r\n                                                            </div>\r\n                                                            <div class="vidDrawer-hd copy-dk">\r\n                                                                {{_videoIndex}}. <a href="{{videoURL}}">{{title}}</a>\r\n                                                            </div>\r\n                                                        </li>\r\n                                                        {{/videos}}\r\n                                                    </ul>\r\n                                                </li>\r\n                                                {{/carouselSlides}}\r\n                                            </ul>\r\n                                        </div>\r\n                                        <div class="arrow-left carousel-previous-slide js-carousel-previous-slide">Previous</div>\r\n                                        <div class="arrow-right carousel-next-slide js-carousel-next-slide">Next</div>\r\n                                    </div>\r\n                                </div>\r\n                                {{/_videoDrawers}}\r\n                                <div class="pointer js-pointer"></div>\r\n                            </div>\r\n                        </li>'}),define("text!app/views/collection-pagination.html",[],function(){return'<ol class="pagination h-list h-list-md h-list-divided copy js-pagination">\r\n    {{#pages}}\r\n    <li><a href="#" class="{{classes}} js-pagination-item" data-page-index="{{pageIndex}}">{{pageNumber}}</a></li>\r\n    {{/pages}}\r\n</ol>'}),define("app/view-controllers/CollectionViewController",["require","framework/controllers/Controller","framework/ViewRenderer","framework/Util","jquery","libs/NCarousel/NCarousel","app/libs/CollectionsDataFeed","text!app/views/collection.html","text!app/views/collection-video-drawer.html","text!app/views/collection-pagination.html"],function(e){var t=e("framework/controllers/Controller"),n=e("framework/ViewRenderer"),r=e("framework/Util"),i=e("jquery"),s=e("libs/NCarousel/NCarousel"),o=e("app/libs/CollectionsDataFeed"),u=e("text!app/views/collection.html"),a=e("text!app/views/collection-video-drawer.html"),f=e("text!app/views/collection-pagination.html"),l=t.extend({constructor:function(e,t){return this.base(e,t),this},_initConfig:function(){this.base();var e=this._config;e.filterChangeRefreshDelay=1e3,e.containerOpenHeight=213},_initReferences:function(e,t){this.base();var n=this._references;n.dataFeed=new o(t),n.$collectionsWrapper=e,n.$loadingIndicator=e.find(".js-loading-indicator"),n.$collectionsContainer=e.find(".js-collections-container"),n.$paginationContainers=e.find(".js-pagination")},_initState:function(){this.base();var e=this._state;e.currentPageNumber=0,e.collectionsPerPage=12,e.collectionsPerRow=4,e.videoDrawerClasses="",e.videosPerDrawer=5},_initEvents:function(){this.base();var e=this._boundFunctions,t=this._references;e.onDataProcessed=this._onDataProcessed.bind(this),t.dataFeed.on("dataProcessed",e.onDataProcessed),e.onInputParamChanged=this._onInputParamChanged.bind(this),t.dataFeed.on("inputParamChanged",e.onInputParamChanged),e.onCollectionItemClick=this._onCollectionItemClick.bind(this),t.$collectionsContainer.on("click",".js-collection-item",e.onCollectionItemClick),e.onPaginationItemClick=this._onPaginationItemClick.bind(this),t.$collectionsWrapper.find(".js-pagination").on("click",".js-pagination-item",e.onPaginationItemClick)},setCollectionsPerPage:function(e){return this._state.collectionsPerPage=e,this},setCollectionsPerRow:function(e){return this._state.collectionsPerRow=e,this},setVideoDrawerClasses:function(e){return this._state.videoDrawerClasses=e,this},setVideosPerDrawer:function(e){return this._state.videosPerDrawer=e,this},getCollections:function(e,t){e==undefined?e=this._state.currentPageNumber:this._state.currentPageNumber=e,t==undefined?t=this._state.collectionsPerPage:this._state.collectionsPerPage=t;var n=this._references.dataFeed;n.setInputParam("offset",e,!0),n.setInputParam("limit",t,!0),$(".js-collections-wrapper").attr("data-searchstring")!=""&&n.setInputParam("searchString",$(".js-collections-wrapper").attr("data-searchstring"));var r=n.getCollections(),i=n.getTotalCount();if(r==0)return!1;this._updateCollectionsDisplay(r,i)},_onDataProcessed:function(){$(".js-collections-wrapper-outer").show(),this.getCollections()},_updateCollectionsDisplay:function(e,t){this._renderCollections(e),this._renderPagination(t),this._initVideoCarousels(),this._references.$loadingIndicator.hide();var n={totalCount:t};this.trigger("collectionsUpdated",n)},_initVideoCarousels:function(){var e=this._references.$collectionsContainer.find(".js-carousel-wrapper"),t=0,n=e.length;for(;t<n;t++)new s(e.eq(t),{autoPlay:!1,allowWrapping:!1})},_renderCollections:function(e,t){var i=this._state,s=i.collectionsPerRow,o=i.videoDrawerClasses,f="",l=[],c=0,h,p=e.length;for(;c<p;c++){var d=r.Object.clone(e[c],!0);d._index=c,d._collectionStats=this._getCollectionStats(d),d._plural=d.videos.length!=1,f+=n.render(u,d);for(h=0;h<d.videos.length;h++)d.videos[h]._time=r.secondsToHMSFormat(d.videos[h].duration);var v=this._prepareVideoDrawerData(d.videos);v._index=c,l.push(v);if((c+1)%s==0||c==p-1)f+=n.render(a,{_videoDrawerClasses:o,_videoDrawers:l}),l.splice(0)}this._references.$collectionsContainer.html(f)},_getCollectionStats:function(e){var t=0,n=e.videos;if(!n)throw new Error("CollectionViewController._getCollectionStats(): trying to get collection stats on an object with no videos array");var i=0,s=n.length;for(;i<s;i++){var o=n[i];t+=o.duration}var u="";e.adoptions<1e4?u=r.integerCommaFormat(e.adoptions):u=r.integerAbbreviatedFormat(e.adoptions);var a="";e.views<1e4?a=r.integerCommaFormat(e.views):a=r.integerAbbreviatedFormat(e.views);var f="";return e.likes<1e4?f=r.integerCommaFormat(e.likes):f=r.integerAbbreviatedFormat(e.likes),{time:r.secondsToHMSFormat(t),adoptions:u,views:a,likes:f}},_prepareVideoDrawerData:function(e){var t=this._state.videosPerDrawer,n=[],r=0,i=e.length,s,o;for(;r<i;r+=t){o=[];for(s=0;s<t&&s+r<i;s++){var u=e[r+s];u._videoIndex=s+r+1,o.push(u)}n.push({videos:o})}return{carouselSlides:n}},_renderPagination:function(e){var t=this._state.collectionsPerPage,r=Math.ceil(e/t),i=[],s=0;for(;s<r;s++){var o={pageIndex:s,pageNumber:s+1};s==this._state.currentPageNumber&&(o.classes="selected"),i.push(o)}var u=n.render(f,{pages:i});this._references.$paginationContainers.html(u)},_onPaginationItemClick:function(e){e.preventDefault();var t=i(e.currentTarget),n=t.data("pageIndex");if(n==this._state.currentPageNumber)return;var r=this._references.$paginationContainers.find(".js-pagination-item");r.removeClass("selected");var s=r.filter("[data-page-index="+n+"]");s.addClass("selected"),this._references.$loadingIndicator.show(),this.getCollections(n)},_onCollectionItemClick:function(e){var t=i(e.currentTarget),n=t.data("collectionItemIndex"),r=this._references.$collectionsContainer.find(".js-video-container"),s=r.find(".js-video-drawer"),o,u=0,a=s.length;for(;u<a;u++){var f=s.eq(u);if(f.data("parentCollectionItemIndex")==n){o=f;break}}var l=o.closest(".js-video-container"),c=l.find(".js-video-drawer").not(o),h=l.hasClass("open");h||(this._openVideoDrawerContainers(l),this._closeVideoDrawerContainers(r.not(l)));var p;this._references.$collectionsContainer.find(".js-video-container").each(function(){$(this).hasClass("open")&&(p=$(this).find(".js-video-drawer").filter(function(){return $(this).css("visibility")=="visible"}))});if(n==p.data("parentCollectionItemIndex"))this._hideDrawers(o),this._closeVideoDrawerContainers(l);else{this._showDrawers(o),this._hideDrawers(c);var d=l.find(".js-pointer"),v=t.offset().left,m=t.width(),g=o.offset().left,y=d.width(),b=20,w=v-g+m/2-y/2+b;h?d.animate({left:w+"px"}):d.css("left",w)}},_openVideoDrawerContainers:function(e){e.stop(!0).animate({height:this._config.containerOpenHeight+"px"}).addClass("open")},_closeVideoDrawerContainers:function(e){e.stop(!0).animate({height:"0px"}).removeClass("open")},_showDrawers:function(e){e.css({position:"relative",visibility:"visible"})},_hideDrawers:function(e){e.css({position:"",visibility:""})},setInputParam:function(e,t,n){this._references.dataFeed.setInputParam(e,t,n)},setFilterStatus:function(e,t,n){this._references.dataFeed.setFilterStatus(e,t,n)},clearFilters:function(){if(!this._references.dataFeed.clearFilters())return;this._onSearchCriteriaChanged()},_onInputParamChanged:function(){this._onSearchCriteriaChanged()},_onSearchCriteriaChanged:function(){this._references.$loadingIndicator.show(),this.getCollections(0)},destroy:function(){this.base()}});return l}),define("app/view-controllers/CollectionMostFiltersViewController",["require","framework/controllers/Controller","jquery"],function(e){var t=e("framework/controllers/Controller"),n=e("jquery"),r=t.extend({constructor:function(e){return this.base(e),this},_initReferences:function(e){this.base();var t=this._references;t.$mostFiltersContainer=e.find(".js-most-filters")},_initEvents:function(){this.base();var e=this._boundFunctions,t=this._references;e.onMostFilterClick=this._onMostFilterClick.bind(this),t.$mostFiltersContainer.on("click",".js-most-filter",e.onMostFilterClick)},_onMostFilterClick:function(e){e.preventDefault();var t=n(e.currentTarget),r=t.data("filter-id");this.setActiveFilter(r)},setActiveFilter:function(e){var t=this._references.$mostFiltersContainer.find(".js-most-filter"),n=t.filter(".active").data("filter-id");if(e==n){this.setActiveFilter("-_score");return}var r=t.filter("[data-filter-id="+e+"]");t.removeClass("active"),r.addClass("active"),this.trigger("orderChanged",e)},destroy:function(){this.base()}});return r}),define("app/libs/NewsDataFeed",["require","app/libs/DigitalGreenDataFeed","app/libs/DataModel","framework/Util"],function(e){var t=e("app/libs/DigitalGreenDataFeed"),n=e("app/libs/DataModel"),r=e("framework/Util"),i=t.extend({constructor:function(){this.base("api/activity/"),this._dataModel.addSubModel("newsItems",!0),this.addInputParam("offset",!1,0),this.addInputParam("limit",!1,10),this.addInputParam("newsFeed",!1,1)},fetch:function(e,t){e==undefined&&(e=0),t==undefined&&(t=12),this.setInputParam("offset",e*t,!0),this.setInputParam("limit",t,!0),this.setInputParam("newsFeed",1,!0),this.base()},_processData:function(e){this.base(e);var t=this._dataModel,n=t.get("newsItems"),r=e.meta.limit,i=e.meta.offset;t.set("totalCount",e.totalCount);var s=e.objects,o=i;return n.addSubset(s,o),s},setInputParam:function(e,t,n){var r=this.base(e,t);return r&&!n&&this.clearNewsItemCache(),r},clearNewsItemCache:function(){this._dataModel.get("newsItems").clear()},getTotalCount:function(){return this._dataModel.get("totalCount")},getNewsItems:function(){var e=this.getInputParam("offset"),t=this.getInputParam("limit"),n=this._dataModel.get("newsItems").getSubset(e*t,t);return n?n:(this.fetch(e,t),!1)}});return i}),define("text!app/views/news/newsItem.html",[],function(){return'                    {{#activities}}\r\n                    <li class="js-news-feed-item">\r\n                        <article class="media">\r\n                            <div class="bd grid-pad-rt-md">\r\n                                <div class="layout-vr-sm">\r\n                                    <a href="{{titleURL}}"><h3 class="hdg-green copy hdg-bold" style="display:inline-block;">{{title}}</h3></a>\r\n                                    <div class="copy-lt">{{date}}</div>\r\n                                    <p class="copy">\r\n                                        {{&textContent}}\r\n\r\n                                    </p>\r\n                                </div>\r\n                                <div class="grid js-assets-container">\r\n\r\n                                    {{#_hasImages}}\r\n                                    <ul class="h-list layout-vr-md">\r\n                                        {{#images}}\r\n                                        <li>\r\n                                            <a href="{{imageLinkURL}}"><img src="{{imageURL}}" target="_blank" height="112px" width="170px" alt="{{altString}}" /></a>\r\n                                        </li>\r\n                                        {{/images}}\r\n                                    </ul>\r\n                                    {{/_hasImages}}\r\n\r\n                                    {{#collection}}\r\n                                    <div class="grid-col">\r\n                                        <div class="vid-cat-selected">\r\n                                            <div class="vid-cat">\r\n                                                <img src="{{collection.thumbnailURL}}" />\r\n                                                <div class="vid-flag">\r\n                                                    <ul class="copy-sm copy-white h-list h-list-sm h-list-divided">\r\n                                                        <li>{{collection.videos.length}} Videos</li>\r\n                                                        <li>{{collection._collectionStats._totalDuration}}</li>\r\n                                                    </ul>\r\n                                                </div>\r\n                                                <div class="vid-cat-inner">\r\n                                                    <div class="vid-cat-hd">\r\n                                                        <h3 class="hdg-green hdg-f copy hdg-bold">{{collection.title}}</h3>\r\n                                                    </div>\r\n                                                    <div class="vid-cat-bd">\r\n                                                        <p class="copy copy-sm layout-vr-tiny">{{collection.state}} | {{collection.language}}</p>\r\n                                                        <p class="copy copy-sm">By: {{collection.partner.name}}</p>\r\n                                                    </div>\r\n                                                    <!-- NOTE: These aren\'t present in the comps, but included in case they\'re later desired -->\r\n                                                    <!-- <div class="vid-cat-ft">\r\n                                                        <ul class="h-list h-list-sm copy-sm copy-lt vid-cat-list">\r\n                                                            <li class="like">{{collection._collectionStats.likes}}</li>\r\n                                                            <li class="view">{{collection._collectionStats.views}}</li>\r\n                                                            <li class="check">{{collection._collectionStats.adoptions}}</li>\r\n                                                        </ul>\r\n                                                    </div> -->\r\n                                                </div>\r\n                                            </div>\r\n                                        </div> <!-- End .vid-cat-selected -->\r\n                                    </div> <!-- End .grid-col -->\r\n                                    <div class="grid-lt">\r\n                                        <div class="news-videoDrawer">\r\n                                            <div class="news-video-carousel carousel-wrapper js-carousel-wrapper">\r\n                                                <div class="carousel-container js-carousel-container">\r\n                                                    <ul class="carousel-list">\r\n                                                        {{#collection._carouselSlides}}\r\n                                                        <li>\r\n                                                            <ul class="h-list">\r\n                                                                {{#videos}}\r\n                                                                <li>\r\n                                                                    <a href="{{videoURL}}"><img src="{{thumbnailURL}}" target="_blank" alt="{{title}}" /></a>\r\n                                                                </li>\r\n                                                                {{/videos}}\r\n                                                            </ul>\r\n                                                        </li>\r\n                                                        {{/collection._carouselSlides}}\r\n                                                    </ul>\r\n                                                </div>\r\n                                                <div class="arrow arrow-left carousel-previous-slide js-carousel-previous-slide">Previous</div>\r\n                                                <div class="arrow arrow-right carousel-next-slide js-carousel-next-slide">Next</div>\r\n                                            </div>\r\n                                        </div>\r\n                                    </div>\r\n                                    {{/collection}}\r\n                                </div> <!-- End .grid -->\r\n                            </div> <!-- End .bd -->\r\n                        </article>\r\n                    </li>\r\n                    {{/activities}}'}),define("app/view-controllers/news/NewsFeedViewController",["require","framework/controllers/Controller","framework/ViewRenderer","framework/Util","jquery","libs/NCarousel/NCarousel","app/libs/NewsDataFeed","text!app/views/news/newsItem.html"],function(e){var t=e("framework/controllers/Controller"),n=e("framework/ViewRenderer"),r=e("framework/Util"),i=e("jquery"),s=e("libs/NCarousel/NCarousel"),o=e("app/libs/NewsDataFeed"),u=e("text!app/views/news/newsItem.html"),a=t.extend({constructor:function(e){return this.base(e),this},_initConfig:function(){this.base()},_initReferences:function(e){this.base();var t=this._references;t.dataFeed=new o,t.$newsItemsWrapper=e,t.$newsItemsContainer=e.find(".js-news-feed-container"),t.$newsFeedShowMoreButton=e.find(".js-news-feed-show-more-btn")},_initState:function(){this.base();var e=this._state;e.currentPageNumber=0,e.newsItemsPerPage=2,e.currentCount=0},_initEvents:function(){this.base();var e=this._boundFunctions,t=this._references;e.onDataProcessed=this._onDataProcessed.bind(this),t.dataFeed.on("dataProcessed",e.onDataProcessed),e.onShowMoreClick=this._onShowMoreClick.bind(this),t.$newsFeedShowMoreButton.on("click",e.onShowMoreClick)},setNewsItemsPerPage:function(e){return this._state.newsItemsPerPage=e,this},getNewsItemsPerPage:function(){return this._state.newsItemsPerPage},setCurrentPageNumber:function(e){return this._state.currentPageNumber=e,this},getCurrentPageNumber:function(){return this._state.currentPageNumber},getNewsItems:function(e,t){e==undefined?e=this.getCurrentPageNumber():this.setCurrentPageNumber(e),t==undefined?t=this.getNewsItemsPerPage():this.setNewsItemsPerPage(t);var n=this._references.dataFeed;n.setInputParam("offset",e,!0),n.setInputParam("limit",t,!0);var r=n.getNewsItems(),i=n.getTotalCount();if(r==0)return!1;this._updateNewsFeedDisplay(r,i)},_onDataProcessed:function(){this.getNewsItems()},_updateNewsFeedDisplay:function(e,t){this._prepareData(e),this._renderNewsItems(e);var n={totalCount:t,addedCount:e.length};this.trigger("newsFeedUpdated",n)},_renderNewsItems:function(e){var t={activities:e};n.renderAppend(this._references.$newsItemsContainer,u,t),this._initCarousels()},_initCarousels:function(){var e=this._references.$newsItemsContainer.find(".js-carousel-wrapper"),t=0,n=e.length;for(;t<n;t++)new s(e.eq(t),{autoPlay:!1,allowWrapping:!1})},_prepareData:function(e){var t=0,n=e.length;for(;t<n;t++){var i=e[t];i._hasImages=i.images&&i.images.length!=0,i.images&&i.images.length>4&&(i.images=i.images.splice(0,4));if(i.collection&&i.collection.videos){var s=i.collection.videos,o={likes:0,views:0,adoptions:0,time:0},u=[],a=[],f=0,l=s.length;for(;f<l;f++){var c=s[f];o.likes+=c.offlineLikes+c.onlineLikes,o.views+=c.offlineViews+c.onlineViews,o.adoptions+=c.adoptions,o.totalDuration+=c.duration,a.push(c);if(f>0&&(f+1)%4==0||f==l-1)u.push({videos:a}),a=[]}i.collection._carouselSlides=u,o.likes=r.integerCommaFormat(o.likes),o.views=r.integerCommaFormat(o.views),o.adoptions=r.integerCommaFormat(o.adoptions),o.totalDuration=r.secondsToHMSFormat(o.totalDuration),i.collection._collectionStats=o}}},updateTotalCount:function(e){this._state.totalCount=e},addToCurrentCount:function(e){this._state.currentCount+=e},updateNewsItemPaginationDisplay:function(){this._state.currentCount>=this._state.totalCount&&this._references.$newsFeedShowMoreButton.hide()},_onShowMoreClick:function(e){e.preventDefault(),e.stopPropagation(),this.getNewsItems(this.getCurrentPageNumber()+1)},setInputParam:function(e,t,n){if(!this._references.dataFeed.setInputParam(e,t,n))return},destroy:function(){this.base()}});return a}),define("app/libs/FeaturedCollectionDataFeed",["require","app/libs/DigitalGreenDataFeed","app/libs/DataModel"],function(e){var t=e("app/libs/DigitalGreenDataFeed"),n=e("app/libs/DataModel"),r=t.extend({constructor:function(e){this.base("api/featuredCollection/");var t=this._dataModel.addSubModel("featuredCollection",!0);this.addInputParamCacheClear("language__name",t)},fetch:function(e){this.setInputParam("language__name",e,!0),this.base()},_processData:function(e){this.base(e);var t=this._dataModel,n=t.get("featuredCollection");return n.set("featuredCollectionObj",e.featured_collection),e.featured_collection},setInputParam:function(e,t,n){var r=this.base(e,t);return r&&!n&&this.clearFeaturedCollectionCache(),r},clearFeaturedCollectionCache:function(){this._dataModel.get("featuredCollection").clear()},getFeaturedCollection:function(){var e=this.getInputParam("language__name"),t=this._dataModel.get("featuredCollection"),n=t.get("featuredCollectionObj");return n?n:(this.fetch(e),!1)}});return r}),define("text!app/views/featured-collection.html",[],function(){return'					<div class="grid-col grid-size3of4">\r\n                    	<a href="{{link}}">\r\n                    		<img src="{{collageURL}}" width=642 height=321 alt="">\r\n                    	</a>\r\n                    </div>\r\n                    <div class="grid-col grid-size1of4">\r\n                        <div class="grid-pad-lt-sm">\r\n                           <h3 class="hdg-green hdg-c layout-vr-sm">{{title}}</h3>\r\n                            <h4 class="copy hdg-bold"> {{state}}, {{country}}</h4>\r\n                            <h5 class="copy layout-vr-sm">{{language}}</h5>\r\n                            <p class="layout-vr-md"></p>\r\n                            <div class="featured-logo copy layout-vr-md">\r\n                            	<a href={{partner_url}}>\r\n                            		<img class="" src="{{partner_logo}}" height=41 width=39 alt="" /> \r\n                               	</a>\r\n                                {{partner_name}}\r\n                            </div>\r\n                            <div class="featured-ft">\r\n                                <div class="featured-ft-videoDetails">\r\n                                   <ul class="h-list h-list-sm h-list-divided copy copy-white">\r\n                                       <li>{{video_count}} Videos</li>\r\n                                       <li>{{duration}}</li>\r\n                                   </ul>\r\n                                </div>\r\n                                <ul class="h-list h-list-sm copy-sm copy-dk vid-cat-list-dk">\r\n                                    <li class="like"><span class="text-hide">Likes</span>{{likes}}</li>\r\n                                    <li class="view"><span class="text-hide">Viewed</span> {{views}}</li>\r\n                                    <li class="check"><span class="text-hide">Adopted</span> {{adoptions}}</li>\r\n                                </ul>\r\n                            </div>\r\n                        </div>\r\n                    </div>'}),define("app/view-controllers/FeaturedCollectionViewController",["require","framework/controllers/Controller","framework/ViewRenderer","jquery","app/libs/FeaturedCollectionDataFeed","text!app/views/featured-collection.html"],function(e){var t=e("framework/controllers/Controller"),n=e("framework/ViewRenderer"),r=e("jquery"),i=e("app/libs/FeaturedCollectionDataFeed"),s=e("text!app/views/featured-collection.html"),o=t.extend({constructor:function(e,t){return this.base(e,t),this},_initReferences:function(e,t){this.base();var n=this._references;n.dataFeed=new i(t),n.$featuredCollectionContainer=e},_initEvents:function(){this.base();var e=this._boundFunctions,t=this._references;e.onDataProcessed=this._onDataProcessed.bind(this),t.dataFeed.on("dataProcessed",e.onDataProcessed),e.onInputParamChanged=this._onInputParamChanged.bind(this),t.dataFeed.on("inputParamChanged",e.onInputParamChanged)},getFeaturedCollection:function(){var e=this._references.dataFeed.getFeaturedCollection();if(e==0)return!1;this._renderFeaturedCollection(e)},_onDataProcessed:function(){this.getFeaturedCollection()},_renderFeaturedCollection:function(e){var t=n.render(s,e);this._references.$featuredCollectionContainer.html(t)},setInputParam:function(e,t,n){this._references.dataFeed.setInputParam(e,t,n)},_onInputParamChanged:function(){this.getFeaturedCollection()},destroy:function(){this.base()}});return o}),define("controllers/HomeController",["require","controllers/DigitalGreenPageController","app/view-controllers/CollectionViewController","app/view-controllers/CollectionMostFiltersViewController","app/view-controllers/news/NewsFeedViewController","app/view-controllers/FeaturedCollectionViewController","jquery","libs/NCarousel/NCarousel","libs/external/swfobject/swfobject"],function(e){var t=e("controllers/DigitalGreenPageController"),n=e("app/view-controllers/CollectionViewController"),r=e("app/view-controllers/CollectionMostFiltersViewController"),i=e("app/view-controllers/news/NewsFeedViewController"),s=e("app/view-controllers/FeaturedCollectionViewController"),o=e("jquery"),u=e("libs/NCarousel/NCarousel");e("libs/external/swfobject/swfobject");var a=t.extend({constructor:function(e,t){this.base(e,t);var n=this._references;return n.collectionViewController.setCollectionsPerPage(4).setCollectionsPerRow(4).setVideosPerDrawer(5),n.collectionMostFiltersViewController.setActiveFilter("-likes"),this._getNewsFeed(),this._getFeaturedCollection(),this},_initReferences:function(e){this.base(e);var t=this._references,a=o(".js-collections-wrapper"),f=o(".js-news-feed-wrapper"),l=o(".js-featured-collection-wrapper"),c=Util.Cookie.get("language__name");t.collectionViewController=new n(a,c),t.collectionMostFiltersViewController=new r(a),t.newsFeedViewController=new i(f),t.FeaturedCollectionViewController=new s(l,c),t.$imageCarouselWrapper=o(".js-imageCarousel"),t.imageCarousel=new u(t.$imageCarouselWrapper,{transition:"fade",autoPlay:!0,autoPlayDelay:2e3}),t.$playButton=o(".play-button")},_initEvents:function(){this.base();var e=this._references,t=this._boundFunctions;t.onOrderChanged=this._onOrderChanged.bind(this),e.collectionMostFiltersViewController.on("orderChanged",t.onOrderChanged),t.onNewsFeedUpdated=this._onNewsFeedUpdated.bind(this),e.newsFeedViewController.on("newsFeedUpdated",t.onNewsFeedUpdated),t.onPlayButtonClick=this._onVideoPlayButtonClick.bind(this),e.$playButton.on("click",t.onPlayButtonClick)},_onOrderChanged:function(e){this._references.collectionViewController.setInputParam("order_by",e)},_getCollections:function(){this._references.collectionViewController.getCollections()},_getNewsFeed:function(){this._references.newsFeedViewController.getNewsItems()},_getFeaturedCollection:function(){this._references.FeaturedCollectionViewController.getFeaturedCollection()},_onNewsFeedUpdated:function(e){this._references.newsFeedViewController.updateTotalCount(e.totalCount),this._references.newsFeedViewController.addToCurrentCount(e.addedCount),this._references.newsFeedViewController.updateNewsItemPaginationDisplay()},_initVideoPlayer:function(){var e="RjMTx1fzpMU",t={allowScriptAccess:"always"},n={id:"player","class":"main-carousel-video-player"};swfobject.embedSWF("http://www.youtube.com/v/"+e+"?enablejsapi=1&playerapiid=ytplayer&version=3","player","1024","424","8",null,null,t,n),window.onYouTubePlayerReady=this._onYouTubePlayerReady.bind(this),$("#video-img > div").not("#player").each(function(e,t){$(t).hide()}),$("#player").show()},_onYouTubePlayerReady:function(){window.onYouTubePlayerReady=undefined;var e=o("#player").get(0);this._references.videoPlayer=e,window.onYouTubePlayerStateChange=this._onYouTubePlayerStateChange.bind(this),e.addEventListener("onStateChange","onYouTubePlayerStateChange"),e.playVideo()},_onYouTubePlayerStateChange:function(e){e==0&&($("#player").hide(),$("#video-img > div").not("#player").each(function(e,t){$(t).show()}))},_onVideoPlayButtonClick:function(e){this._initVideoPlayer()},destroy:function(){this.base()}});return a});