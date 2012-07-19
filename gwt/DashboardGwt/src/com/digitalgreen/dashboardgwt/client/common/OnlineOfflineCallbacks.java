package com.digitalgreen.dashboardgwt.client.common;

import com.digitalgreen.dashboardgwt.client.data.BaseData;
import com.digitalgreen.dashboardgwt.client.servlets.BaseServlet;
import com.google.gwt.http.client.Response;

public class OnlineOfflineCallbacks {
	private BaseServlet servlet;
	private Response response;
	protected boolean uploadInterrupted = false;
	
	public OnlineOfflineCallbacks(BaseServlet servlet) {
		this.servlet = servlet;
		this.uploadInterrupted=false;
	}
	
	public OnlineOfflineCallbacks(BaseServlet servlet, boolean uploadInterrupted) {
		this.servlet = servlet;
		this.uploadInterrupted = uploadInterrupted;
	}
	
	public BaseServlet getServlet() {
		return this.servlet;
	}
	
	public void onlineSuccessCallback(String results) {}
	public void onlineErrorCallback(int errorCode) {}
	public void offlineSuccessCallback(Object results) {}

	public void setResponse(Response response) {
		this.response = response;
	}
	
	public Response getResponse() {
		return this.response;
	}
	
	public int getStatusCode() {
		return this.response.getStatusCode();
	}
	
}