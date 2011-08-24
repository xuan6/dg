package com.digitalgreen.dashboardgwt.client.data;

import com.google.gwt.gears.client.database.DatabaseException;
import com.google.gwt.user.client.Window;

public class Schema {
	
	public static void createSchema() {
		try {
			BaseData.dbOpen();
			BaseData.dbStartTransaction();
			BaseData.getDb().execute(RegionsData.createTable);
			BaseData.getDb().execute(EquipmentHoldersData.createTable);
			BaseData.getDb().execute(ReviewersData.createTable);
			BaseData.getDb().execute(DevelopmentManagersData.createTable);
			BaseData.getDb().execute(StatesData.createTable);
			BaseData.getDb().execute(PartnersData.createTable);
			BaseData.getDb().execute(FieldOfficersData.createTable);
			BaseData.getDb().execute(DistrictsData.createTable);
			BaseData.getDb().execute(BlocksData.createTable);
			BaseData.getDb().execute(VillagesData.createTable);
			BaseData.getDb().execute(MonthlyCostPerVillageData.createTable);
			BaseData.getDb().execute(PersonGroupsData.createTable);
			BaseData.getDb().execute(PersonsData.createTable);
			BaseData.getDb().execute(PersonRelationsData.createTable);
			BaseData.getDb().execute(AnimatorsData.createTable);
			BaseData.getDb().execute(TrainingsData.createTable);
			BaseData.getDb().execute(TrainingAnimatorsTrainedData.createTable);
			BaseData.getDb().execute(AnimatorAssignedVillagesData.createTable);
			BaseData.getDb().execute(AnimatorSalaryPerMonthData.createTable);
			BaseData.getDb().execute(LanguagesData.createTable);
			BaseData.getDb().execute(PracticesData.createTable);
			BaseData.getDb().execute(VideosData.createTable);
			BaseData.getDb().execute(VideoRelatedAgriculturalPracticesData.createTable);
			BaseData.getDb().execute(VideoFarmersShownData.createTable);
			BaseData.getDb().execute(ScreeningsData.createTable);
			BaseData.getDb().execute(ScreeningFarmerGroupsTargetedData.createTable);
			BaseData.getDb().execute(ScreeningVideosScreenedData.createTable);
			BaseData.getDb().execute(PersonMeetingAttendanceData.createTable);
			BaseData.getDb().execute(PersonAdoptPracticeData.createTable);
			BaseData.getDb().execute(EquipmentsData.createTable);
			BaseData.getDb().execute(LoginData.createTable);
			BaseData.getDb().execute(FormQueueData.createTable);
			BaseData.getDb().execute(TargetsData.createTable);
			BaseData.dbCommit();
			BaseData.dbClose();
		} catch (DatabaseException e) {
			Window.alert("Database Exception : Error in creating the tables");
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void createIndexes() {
		try {
			BaseData.dbOpen();
			BaseData.dbStartTransaction();
			BaseData.getDb().execute(RegionsData.createIndexes);
			BaseData.getDb().execute(EquipmentHoldersData.createIndexes);
			BaseData.getDb().execute(ReviewersData.createTable);
			BaseData.getDb().execute(DevelopmentManagersData.createTable);
			BaseData.getDb().execute(StatesData.createTable);
			BaseData.getDb().execute(PartnersData.createTable);
			BaseData.getDb().execute(FieldOfficersData.createTable);
			BaseData.getDb().execute(DistrictsData.createTable);
			BaseData.getDb().execute(BlocksData.createTable);
			BaseData.getDb().execute(VillagesData.createTable);
			BaseData.getDb().execute(MonthlyCostPerVillageData.createTable);
			BaseData.getDb().execute(PersonGroupsData.createTable);
			BaseData.getDb().execute(PersonsData.createTable);
			BaseData.getDb().execute(PersonRelationsData.createTable);
			BaseData.getDb().execute(AnimatorsData.createTable);
			BaseData.getDb().execute(TrainingsData.createTable);
			BaseData.getDb().execute(TrainingAnimatorsTrainedData.createTable);
			BaseData.getDb().execute(AnimatorAssignedVillagesData.createIndexes);
			BaseData.getDb().execute(AnimatorSalaryPerMonthData.createIndexes);
			BaseData.getDb().execute(LanguagesData.createTable);
			BaseData.getDb().execute(PracticesData.createTable);
			BaseData.getDb().execute(VideosData.createTable);
			BaseData.getDb().execute(VideoRelatedAgriculturalPracticesData.createTable);
			BaseData.getDb().execute(VideoFarmersShownData.createTable);
			BaseData.getDb().execute(ScreeningsData.createTable);
			BaseData.getDb().execute(ScreeningFarmerGroupsTargetedData.createTable);
			BaseData.getDb().execute(ScreeningVideosScreenedData.createTable);
			BaseData.getDb().execute(PersonMeetingAttendanceData.createTable);
			BaseData.getDb().execute(PersonAdoptPracticeData.createTable);
			BaseData.getDb().execute(EquipmentsData.createTable);
			BaseData.getDb().execute(LoginData.createTable);
			BaseData.getDb().execute(FormQueueData.createTable);
			BaseData.getDb().execute(TargetsData.createTable);
			BaseData.dbCommit();
			BaseData.dbClose();
		} catch (DatabaseException e) {
			Window.alert("Database Exception : Error in creating the tables");
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void dropSchema() {
		try {
			BaseData.dbOpen();
			BaseData.dbStartTransaction();
			BaseData.getDb().execute(RegionsData.dropTable);
			BaseData.getDb().execute(EquipmentHoldersData.dropTable);
			BaseData.getDb().execute(ReviewersData.dropTable);
			BaseData.getDb().execute(DevelopmentManagersData.dropTable);
			BaseData.getDb().execute(StatesData.dropTable);
			BaseData.getDb().execute(PartnersData.dropTable);
			BaseData.getDb().execute(FieldOfficersData.dropTable);
			BaseData.getDb().execute(DistrictsData.dropTable);
			BaseData.getDb().execute(BlocksData.dropTable);
			BaseData.getDb().execute(VillagesData.dropTable);
			BaseData.getDb().execute(MonthlyCostPerVillageData.dropTable);
			BaseData.getDb().execute(PersonGroupsData.dropTable);
			BaseData.getDb().execute(PersonsData.dropTable);
			BaseData.getDb().execute(PersonRelationsData.dropTable);
			BaseData.getDb().execute(AnimatorsData.dropTable);
			BaseData.getDb().execute(TrainingsData.dropTable);
			BaseData.getDb().execute(TrainingAnimatorsTrainedData.dropTable);
			BaseData.getDb().execute(AnimatorAssignedVillagesData.dropTable);
			BaseData.getDb().execute(AnimatorSalaryPerMonthData.dropTable);
			BaseData.getDb().execute(LanguagesData.dropTable);
			BaseData.getDb().execute(PracticesData.dropTable);
			BaseData.getDb().execute(VideosData.dropTable);
			BaseData.getDb().execute(VideoRelatedAgriculturalPracticesData.dropTable);
			BaseData.getDb().execute(VideoFarmersShownData.dropTable);
			BaseData.getDb().execute(ScreeningsData.dropTable);
			BaseData.getDb().execute(ScreeningFarmerGroupsTargetedData.dropTable);
			BaseData.getDb().execute(ScreeningVideosScreenedData.dropTable);
			BaseData.getDb().execute(PersonMeetingAttendanceData.dropTable);
			BaseData.getDb().execute(PersonAdoptPracticeData.dropTable);
			BaseData.getDb().execute(EquipmentsData.dropTable);
			BaseData.getDb().execute(LoginData.dropTable);
			BaseData.getDb().execute(FormQueueData.dropTable);
			BaseData.getDb().execute(TargetsData.dropTable);
			BaseData.dbCommit();
			BaseData.dbClose();
		} catch (DatabaseException e) {
			Window.alert("Database Exception : Error in creating the tables");
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}