# Name:                     Kat Kime
# Date:                     8/2/2021
# Description:              Creates Ticket objects for the ticket_viewer program.

class Ticket:
    """
    Class representing individual tickets.
    """
    def __init__(self):
        """
        Constructor for Ticket objects.
        """
        self._id = None
        self._assignee_id = None
        self._created_date = None
        self._description = None
        self._due_date = None
        self._priority = None
        self._requester = None
        self._subject = None
        self._status = None
        self._type = None
        self._url = None

    def get_id(self) -> int:
        return self._id

    def get_assignee_id(self) -> int:
        return self._assignee_id

    def get_created_date(self) -> str:
        return self._created_date

    def get_description(self) -> str:
        return self._description

    def get_due_date(self) -> str:
        return self._due_date

    def get_priority(self) -> str:
        return self._priority

    def get_requester(self) -> int:
        return self._requester

    def get_subject(self) -> str:
        return self._subject

    def get_status(self) -> str:
        return self._status

    def get_type(self) -> str:
        return self._type

    def get_url(self) -> str:
        return self._url

    def set_id(self, ticket_id) -> None:
        self._id = ticket_id

    def set_assignee_id(self, assignee_id: str) -> None:
        self._assignee_id = assignee_id

    def set_created_date(self, created_date: str) -> None:
        self._created_date = created_date

    def set_description(self, description: str) -> None:
        self._description = description

    def set_due_date(self, due_date: str) -> None:
        self._due_date = due_date

    def set_priority(self, priority: str) -> None:
        self._priority = priority

    def set_requester(self, requester: int) -> None:
        self._requester = requester

    def set_subject(self, subject: str) -> None:
        self._subject = subject

    def set_status(self, status: str) -> None:
        self._status = status

    def set_type(self, ticket_type: str) -> None:
        self._type = ticket_type

    def set_url(self, url: str) -> None:
        self._url = url
