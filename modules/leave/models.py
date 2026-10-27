from django.db import models
from core.db.mixins import TimeStampedModel, UserScopedModel

class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class LeaveBalance(models.Model):
    user = models.ForeignKey(UserScopedModel, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    balance = models.IntegerField()

class LeaveApplication(models.Model):
    user = models.ForeignKey(UserScopedModel, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(read_only=True)
