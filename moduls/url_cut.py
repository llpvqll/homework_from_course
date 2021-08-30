

class LinksDB:

    def __init__(self):
        self._links = {}

    def get_link(self, name):

        return self._links[name]

    def set_link(self, name, url):

        if not name:
            raise KeyError('Link name cannot be empty!', name)
        if not url:
            raise ValueError('Invalid link URL!', url)
        if name in self._links:
            raise KeyError("Name already exists!", name)

        self._links[name] = url
