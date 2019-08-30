from banks.models import BankName, BankData
from banks.serializers import BankBranchSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class BankUsingIFSC(generics.ListAPIView):
    serializer_class = BankBranchSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        bank_list = BankData.objects.filter(ifsc=self.kwargs['ifsc'])
        return bank_list


class BankListUsingNameCity(generics.ListAPIView):
    serializer_class = BankBranchSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        bank = BankName.objects.get(bank_name=self.kwargs['bank_name'])
        bank_list = BankData.objects.filter(bank=bank.id, city=self.kwargs['city'])
        return bank_list
