# Name:                 Kat Kime
# Date:                 8/1/2021
# Description:          Tests the ticket viewer program.

import unittest
import ticket_viewer
import ticket_database
import Constants

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
        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN
        expected = dict

        self.assertEqual(expected, type(ticket_viewer.get_tickets(authorization, domain)))

    def test_2_list(self):
        """
        Tests that display_table prints a table of Zendesk tickets.
        """
        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN
        tickets = ticket_database.Tickets(ticket_viewer.get_tickets(authorization, domain))
        tickets.display_tickets()

    def test_3_details(self):
        """
        Tests that the ticket viewer creates and returns a string object with user details when prompted.
        """
        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN

        tickets = ticket_database.Tickets(ticket_viewer.get_tickets(authorization, domain))
        ticket_id = 1
        expected = str

        print(tickets.get_ticket_details(ticket_id))

        self.assertEqual(expected, type(tickets.get_ticket_details(ticket_id)))

    def test_4_next(self):
        """
        Tests that the ticket viewer displays the next page of tickets when prompted.

        """
        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN

        # test that final displayed ticket is greater than original ticket
        tickets = ticket_database.Tickets(ticket_viewer.get_tickets(authorization, domain))
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

        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN

        tickets = ticket_database.Tickets(ticket_viewer.get_tickets(authorization, domain))

        self.assertEqual(expected, tickets.execute_command(command, ticket_id))

    def test_7_excute_next(self):
        """
        Tests that execute_command() returns a number greater than -1 when view details is selected

        """
        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN

        command = 'next'
        ticket_id = 5
        expected = True

        tickets = ticket_database.Tickets(ticket_viewer.get_tickets(authorization, domain))

        self.assertEqual(expected, tickets.execute_command(command, ticket_id) > ticket_id)

    def test_5_bad_API(self):
        """
        Tests that the ticket viewer displays an error and exits when the API cannot be reached.

        """
        authorization = "bad key"
        domain = Constants.DOMAIN
        tickets = ticket_viewer.get_tickets(authorization, domain)
        expected = None

        self.assertEqual(expected, tickets)

    def test_9_good_data(self):
        """
        Tests that program runs successfully when good data is given.

        """
        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN

        tickets = ticket_database.Tickets(ticket_viewer.get_tickets(authorization, domain))

    def test_10_bad_ticket_number(self):
        """
        Tests that program responds accordingly when user feeds a number that's larger than database

        """
        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN
        n = 1000

        tickets = ticket_database.Tickets(ticket_viewer.get_tickets(authorization, domain))
        tickets.get_ticket_details(n)

    def test_11_bad_data_input(self):
        """
        Tests that exception is caught when user enters invalid ticket id.
        """
        authorization = Constants.AUTHORIZATION_KEY
        domain = Constants.DOMAIN
        command = 'view'
        tid = 5
        n = 'stuff'

        tickets = ticket_database.Tickets(ticket_viewer.get_tickets(authorization, domain))
        tickets.execute_command(command, tid)


