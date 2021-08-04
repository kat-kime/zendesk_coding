# Zendesk Ticket Viewer
===

<img src="https://github.com/kat-kime/zendesk_coding/blob/main/ticket_viewer_walk_3.gif" width = "600">

## Table of Contents
1. [Overview](#Overview)
2. [System Requirements](#System-Requirements)
3. [Running the Program](#Running-the-Program)
4. [Software Features](#Software-Specs)
5. [Ticket Viewer in Action](#Ticket-Viewer-in-Action)

## Overview
The Zendesk Ticket Viewer is a command-line application that was developed as a submission to the 2021 Zendesk Coding Challenge. It allows users to:

- Request all company tickets
- View individual ticket details
- Get a bird's eye view of tickets at 25-item intervals


If you would like to demo this application, follow the instructions below:

## System Requirements
To successfully run this application, you will need the following resources:

- **A Copy of this Application.** To copy this application to your machine, use the command line to `cd` to your desired location and enter the following: `git clone https://github.com/kat-kime/zendesk_coding.git`

- **Python:** To download the latest version of Python, [visit Python.org](https://www.python.org/downloads/).
- **Authorization Code:** This application uses an OAuth token to confirm authorization. To get yours, [follow Zendesk's instructions here](https://support.zendesk.com/hc/en-us/articles/203663836).
- **Constants.py:** This program relies on a Constants.py file to store secret information. Create your own and add the following variables:
  - AUTHORIZATION_KEY = "{insert OAuth token}"
  - DOMAIN = "{your Zendesk domain}"
  - REDIRECT_URI = "{Redirect URI}"
- **PrettyTable:** To download [the PrettyTable module](https://pypi.org/project/prettytable/) that displays content in tables, use the following command: `pip3 install prettytable`
- **Unit Testing Framework:** To run the `tests.py` program, you will need to import [the unittest module](https://docs.python.org/3/library/unittest.html).
- [Optional] **Sample Tickets:** To generate your own, use the included tickets.json file and the following curl command:
`curl https://{subdomain}.zendesk.com/api/v2/imports/tickets/create_many.json -v -u
{email_address}:{password} -X POST -d @tickets.json -H "Content-Type:
application/json"`

## Running the Program
To run the program, `cd` to the program's directory and run the following command:

`python3 ticket_viewer.py`

A menu will appear with brief instructions to help you navigate the application. Enjoy the positive customer support vibes while you're there!

## Software Specs
The following requirements were set by the user (Zendesk) and met by the Ticket Viewer application:

- Connects to the Zendesk API
- Requests all the tickets for your account
- Displays tickets in a list
- Displays individual ticket details
- Pages through tickets when more than 25 are returned
- Displays a friendly error message if the API is unavailable or the response is
invalid.
- Tells the user something is wrong if there is a program error.
- The Ticket Viewer should handle the API being unavailable

## Ticket Viewer in Action
The following are screenshots to help you get a feel of how the program works:

### Welcome Screen
As the program starts, it calls the Zendesk API to request all tickets, then displays the tickets in a table. Users can navigate the application by using the input-based menu.

<img width="740" alt="welcome_screen" src="https://user-images.githubusercontent.com/44751576/127990953-4a7bf48a-ae31-483d-9cde-98e65a65c701.png">


### Individual Tickets
On command, the application presents curated ticket details to the user, with a URL to help users get an even closer look at a ticket's information.

<img width="740" alt="individual_ticket" src="https://user-images.githubusercontent.com/44751576/127991002-bc12f93c-cc22-422d-9c8f-4c28f11b8aca.png">

### User Error
Upon receiving invalid inputs, the ticket viewer will handle exceptions and instruct the user on how to provide valid inputs.

<img width="740" alt="error_handling_1" src="https://user-images.githubusercontent.com/44751576/127991022-86c113bf-182c-4ca2-980d-deb0b28e0864.png">

<img width="740" alt="error_handling_2" src="https://user-images.githubusercontent.com/44751576/127991042-bb7a546f-6d4b-4546-8204-14606f8c0827.png">







