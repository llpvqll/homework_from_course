import shelve


class LinksDB:

    def __init__(self):
        self._links = {}

    @staticmethod
    def get_link(name):
        with shelve.open('database') as db:
            name = db[name]
            return name

    def set_link(self, name, url):

        if not name:
            raise KeyError('Link name cannot be empty!', name)
        if not url:
            raise ValueError('Invalid link URL!', url)
        if name in self._links:
            raise KeyError("Name already exists!", name)

        self._links[name] = url

        with shelve.open('database') as db:
            db[name] = url

