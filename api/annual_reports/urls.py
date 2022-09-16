from django.urls import path

from annual_reports.views import ListIncomeStatements, ListBalanceSheetStatements, ListCashFlowStatements


urlpatterns = [
    path('<str:symbol>/income-statement/', ListIncomeStatements.as_view()),
    path('<str:symbol>/balance-sheet-statement/', ListBalanceSheetStatements.as_view()),
    path('<str:symbol>/cash-flow-statement/', ListCashFlowStatements.as_view()),
]
