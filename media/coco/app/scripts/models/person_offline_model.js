define([
  'backbone',
  'indexeddb_backbone_config'
  
], function(_){
  var person_offline_model = Backbone.Model.extend({
        remove: function() {
            this.destroy();
        },
        database: databasev1,
        storeName: "person",

    });
  // Return the model for the module
  return person_offline_model;
});