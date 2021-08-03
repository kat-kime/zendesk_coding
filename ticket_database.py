# Name:                     Kat Kime
# Date:                     8/2/2021
# Description:              Creates ticket database for the ticket_viewer program.
from ticket import Ticket
from collections import defaultdict
from prettytable import PrettyTable

_MAX_TICKET = 25


class Tickets:
    """
    Class for ticket aggregation objects.
    """
    def __init__(self, data: dict):
        """
        Constructor for Tickets objects. Iterates through list and adds each ticket to a tickets dictionary.
        Args:
            data: Response from Zendesk API tickets request.
        """
        self._tickets = defaultdict(Ticket)

        for i in range(len(data['tickets'])):
            ticket_object = data['tickets'][i]
            ticket = Ticket()

            if ticket_object['id']:
                ticket.set_id(ticket_object['id'])

            if ticket_object['assignee_id']:
                ticket.set_assignee_id(ticket_object['assignee_id'])

            if ticket_object['created_at']:
                ticket.set_created_date(ticket_object['created_at'])

            if ticket_object['description']:
                ticket.set_description(ticket_object['description'])

            if ticket_object['due_at']:
                ticket.set_due_date(ticket_object['due_at'])

            if ticket_object['priority']:
                ticket.set_priority(ticket_object['priority'])

            if ticket_object['requester_id']:
                ticket.set_requester(ticket_object['requester_id'])

            if ticket_object['subject']:
                ticket.set_subject(ticket_object['subject'])

            if ticket_object['status']:
                ticket.set_status(ticket_object['status'])

            if ticket_object['type']:
                ticket.set_type(ticket_object['type'])

            if ticket_object['url']:
                ticket.set_url(ticket_object['url'])

            self._tickets[i + 1] = ticket

    def get_tickets(self) -> dict:
        """
        Returns tickets for user's account.
        Returns: Dictionary containing user's tickets
        """
        return self._tickets

    def display_tickets(self, start_id=1) -> int:
        """
        Prints user's tickets until MAX_TICKET is reached, and returns the id of the last ticket printed.
        Args:
            start_id: Ticket ID to begin printing
        Returns: Int representing id of last ticket printed.
        """
        start = start_id
        table = PrettyTable()
        table.field_names = ["ID", "Status", "Date", "Subject", "Type", "Priority"]

        for i in range(_MAX_TICKET):
            ticket_id = self._tickets[start_id].get_id()
            status = self._tickets[start_id].get_status()
            created_date = self._tickets[start_id].get_created_date()
            subject = self._tickets[start_id].get_subject()
            ticket_type = self._tickets[start_id].get_type()
            priority = self._tickets[start_id].get_priority()
            table.add_row([ticket_id, status, created_date, subject, ticket_type, priority])
            start_id += 1

            if start_id >= len(self._tickets):
                start_id = 1

        print(table)
        if len(self._tickets) > 25:
            print(f"\nTickets {start} - {start_id - 1} are displayed.\nTo see more tickets, use the N command.")

        return start_id

    def get_ticket_details(self, ticket_id: int) -> str:
        """
        Returns a string representing a given ticket's details.
        Args:
            ticket_id: User-defined ticket ID.
        Returns: String representing ticket details.
        """
        if ticket_id >= len(self._tickets):
            return f"\n{ticket_id} is outside the range of current tickets.\n\n\nEnter R to return."

        ticket = self._tickets[ticket_id]
        subject = ticket.get_subject()
        created_date = ticket.get_created_date()
        requester = ticket.get_requester()
        assignee = ticket.get_assignee_id()
        url = ticket.get_url()
        description = ticket.get_description()

        return f"\n\n\n\nSubject: {subject}\nCreated Date: {created_date}\nRequester: {requester}\n" \
               f"Assignee: {assignee}\nURL: {url}\n\nDescription:\n\n{description}\n\n\n\nEnter R to return."

    def view_next_page(self, start_id) -> int:
        """
        Displays the next page of the ticket results.

        Args:
            start_id: First ticket to display

        Returns: ID of the last ticket.

        """
        return self.display_tickets(start_id)

    def execute_command(self, command: str, last_ticket_id: int) -> int:
        """
        Receives user's input command and executes it.
        Args:
            command: User-defined command.
            last_ticket_id: ID of the last ticket displayed.

        Returns: Last ticket id if new page was selected, -1 if otherwise
        """
        last_ticket = last_ticket_id

        if command.lower() == 'v' or command.lower() == 'view':
            instructions = "\nEnter a Ticket ID: \n"

            try:
                ticket_id = int(input(instructions))

                print(self.get_ticket_details(ticket_id))

                user_input = input()

                self.display_tickets()

            except ValueError:
                print("Invalid input. Must enter an integer.")

            return -1

        elif command.lower() == 'n' or command.lower() == 'next':
            last_ticket = self.view_next_page(last_ticket)
            return last_ticket
