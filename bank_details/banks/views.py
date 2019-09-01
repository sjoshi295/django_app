from banks.models import BankName, BankData
from banks.serializers import BankBranchSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class BankList(generics.ListAPIView):
    serializer_class = BankBranchSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        ifsc = self.request.query_params.get('ifsc', None)
        bank_name = self.request.query_params.get('bank', None)
        city = self.request.query_params.get('city', None)
        if ifsc is not None:
            bank_list = BankData.objects.filter(ifsc=ifsc)
        else:
            bank = BankName.objects.get(bank_name=bank_name)
            bank_list = BankData.objects.filter(bank=bank.id, city=city)
        return bank_list
