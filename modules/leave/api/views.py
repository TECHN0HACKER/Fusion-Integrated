from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from modules.leave.models import LeaveApplication, LeaveType, LeaveBalance
from modules.leave.serializers import LeaveApplicationSerializer, LeaveTypeSerializer, LeaveBalanceSerializer

class LeaveApplicationListView(generics.ListCreateAPIView):
    serializer_class = LeaveApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveApplication.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

class LeaveApplicationDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = LeaveApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveApplication.objects.filter(user_id=self.request.user.id)

class LeaveTypeListView(generics.ListAPIView):
    serializer_class = LeaveTypeSerializer
    permission_classes = [IsAuthenticated]

class LeaveBalanceListView(generics.ListAPIView):
    serializer_class = LeaveBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveBalance.objects.filter(user_id=self.request.user.id)
