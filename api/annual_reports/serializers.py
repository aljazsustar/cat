from rest_framework import serializers

from annual_reports.models import IncomeStatement, BalanceSheetStatement, CashFlowStatement


class IncomeStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeStatement
        fields = '__all__'
        read_only_fields = ('id', )


class BalanceSheetStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = BalanceSheetStatement
        fields = '__all__'
        read_only_fields = ('id', )


class CashFlowStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashFlowStatement
        fields = '__all__'
        read_only_fields = ('id', )
