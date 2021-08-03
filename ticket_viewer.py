# Name:                     Kat Kime
# Date:                     8/1/2021
# Description:              Allows users to access tickets for a given account number.
import requests
import Constants

_AUTHORIZATION = Constants.AUTHORIZATION_KEY
_DOMAIN = Constants.DOMAIN


def get_tickets():
    tickets_url = f"https://{_DOMAIN}.zendesk.com/api/v2/tickets.json"
    headers = {"Authorization": f"Bearer {_AUTHORIZATION}"}
    r = requests.get(tickets_url, headers=headers)

    if r.status_code != requests.codes.ok:
        data = r.status_code
        print("Error:", r.status_code)

    else:
        data = r.json()

    return data


def display_tickets():
    pass


def main():
    pass


if __name__ == "__main__":
    main()