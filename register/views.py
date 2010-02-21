from revels2010.register.models import Student_details, RegisteredStudent
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# function to feed all the details into the database from the CSV file on my desktop
# this is awesome 
def feed_details():	
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

# function to query based on regno

def search_reg(val):
    
    student = Student_details.objects.get(regno=val)
    dict = {'student_name':student.name , 'student_regno':student.regno , 'student_sem':student.semester, 'student_college':student.coll }
    return dict 



# home page render to response
def home(request):
    regno_form = request.POST['regno']	
    con = request.POST['contact']	
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
def reg_page(request):
    return render_to_response('register.html',{})


def authentication(request):
    return render_to_response('login.html',{})

#@login_required    
def access_check(request):
    user = request.POST["username"]
    password = request.POST["password"]
    authuser = authenticate(username=user,password=password)
    if authuser is None:
        return render_to_response('alreg.html',{'error':'Not Authorized to use this system'})
    else:
        return reg_page(request)





def outside(request):
    regno_form = request.POST['regno']	
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
        newreg.save()
        obj = RegisteredStudent.objects.get(regno=regno_form)
	d['student_name']=obj.name
        d['student_regno'] = obj.regno
	d['contact'] = obj.contact
	d['student_college'] = obj.coll
        return render_to_response('index.html',d)

 
