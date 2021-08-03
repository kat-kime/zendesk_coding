# Name:                     Kat Kime
# Date:                     8/1/2021
# Description:              Allows users to access tickets for a given account number.
import requests
import Constants
from prettytable import PrettyTable
from collections import defaultdict

_AUTHORIZATION = Constants.AUTHORIZATION_KEY
_DOMAIN = Constants.DOMAIN


class Tickets:
    def __init__(self, data: dict):
        self._tickets = defaultdict(dict)

        for ticket in data['tickets']:
            self._tickets[ticket['id']] = ticket

    def get_tickets(self) -> dict:
        return self._tickets

    def display_tickets(self) -> None:
        table = PrettyTable()
        table.field_names = ["ID", "Status", "Date", "Subject", "Type", "Priority"]

        for i in range(1, 26):
            id = self._tickets[i]['id']
            status = self._tickets[i]['status']
            date = self._tickets[i]['created_at']
            subject = self._tickets[i]['subject']
            type = self._tickets[i]['type']
            priority = self._tickets[i]['priority']
            table.add_row([id, status, date, subject, type, priority])

        print(table)


def get_tickets() -> dict:
    tickets_url = f"https://{_DOMAIN}.zendesk.com/api/v2/tickets.json"
    headers = {"Authorization": f"Bearer {_AUTHORIZATION}"}
    r = requests.get(tickets_url, headers=headers)

    if r.status_code != requests.codes.ok:
        data = r.status_code
        print("Error:", r.status_code)

    else:
        data = r.json()

    return data


def main():
    pass


if __name__ == "__main__":
    main()
