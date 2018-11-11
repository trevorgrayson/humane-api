from tkts import tkts

from tkts.models import Ticket

class TestTkts(object):

    def test_writes_ticket(self):
        ticket = tkts.create_issue("this is a summary", '', '', '', [])

        assert isinstance(ticket, Ticket)

    def test_get_ticket(self):
        assert isinstance(tkts.get_issue(1), Ticket)

    def test_lists_ticket(self):
        assert isinstance(tkts.get_list(), list)
