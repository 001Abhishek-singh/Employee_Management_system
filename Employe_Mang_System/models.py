from django.db import models

# Create your models here.
class EmployeeRecord(models.Model):
    EmpName = models.CharField(max_length = 250)
    EmpDOB = models.CharField(max_length=200)
    EmpEmail = models.EmailField(unique=True)
    EmpMobile = models.IntegerField(default=0)
    EmpGender = models.CharField(max_length=200)
    EmpOccupation = models.CharField(max_length=250)
    EmpIDType = models.CharField(max_length=200)
    EmpIDNumber = models.CharField(max_length=250, unique=True)
    EmpIssueAuthority = models.CharField(max_length=200)
    EmpIssueState = models.CharField(max_length=200)
    EmpIssuedDate = models.CharField(max_length=230)
    EmpExpiryDate = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.EmpIDNumber



