from rest_framework import serializers
from modules.leave.models import LeaveApplication, LeaveType

class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = '__all__'
        read_only_fields = ('user_id',)
