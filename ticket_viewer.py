# Name:                     Kat Kime
# Date:                     8/1/2021
# Description:              Allows users to access tickets for a given account number.
import requests
import Constants
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
    last_ticket = tickets.display_tickets()

    user_instructions = f"\nSelect an option:\n[V] View Ticket Details   ---   " \
                        f"[N] Next Page   ---   [Q] Quit\n"

    while True:
        user_input = input(user_instructions)

        if user_input.lower() == 'quit' or user_input.lower() == 'q':
            print("\nExiting the Ticket Viewer program...")
            break

        elif user_input.lower() == 'v' or user_input.lower() == 'view' or user_input.lower() == 'n' or \
                user_input.lower() == 'next':
            num = tickets.execute_command(user_input, last_ticket)

            if num >= 0:
                last_ticket = num

        else:
            print("\nCommand not recognized.\n")


if __name__ == "__main__":
    main()
