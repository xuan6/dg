define(["require","app/libs/DigitalGreenDataFeed"],function(e){var t=e("app/libs/DigitalGreenDataFeed"),n=t.extend({constructor:function(){this.base("api/updateVideoLike/"),this.addInputParam("video",!0),this.addInputParam("user",!0)},fetch:function(e,t,n,r){this.setInputParam("video",e),this.setInputParam("user",t),this.base(null,n,r)},_initConfig:function(){this.base(),this._config.fetchDelay=0},_processData:function(e){this.base(e);if(e.objects==undefined)return e.id!=undefined?[{liked:!0}]:[{liked:!1}];var t=e.objects;return t.length>0?[{liked:!0}]:[{liked:!1}]}});return n});