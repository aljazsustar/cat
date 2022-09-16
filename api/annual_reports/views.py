import datetime
import json
import os

import requests
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.core import serializers

from annual_reports.models import IncomeStatement
from annual_reports.serializers import IncomeStatementSerializer, BalanceSheetStatementSerializer, CashFlowStatementSerializer
from annual_reports.models import BalanceSheetStatement, CashFlowStatement
from indicators.models import Indicator


class ListIncomeStatements(ListAPIView):
    serializer_class = IncomeStatementSerializer
    queryset = IncomeStatement.objects.all()

    def get(self, request, *args, **kwargs):
        symbol_id = Indicator.objects.filter(symbol=kwargs['symbol']).first().id
        income_statements = IncomeStatement.objects.filter(symbol=symbol_id).all()

        if income_statements.count() == 0:
            self.fetch_financial_statements(kwargs['symbol'], symbol_id)
            income_statements = IncomeStatement.objects.filter(symbol=symbol_id).all()

        return Response(status=status.HTTP_200_OK, data=IncomeStatementSerializer(income_statements, many=True).data)

    @staticmethod
    def fetch_financial_statements(symbol, symbol_id):
        req_income_statement = requests.get(
            f'{os.environ.get("ANNUAL_REPORTS_URL")}income-statement/{symbol}?apikey={os.environ.get("ANNUAL_REPORTS_API_KEY")}')
        req_balance_sheet = requests.get(
            f'{os.environ.get("ANNUAL_REPORTS_URL")}balance-sheet-statement/{symbol}?apikey={os.environ.get("ANNUAL_REPORTS_API_KEY")}')
        req_cash_flow = requests.get(
            f'{os.environ.get("ANNUAL_REPORTS_URL")}cash-flow-statement/{symbol}?apikey={os.environ.get("ANNUAL_REPORTS_API_KEY")}')

        for income, balance, cash in zip(req_income_statement.json(), req_balance_sheet.json(), req_cash_flow.json()):

            indicator = Indicator.objects.filter(id=symbol_id).first()
            income['symbol'] = indicator
            balance['symbol'] = indicator
            cash['symbol'] = indicator

            for key, value in income.items():
                try:
                    dt = datetime.datetime.strptime(value.split()[0], '%Y-%m-%d').date()
                    income[key] = dt
                except Exception as e:
                    pass

            for key, value in balance.items():
                try:
                    dt = datetime.datetime.strptime(value.split(' ')[0], '%Y-%m-%d').date()
                    balance[key] = dt
                except Exception as e:
                    pass

            for key, value in cash.items():
                try:
                    dt = datetime.datetime.strptime(value.split()[0], '%Y-%m-%d').date()
                    cash[key] = dt
                except Exception as e:
                    pass

            new_income_statement = IncomeStatement(**income)
            new_balance_statement = BalanceSheetStatement(**balance)
            new_cash_statement = CashFlowStatement(**cash)

            new_income_statement.save()
            new_balance_statement.save()
            new_cash_statement.save()


class ListBalanceSheetStatements(ListAPIView):
    serializer_class = BalanceSheetStatementSerializer
    queryset = BalanceSheetStatement.objects.all()

    def get(self, request, *args, **kwargs):
        symbol_id = Indicator.objects.filter(symbol=kwargs['symbol']).first().id
        income_statements = BalanceSheetStatement.objects.filter(symbol=symbol_id).all()

        if income_statements.count() == 0:
            ListIncomeStatements.fetch_financial_statements(kwargs['symbol'], symbol_id)
            income_statements = BalanceSheetStatement.objects.filter(symbol=symbol_id).all()

        return Response(status=status.HTTP_200_OK,
                        data=BalanceSheetStatementSerializer(income_statements, many=True).data)


class ListCashFlowStatements(ListAPIView):
    serializer_class = CashFlowStatementSerializer
    queryset = CashFlowStatement.objects.all()

    def get(self, request, *args, **kwargs):
        symbol_id = Indicator.objects.filter(symbol=kwargs['symbol']).first().id
        income_statements = CashFlowStatement.objects.filter(symbol=symbol_id).all()

        if income_statements.count() == 0:
            ListIncomeStatements.fetch_financial_statements(kwargs['symbol'], symbol_id)
            income_statements = CashFlowStatement.objects.filter(symbol=symbol_id).all()

        return Response(status=status.HTTP_200_OK, data=CashFlowStatementSerializer(income_statements, many=True).data)
