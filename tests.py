# Name:                 Kat Kime
# Date:                 8/1/2021
# Description:          Tests the ticket viewer program.

import unittest
import ticket_viewer
import ticket_database

"""
Specifications:
-- Connects to the Zendesk API
-- Requests all the tickets for your account
-- Displays tickets in a list
-- Displays individual ticket details
-- Pages through tickets when more than 25 are returned
- Displays a friendly error message if the API is unavailable or the response is
invalid.
-- Tells the user something is wrong if there is a program error.
-- The Ticket Viewer should handle the API being unavailable
"""


class TestCase(unittest.TestCase):

    def test_1_API(self):
        """
        Tests that get_tickets connects to the Zendesk API.
        """
        expected = dict

        self.assertEqual(expected, type(ticket_viewer.get_tickets()))

    def test_2_list(self):
        """
        Tests that display_table prints a table of Zendesk tickets.
        """
        tickets = ticket_database.Tickets(ticket_viewer.get_tickets())
        tickets.display_tickets()

    def test_3_details(self):
        """
        Tests that the ticket viewer creates and returns a string object with user details when prompted.
        """
        tickets = ticket_database.Tickets(ticket_viewer.get_tickets())
        ticket_id = 1
        expected = str

        print(tickets.get_ticket_details(ticket_id))

        self.assertEqual(expected, type(tickets.get_ticket_details(ticket_id)))

    def test_4_next(self):
        """
        Tests that the ticket viewer displays the next page of tickets when prompted.

        """
        # test that final displayed ticket is greater than original ticket
        tickets = ticket_database.Tickets(ticket_viewer.get_tickets())
        start = tickets.display_tickets()
        end = tickets.view_next_page(start)

        expected = True
        self.assertEqual(expected, end - start > 0)

    def test_6_execute_details(self):
        """
        Tests that execute_command() returns -1 when view details is selected

        """
        command = 'view'
        ticket_id = 5
        expected = -1

        tickets = ticket_database.Tickets(ticket_viewer.get_tickets())

        self.assertEqual(expected, tickets.execute_command(command, ticket_id))

    def test_7_excute_next(self):
        """
        Tests that execute_command() returns a number greater than -1 when view details is selected

        """
        command = 'next'
        ticket_id = 5
        expected = True

        tickets = ticket_database.Tickets(ticket_viewer.get_tickets())

        self.assertEqual(expected, tickets.execute_command(command, ticket_id) > ticket_id)

    def test_5_bad_API(self):
        """
        Tests that the ticket viewer displays an error and exits when the API cannot be reached.
        NOTE: Constraints.AUTHORIZATION_KEY must be changed to an invalid code.

        """
        tickets = ticket_viewer.get_tickets()
        expected = None

        self.assertEqual(expected, tickets)

