# Name:                     Kat Kime
# Date:                     8/1/2021
# Description:              Allows users to access tickets for a given account number.
import requests
import Constants
from collections import defaultdict
import ticket_database

_AUTHORIZATION = Constants.AUTHORIZATION_KEY
_DOMAIN = Constants.DOMAIN


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
    tickets = ticket_database.Tickets(get_tickets())
    tickets.display_tickets()

    user_instructions = f"\nSelect an option:\n[V] View Ticket Details   ---   " \
                        f"[N] Next Page   ---   [Q] Quit\n"

    while True:
        user_input = input(user_instructions)

        if user_input.lower() == 'quit' or user_input.lower() == 'q':
            print("\nExiting the Ticket Viewer program...")
            break

        else:
            tickets.execute_command(user_input)


if __name__ == "__main__":
    main()
