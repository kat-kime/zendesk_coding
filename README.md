# Zendesk Ticket Viewer
===

## Table of Contents
1. [Overview](#Overview)
2. [System Requirements](#Requirements)
3. [Running the Program](#Running-Program)
4. [User Specifications](#User-Specifications)

## Overview
The Zendesk Ticket Viewer is a command-line appliction that was developed as a submission to the 2021 Zendesk Coding Challenge. It allows users to:

- Request all company tickets
- View individual ticket details
- Get a bird's eye view of tickets at 25-item intervals


If you would like to demo this application, follow the instructions below:

## System Requirements
To successfully run this application, you will need the following resources:

- **A Copy of this Application.** To copy this application to your machine, use the command line to 'cd' to your desired location and enter the following: `git clone https://github.com/kat-kime/zendesk_coding.git`

- **Python:** To download the latest version of Python, [visit Python.org](https://www.python.org/downloads/).
- **Authorization Code:** This application uses an OAuth token to confirm authorization. To get yours, [follow Zendesk's instructions here](https://support.zendesk.com/hc/en-us/articles/203663836).
- **Constants.py:** This program relies on a Constants.py file to store secret information. Create your own and add the following variables:
  - AUTHORIZATION_KEY = "{insert OAuth token}"
  - DOMAIN = "{your Zendesk domain}"
  - REDIRECT_URI = "{Redirect URI}"
- [Optional] **Sample Tickets:** To generate your own, use the included tickets.json file and the following curl command:
`curl https://{subdomain}.zendesk.com/api/v2/imports/tickets/create_many.json -v -u
{email_address}:{password} -X POST -d @tickets.json -H "Content-Type:
application/json"`

## Running the Program
To run the program, `cd` to the program's directory and run the following command:

`python3 ticket_viewer.py`

A menu will appear with brief instructions to help you navigate the application. Enjoy the positive customer support vibes while you're there!

## User Specifications
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





