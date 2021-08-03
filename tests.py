# Name:                 Kat Kime
# Date:                 8/1/2021
# Description:          Tests the ticket viewer program.

import unittest
import ticket_viewer

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
