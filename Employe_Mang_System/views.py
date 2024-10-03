from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import EmployeeRecord

# server port address is 8001
# Create your views here.

# Home function
def home(request):
    return render(request, 'index.html', {})

# Add function
def add(request):
    return render(request, 'add.html',{})

# Update Show function
def update(request):
    EmpDataUpdateObj = EmployeeRecord.objects.all()
    updatedata = {
        'EmpDataUpdateObj':EmpDataUpdateObj
    }
    return render(request, 'update.html',updatedata)

# Update function
def updateEmp(request, Emp_id):
    print(Emp_id)
    EmpDataUpdateObj = get_object_or_404(EmployeeRecord, id=Emp_id)
    mydict = {
        'EmpDataUpdateObj': EmpDataUpdateObj
    }
    if request.method == 'POST':
        EmpDataUpdateObj.EmpMobile = request.POST['mobile']
        EmpDataUpdateObj.EmpOccupation = request.POST['occupation']
        EmpDataUpdateObj.EmpIssueState = request.POST['IssuedState']
        print(EmpDataUpdateObj.EmpMobile, EmpDataUpdateObj.EmpOccupation, EmpDataUpdateObj.EmpIssueState)
    EmpDataUpdateObj.save()
    return render(request, 'EmpUpdate.html', mydict)
    # return redirect('/update/')

# Show Data for Delete function
def deleteShow(request):
    EmpDataDeleteObj = EmployeeRecord.objects.all()
    deleteData = {
        'EmpDataDeleteObj':EmpDataDeleteObj
    }
    return render(request, 'delete.html', deleteData)

# Delete function
def delete(request,Emp_id):
    print(Emp_id)
    
    Emp_Del_Obj = get_object_or_404(EmployeeRecord, id=Emp_id)
    Emp_Del_Obj.delete()
    # Emp_Del_Obj = EmployeeRecord.objects.get(pk=Emp_id)
    # Emp_Del_Obj.delete()
    return redirect('/delete/')
 
# Profile function
def profile(request):
    empObj = EmployeeRecord.objects.all()
    data = {
        'empObj': empObj
    }
    return render(request, 'profile.html',data)

# Success function
def success(request):

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        email = request.POST['email']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        occupation = request.POST['occupation']
        idtype = request.POST['Idtype']
        idnumber = request.POST['Idnumber']
        issueauthority = request.POST['IssueAuthority']
        issuestate = request.POST['IssuedState']
        issuedate = request.POST['IssuedDate']
        expirydate = request.POST['ExpiryDate']

        print(name, dob, email, mobile, gender, occupation, idtype, idnumber, issueauthority, issuestate, issuedate,expirydate)

    # creating Employee class object so that we can store the value from input form to database
    EmpDataRecord = EmployeeRecord(EmpName=name, EmpDOB = dob, EmpEmail = email, EmpMobile = mobile, EmpGender = gender, EmpOccupation = occupation, EmpIDType = idtype, EmpIDNumber = idnumber, EmpIssueAuthority = issueauthority,EmpIssueState = issuestate,  EmpIssuedDate = issuedate, EmpExpiryDate = expirydate)
    # save the data
    EmpDataRecord.save()

    return render(request, 'success.html', {})
    # return HttpResponse("<h1>Congratulations!!! Your Registration Successful</h1> <h3> We are feeling great to <b>onboard</b> you </h3>")