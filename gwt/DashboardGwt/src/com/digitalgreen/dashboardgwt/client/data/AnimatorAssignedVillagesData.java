package com.digitalgreen.dashboardgwt.client.data;

import java.util.ArrayList;
import java.util.List;
import com.digitalgreen.dashboardgwt.client.common.Form;
import com.digitalgreen.dashboardgwt.client.common.OnlineOfflineCallbacks;
import com.digitalgreen.dashboardgwt.client.common.RequestContext;
import com.google.gwt.core.client.JsArray;
import com.google.gwt.gears.client.database.DatabaseException;
import com.google.gwt.user.client.Window;

public class AnimatorAssignedVillagesData extends BaseData{
	
	public static class Type extends BaseData.Type {
		protected Type() {}
		public final native AnimatorsData.Type getAnimator() /*-{ return this.fields.animator; }-*/ ;
		public final native VillagesData.Type getVillage() /*-{ return this.fields.village; }-*/ ;
		public final native String getStartDate() /*-{ return this.fields.start_date; }-*/;
	}
	
	public class Data extends BaseData.Data {
		
		final private static String COLLECTION_PREFIX = "animatorAssignedVillages";
		
		private AnimatorsData.Data animator;
		private VillagesData.Data village;
		private String start_date;
		
		public Data() {
			super();
		}
		
		public Data(String id, String start_date){
			super();
			this.id = id;
			this.start_date = start_date;
		}
		
		public Data(String id, AnimatorsData.Data animator, VillagesData.Data village, String start_date){
			super();
			this.id = id;
			this.animator = animator;
			this.village = village;
			this.start_date = start_date;
		}
		
		public String getStartDate(){
			return this.start_date;
		}
		
		public AnimatorsData.Data getAnimator(){
			return this.animator;
		}
		
		public VillagesData.Data getVillage(){
			return this.village;
		}
		
		@Override
		public BaseData.Data clone(){
			Data obj = new Data();
			obj.id = this.id;
			obj.animator = this.animator;
			obj.village = this.village;
			obj.start_date = this.start_date;
			return obj;
		}
		
		@Override
		public String getPrefixName(){
			return this.COLLECTION_PREFIX;
		}
		
		@Override
		public void setObjValueFromString(String key, String val){
			super.setObjValueFromString(key, val);
			if(key.equals("id")) {
				this.id = val;
			}
			else if(key.equals("animator")) {
				AnimatorsData animator1 = new AnimatorsData();
				this.animator = animator1.getNewData();
				this.animator.id = val;
			}
			else if(key.equals("village")){
				VillagesData village1 = new VillagesData();
				this.village = village1.getNewData();
				this.village.id = val;
			}
			else if(key.equals("start_date")) {
				this.start_date = (String)val;
			}
		}
		
		@Override
		public void save(){

			AnimatorAssignedVillagesData animatorAssignedVillagesDataDbApis = new AnimatorAssignedVillagesData();
<<<<<<< .mine
			
			this.id = animatorAssignedVillagesDataDbApis.autoInsert(this.animator.getId(), 
					this.village.getId(), 
					this.start_date);
=======
			if(this.id == 0){
				this.id = animatorAssignedVillagesDataDbApis.autoInsert(Integer.valueOf(this.animator.getId()).toString(), 
						Integer.valueOf(this.village.getId()).toString(), this.start_date);
			}else{
				this.id = animatorAssignedVillagesDataDbApis.autoInsert(Integer.valueOf(this.id).toString(), Integer.valueOf(this.animator.getId()).toString(), 
						Integer.valueOf(this.village.getId()).toString(), this.start_date);
			}
				
				
>>>>>>> .r278
		}
		
	}
	
	protected static String tableID = "18";
	protected static String createTable = "CREATE TABLE IF NOT EXISTS `animator_assigned_village` " +
												"(id INTEGER PRIMARY KEY NOT NULL ," +
												"animator_id INT  NOT NULL DEFAULT 0," +
												"village_id INT  NOT NULL DEFAULT 0," +
												"START_DATE DATE  NULL DEFAULT NULL, " +
												"FOREIGN KEY(animator_id) REFERENCES animator(id), " +
												"FOREIGN KEY(village_id) REFERENCES village(id));";
	protected static String selectAnimatorsAssignedVillages = "SELECT id, start_date from animator_assigned_village ORDER BY(id);";
	protected static String listAnimatorsAssignedVillages = "SELECT animator_assigned_village.id, animator.id, animator.name, village.id, village.VILLAGE_NAME, animator_assigned_village.START_DATE FROM animator_assigned_village JOIN animator ON animator_assigned_village.animator_id = animator.id JOIN village ON animator_assigned_village.village_id = village.id ORDER BY(-animator_assigned_village.id);";
	protected static String saveAnimatorAssignedVillageOnlineURL = "/dashboard/saveanimatorassignedvillageonline/";
	protected static String getAnimatorAssignedVillageOnlineURL = "/dashboard/getanimatorassignedvillagesonline/";
	protected static String saveAnimatorAssignedVillageOfflineURL = "/dashboard/saveanimatorassignedvillageoffline/";
	protected String table_name = "animator_assigned_village";
	protected String[] fields = {"id", "animator_id", "village_id", "start_date"};

	public AnimatorAssignedVillagesData(){
		super();
	}
	
	public AnimatorAssignedVillagesData(OnlineOfflineCallbacks callbacks){
		super(callbacks);
	}
	
	public AnimatorAssignedVillagesData(OnlineOfflineCallbacks callbacks, Form form, String queryString){
		super(callbacks, form, queryString);
	}
	
	@Override
	public Data getNewData(){
		return new Data();
	}
	
	@Override
	protected String getTableId(){
		return AnimatorAssignedVillagesData.tableID;
	}
	
	@Override
	protected String getTableName(){
		return this.table_name;
	}
	
	@Override
	protected String[] getFields(){
		return this.fields;
	}
	
	@Override
	public String getListingOnlineURL(){
		return AnimatorAssignedVillagesData.getAnimatorAssignedVillageOnlineURL;
	}

	public final native JsArray<Type> asArrayOfData(String json) /*-{
		return eval(json);
	}-*/;
	
	public List serialize(JsArray<Type> animatorAssignedVillageObjects){
		List animatorAssignedVillages = new ArrayList();
		AnimatorsData animator = new AnimatorsData();
		VillagesData village = new VillagesData();
		for ( int i = 0; i < animatorAssignedVillageObjects.length(); i++ ) {
			
			AnimatorsData.Data a = animator. new Data(Integer.parseInt(animatorAssignedVillageObjects.get(i).getAnimator().getPk()), 
					animatorAssignedVillageObjects.get(i).getAnimator().getAnimatorName());
			
			VillagesData.Data v = village. new Data(Integer.parseInt(animatorAssignedVillageObjects.get(i).getVillage().getPk()), animatorAssignedVillageObjects.get(i).getVillage().getVillageName());
			
			Data animatorassignedvillage = new Data(Integer.parseInt(animatorAssignedVillageObjects.get(i).getPk()), a, v, animatorAssignedVillageObjects.get(i).getStartDate());
			
			animatorAssignedVillages.add(animatorassignedvillage);
		}
		return animatorAssignedVillages;
	}
	
	@Override
	public List getListingOnline(String json){
		return this.serialize(this.asArrayOfData(json));		
	}
	
	public List getAnimatorsAssignedVillagesListingOffline(){
		BaseData.dbOpen();
		List animatorsAssignedVillages = new ArrayList();
		AnimatorsData animator = new AnimatorsData();
		VillagesData village = new VillagesData();
		this.select(listAnimatorsAssignedVillages);
		if(this.getResultSet().isValidRow()){
			try{
				
				for (int i = 0; this.getResultSet().isValidRow(); ++i, this.getResultSet().next()) {
					
					AnimatorsData.Data a = animator. new Data(this.getResultSet().getFieldAsInt(1), this.getResultSet().getFieldAsString(2));
					
					VillagesData.Data s = village. new Data(this.getResultSet().getFieldAsInt(3), this.getResultSet().getFieldAsString(4));
					
					Data animatorassignedvillage = new Data(this.getResultSet().getFieldAsInt(0), this.getResultSet().getFieldAsString(5));
					
					animatorsAssignedVillages.add(animatorassignedvillage);					
				}
			}
			catch (DatabaseException e) {
				Window.alert("Database Exception : " + e.toString());
				BaseData.dbClose();
			}
		}
		BaseData.dbClose();
		return animatorsAssignedVillages;
	}
	
	public List getAllAnimatorsAssignedVillagesOnline(){
		BaseData.dbOpen();
		List animatorsAssignedVillages = new ArrayList();
		this.select(selectAnimatorsAssignedVillages);
		if(this.getResultSet().isValidRow()){
			try {
				for (int i = 0; this.getResultSet().isValidRow(); ++i, this.getResultSet().next()) {
				
					Data animatorassignedvillage = new Data(this.getResultSet().getFieldAsInt(0), this.getResultSet().getFieldAsString(1));
					
					animatorsAssignedVillages.add(animatorassignedvillage);
				}
			}
			catch (DatabaseException e) {
				Window.alert("Database Exception : " + e.toString());
				BaseData.dbClose();
			}
		}
		
		BaseData.dbClose();
		return animatorsAssignedVillages;
	}
	
	public List getTemplateDataOnline(String json){
		List relatedData = null;
		return relatedData;
	}
	
	public Object postPageData() {
		if(BaseData.isOnline()){
			this.post(RequestContext.SERVER_HOST + AnimatorAssignedVillagesData.saveAnimatorAssignedVillageOnlineURL, this.queryString);
		}
		else{
			this.save();
			return true;
		}
		return false;
	}
	
	public Object getListPageData(){
		if(BaseData.isOnline()){
			this.get(RequestContext.SERVER_HOST + AnimatorAssignedVillagesData.getAnimatorAssignedVillageOnlineURL);
		}
		else {
			return true;
		}
		return false;
	}
	
	public String retrieveDataAndConvertResultIntoHtml() {
		AnimatorsData animatorData = new AnimatorsData();
		List animators = animatorData.getAnimatorsListingOffline();
		AnimatorsData.Data animator;
		String htmlAnimator = "<select name=\"animator\" id=\"id_animator\"";
		for ( int i = 0; i < animators.size(); i++ ) {
			animator = (AnimatorsData.Data)animators.get(i);
			htmlAnimator = htmlAnimator + "<option value=\"" + animator.getId() + "\">" + animator.getAnimatorName() + "</option>";
		}
		htmlAnimator = htmlAnimator + "</select>";
		
		VillagesData villageData = new VillagesData();
		List villages = villageData.getVillagesListingOffline();
		VillagesData.Data village;
		String htmlVillage = "<select name=\"village\" id=\"id_village\"";
		for(int i = 0; i < villages.size(); i++ ) {
			village = (VillagesData.Data)villages.get(i);
			htmlVillage = htmlVillage + "<option value=\"" + village.getId() + "/>" + village.getVillageName() + "</option>";
		}
		htmlVillage = htmlVillage + "</select>";
		
		return htmlAnimator + htmlVillage;
	}
	
	public Object getAddPageData() {
		if(BaseData.isOnline()) {
			this.get(RequestContext.SERVER_HOST + AnimatorAssignedVillagesData.saveAnimatorAssignedVillageOnlineURL);
		}
		else{
			return retrieveDataAndConvertResultIntoHtml();
		}
		return false;
	}
}