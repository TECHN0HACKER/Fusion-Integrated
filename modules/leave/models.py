from django.db import models
from core.db.mixins import TimeStampedModel, UserScopedModel

class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class LeaveBalance(TimeStampedModel, UserScopedModel):
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    balance = models.IntegerField()

class LeaveApplication(TimeStampedModel, UserScopedModel):
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
