define(["require","app/libs/DigitalGreenDataFeed","app/libs/DataModel"],function(e){var t=e("app/libs/DigitalGreenDataFeed"),n=e("app/libs/DataModel"),r=t.extend({_filters:undefined,constructor:function(){this.base("api/activity/");var e=this._dataModel.addSubModel("activities",!0);this.addInputParam("partner",!1,undefined,!0,e),this.addInputParam("farmerID",!1,undefined,!0,e),this.addInputParam("userUID",!1,undefined,!0,e),this.addInputParamCacheClear("language__name",e),this.addInputParam("offset",!1),this.addInputParam("limit",!1)},fetch:function(e,t){e==undefined&&(e=0),t==undefined&&(t=10),this.setInputParam("offset",e*t,!0),this.setInputParam("limit",t,!0),this.base()},_processData:function(e){this.base(e);var t=this._dataModel,n=t.get("activities"),r=e.meta.limit,i=e.meta.offset;t.set("totalCount",e.meta.total_count);var s=e.objects,o=i;return n.addSubset(s,o),s},clearCollectionCache:function(){this._dataModel.get("activities").clear()},getTotalCount:function(){return this._dataModel.get("totalCount")},getActivities:function(){var e=this.getInputParam("offset"),t=this.getInputParam("limit"),n=this._dataModel.get("activities").getSubset(e*t,t);return n?n:(this.fetch(e,t),!1)}});return r});