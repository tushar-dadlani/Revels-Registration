from revels2010.register.models import Student_details
from django.shortcuts import render_to_response

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
    d = search_reg(regno_form)
    return render_to_response('index.html',d)

def reg_page(request):
    return render_to_response('register.html',{})
