class Ticket(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.summary = kwargs.get('summary')
        self.description = kwargs.get('description')
        self.type = kwargs.get('type')
        self.project = kwargs.get('project')

    def __str__(self):
        return "{}: {}".format(self.id, self.summary)
