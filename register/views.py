from revels2010.register.models import Student_details,RegisteredStudent,Category,Event,Team
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import datetime

# function to feed all the details into the database from the CSV file on my desktop
# this is awesome 
'''def feed_details():	
    f= open("/home/tushar/Desktop/student.csv","r")

    list_lines = f.readlines()
    for li in list_lines:
        p = li.split(";")
        if  p[0][1] == '9':
            p[0] = p[0][0] + '0' + p[0][1:]
#for i in xrange(0,len(p)):
        name =  p[1][1:-1]
        regno = p[0][1:-1]
	sem = p[3]
	sem = int(sem[1]) + 1
	r = Student_details()
	r.name = name
	r.regno = regno
	r.semester = sem
	r.save()
'''
# function to query based on regno
#@login_required
def search_reg(val):
    
    student = Student_details.objects.get(regno=val)
    dict = {'student_name':student.name , 'student_regno':student.regno , 'student_sem':student.semester, 'student_college':student.coll }
    return dict 



# home page render to response
def home(request):
    regno_form = request.POST['regno']	
    con = request.POST['contact'];
    email = request.POST['email']
    if ((len(con) < 10) or (len(con) > 11)): 
        return render_to_response('alreg.html',{'error':"Invalid Contact Number"})
    if (len(con)==11 and con[0]!='0'):
        return render_to_response('alreg.html',{'error':"Invalid Contact Number"})		
    try:
        d = search_reg(regno_form)	
    except Student_details.DoesNotExist:
        return render_to_response('alreg.html',{'error':"Not a valid student"})


    try:	
        reg = RegisteredStudent.objects.get(regno=regno_form)	
        return render_to_response('alreg.html', {'error':"Already Registered with Id  "+str(reg.id)}) 	    
    except RegisteredStudent.DoesNotExist:
        newreg = RegisteredStudent()	
        newreg.name = d['student_name']
        newreg.regno = d['student_regno']
        newreg.coll = d['student_college']
	newreg.contact= con;
        newreg.save()
        obj = RegisteredStudent.objects.get(regno=regno_form)
        d['regid'] = obj.id
	d['contact'] = obj.contact
        return render_to_response('index.html',d)

   
## reigstration page       
#@login_required	
def reg_page(request):
    return render_to_response('registration.html',{})

def mit(request):
    return render_to_response('register.html',{})

def authentication(request):
    return render_to_response('login.html',{})
def outsider(request):
    return render_to_response('outside.html',{})	

#@login_required    
def access_check(request):
    user = request.POST['username']
    password = request.POST['password']
    authuser = authenticate(username=user,password=password)
    if authuser is None:
        return render_to_response('alreg.html',{'error':'Not Authorized to use this system'})
    else:
        return reg_page(request)




#@login_required
def outside(request):
    regno_form = request.POST['regno']	
    sname = request.POST['name']
    scoll = request.POST['coll']
    add = request.POST['address']
    con = request.POST['contact']
    if len(sname) == 0 or len(add)==0 or len(scoll)==0 or len(con)==0:
	return render_to_response('alreg.html',{'error':"all fields need to be filled"})
    if ((len(con) < 10) or (len(con) > 11)): 
        return render_to_response('alreg.html',{'error':"Invalid Contact Number"})
    if (len(con)==11 and con[0]!='0'):
        return render_to_response('alreg.html',{'error':"Invalid Contact Number"})		
 	
    try:	
        reg = RegisteredStudent.objects.get(regno=regno_form)	
        return render_to_response('alreg.html', {'error':"Already Registered with Id  "+str(reg.id)}) 	    
    except RegisteredStudent.DoesNotExist:
        newreg = RegisteredStudent()	
        newreg.name = request.POST['name']
        newreg.regno = request.POST['regno']
        newreg.coll = request.POST['coll']
	newreg.address = request.POST['address']
	newreg.contact= request.POST['contact']
	newreg.email = request.POST['email']
        newreg.save()
        obj = RegisteredStudent.objects.get(regno=regno_form)
	d={}
	d['student_name']=obj.name
        d['student_regno'] = obj.regno
	d['contact'] = obj.contact
	d['student_college'] = obj.coll
	d['regid'] = obj.id
        return render_to_response('index.html',d)



	
def addCategory(catname,cathead):
    cat = Category()
    cat.name = catname
    cat.head = cathead
    cat.save()
    return cat.id

def addEvent(eventname,eventhead,n,categ): 
    event = Event()
    event.name = eventname
    event.head = eventhead
    event.participants = n
    cat = Category.objects.get(name=categ)
    event.category = cat
    event.save()
    return event.id

def addParticipant(teamid,delno):
    student = RegisteredStudent.objects.get(pk=delno)
    teamobj = Team.objects.get(pk=teamid)
    student.team = teamobj
    student.save()
    return None
    

def addTeam(event,list):	## takes name of event
    team = Team()
    ev = Event.objects.get(name=event)
    team.event = ev
    team.save()	       
    for i in range(0,len(list)):
        addParticipant(team.id,list[i])
    return team.id		 
				

def eventreg(request):
    return render_to_response('eventlogin.html',{})

def eventcheck(request):
    user = request.POST['username']
    password = request.POST['password']
    authuser = authenticate(username=user,password=password)
    if authuser is None:
        return render_to_response('alreg.html',{'error':'Not Authorized to use this system'})
    else:
    	categories = Category.objects.all()                
        return render_to_response('cateventlist.html',{'eventlist':categories})


def getEventList(request):
    cat = request.GET['category']
    categ = Category.objects.get(name=cat)
    
    eventobjs =  Event.objects.filter(category=categ.id)
    return render_to_response('eventlist.html',{'events':eventobjs})

def regforevent(request):
    eventname = request.GET['events']
    event = Event.objects.get(name=eventname)
    numpart = event.participants
    return render_to_response('regevent.html',{'eventname':event,'numpart':numpart})



def regcomplete(request):
    delnos = request.GET['delcard']
    eventname = request.GET['eventid']
    dellist = delnos.split(',')
    teamid = addTeam(eventname,dellist)
    return render_to_response('complete.html',{'teamid':teamid })	
    

def search(request):
    delid = request.GET['delno']
    delobj = RegisteredStudent.objects.get(pk=delid)
    return render_to_response('searchresults.html',{ 'del':delobj })
 
