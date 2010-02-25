package com.digitalgreen.dashboardgwt.client.common;

import com.digitalgreen.dashboardgwt.client.servlets.BaseServlet;

public class OnlineOfflineCallbacks {
	private BaseServlet servlet;
	public OnlineOfflineCallbacks(BaseServlet servlet) {
		this.servlet = servlet;
	}
	
	public BaseServlet getServlet() {
		return this.servlet;
	}
	
	public void onlineSuccessCallback(String results) {}
	public void onlineErrorCallback() {}
	public void offlineSuccessCallback(Object results) {}
}