import json
import os

from django.core.management.base import BaseCommand
import requests

from indicators.models import Indicator

URL = 'https://financialmodelingprep.com/api/v3/available-traded/list'


class Command(BaseCommand):

    def handle(self, *args, **options):
        json_data = self.get_data()

        for indicator in json_data:
            self.stdout.write(f"Saving data for {indicator['symbol']}")
            new_indicator = Indicator(symbol=indicator['symbol'], company_name=indicator['name'])
            new_indicator.save()

    def get_data(self):
        self.stdout.write("Getting indicator data")
        request = requests.get(f'{URL}?apikey={os.environ.get("ANNUAL_REPORTS_API_KEY")}')
        return request.json()

