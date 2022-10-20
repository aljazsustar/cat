from django.urls import path

from annual_reports.views import ListIncomeStatements, ListBalanceSheetStatements, ListCashFlowStatements


urlpatterns = [
    path('<str:symbol>/income-statements/', ListIncomeStatements.as_view()),
    path('<str:symbol>/balance-sheet-statements/', ListBalanceSheetStatements.as_view()),
    path('<str:symbol>/cash-flow-statements/', ListCashFlowStatements.as_view()),
]
