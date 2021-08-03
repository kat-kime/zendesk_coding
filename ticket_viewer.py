# Name:                     Kat Kime
# Date:                     8/1/2021
# Description:              Allows users to access tickets for a given account number.
import requests
import Constants
import ticket_database

_AUTHORIZATION = Constants.AUTHORIZATION_KEY
_DOMAIN = Constants.DOMAIN


def get_tickets(authorization, domain) -> dict:
    """
    Connects with the Zendesk API to receive tickets for a given account.
    Args:
        authorization: Zendesk authorization code
        domain: Domain for the Zendesk company

    Returns:

    """
    tickets_url = f"https://{domain}.zendesk.com/api/v2/tickets.json"
    headers = {"Authorization": f"Bearer {authorization}"}
    r = requests.get(tickets_url, headers=headers)

    if r.status_code != requests.codes.ok:
        data = None
        print("Error:", r.status_code)

    else:
        data = r.json()

    return data


def launch_ticket_viewer(data):
    if data:
        print("********** ZENDESK TICKET VIEWER **********\nAre you ready for some customer support? View your following "
              "tickets and use the menu below to get started.\n")
        tickets = ticket_database.Tickets(data)
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
    else:
        print("Error: Could not retrieve tickets at this time. Please check with your system administrator.")


def main():
    authorization = Constants.AUTHORIZATION_KEY
    domain = Constants.DOMAIN

    data = get_tickets(authorization, domain)

    if data is not None:
        launch_ticket_viewer(data)
        return 1

    else:
        print("Error: Could not retrieve tickets at this time. Please check with your system administrator.")
        return -1


if __name__ == "__main__":
    main()
