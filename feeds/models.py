class News:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.link = kwargs.get('link')

        self.source = None
