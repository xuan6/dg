from django.shortcuts import *
from django.http import HttpResponseRedirect
from dg.output.views.common import home_with_analytics
#Mindless views for plain HTML pages on the main website
def home(request):
    if request.get_host() == "sandbox.digitalgreen.org":
        return HttpResponseRedirect('/coco/home.html')
    else:
        return home_with_analytics()
    
def wondervillage(request):
   
    return render_to_response('wondervillage.html') 

def annualreports(request):
   
    return render_to_response('annualreports.html')    

def featuredfarmer(request):
   
    return render_to_response('base_featuredfarmer.html')

def melissaho(request):
   
    return render_to_response('mellisaho.html')

def videopage(request):
   
    return render_to_response('videopage.html')

def searchvideo_result(request):
   
    return render_to_response('searchvideo_result.html')

def aboutus(request):
    
    return render_to_response('base_aboutusoverview.html')

def annualreport09(request):
   
    return render_to_response('annualreport09-10.html')

def annualreport10(request):   
    return render_to_response('annualreport10-11.html')

def annualletter(request):   
    return render_to_response('annualletter.html')

def annualletter10(request):   
    return render_to_response('annualletter10-11.html')

def projectprogress(request):   
    return render_to_response('projectprogress.html')

def projectprogress10(request):   
    return render_to_response('projectprogress10-11.html')

def budgetprogress(request):   
    return render_to_response('budgetprogress.html')

def financial10(request):   
    return render_to_response('financial10-11.html')

def scalability(request):   
    return render_to_response('scalability.html')

def lessonlearned(request):   
    return render_to_response('lessonlearned.html')

def challenge10(request):   
    return render_to_response('challenge10.html')

def keyprinciple(request):
    
    return render_to_response('base_overviewkeyprinciple.html')

def corevalue(request):
    
    return render_to_response('base_overviewcorevalue.html')

def sop(request):    
    return render_to_response('workprocedure.html')

def overviewfarmer(request):    
    return render_to_response('base_overviewfarmer.html')

def overviewdatabase(request):    
    return render_to_response('base_overviewdatabase.html')

def overviewproduction(request):    
    return render_to_response('base_overviewproduction.html')

def overviewsequence(request):    
    return render_to_response('base_overviewsequence.html')

def overviewdiffusion(request):    
    return render_to_response('base_overviewdiffusion.html')

def overviewscalability(request):    
    return render_to_response('base_overviewscalability.html')

def overviewdistribution(request):    
    return render_to_response('base_overviewdistribution.html')

def career(request):    
    return render_to_response('base_career.html')

def careers(request):    
    return render_to_response('base_career.html')

def contact(request):    
    return render_to_response('base_contact.html')

def team(request):    
    return render_to_response('base_team.html')


def teamboard(request):    
    return render_to_response('base_team_board.html')


def teamadviser(request):    
    return render_to_response('base_team_adviser.html')

def teamacclaw(request):    
    return render_to_response('base_team_acclaw.html')

def teamintern(request):    
    return render_to_response('base_team_intern.html')

def teamalumni(request):    
    return render_to_response('base_team_alumni.html')

def teammember(request):    
    return render_to_response('base_team_members.html')

def press(request):
    
    return render_to_response('base_press.html')

def partner(request):
    
    return render_to_response('base_partner.html')

def rfa(request):
   
    return render_to_response('partnerselection.html')

def partnerexecutive(request):
    
    return render_to_response('base_partnerexecutive.html')

def partnerresearch(request):
    
    return render_to_response('base_partnerresearch.html')

def partnerinvestor(request):
    
    return render_to_response('base_partnerinvestor.html')

def partnersupporter(request):
    
    return render_to_response('base_partnersupporter.html')

def careerid(request):
    
    return render_to_response('base_career_id.html')

def careersm(request):
    
    return render_to_response('base_career_sm.html')

def careerpm(request):
    
    return render_to_response('base_career_pm.html')

def careerts(request):
    
    return render_to_response('base_career_ts.html')

def careerqam(request):
    
    return render_to_response('base_career_qam.html')

def careerrse(request):
    
    return render_to_response('base_career_se.html')

def careeradm(request):
    
    return render_to_response('base_career_adm.html')

def donate(request):
    
    return render_to_response('base_donate.html')

def tech(request):
    
    return render_to_response('technology.html')

def update(request):
    return HttpResponseRedirect('https://sites.google.com/a/digitalgreen.org/inside-digital-green/updates')

def latestupdate(request):
    return HttpResponseRedirect('https://sites.google.com/a/digitalgreen.org/inside-digital-green/updates/june292010transition')

def nexus(request):
    return HttpResponseRedirect('https://sites.google.com/a/digitalgreen.org/inside-digital-green/nexus')
