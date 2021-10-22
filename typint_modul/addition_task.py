class Directory:
    def __init__(self, name: str, root: dir, files: list, sub_directory: list[dir]):
        self.name = name
        self.root = root
        self.files = files
        self.sub_directory = sub_directory

    @staticmethod
    def add_sub_directory(self, name: str, root: dir, files: list, sub_directory: list[dir]):
        return Directory(name=name, root=root, files=files, sub_directory=sub_directory)

    @staticmethod
    def remove_sub_directory(self, name: str, root: dir, files: list, sub_directory: list[dir]):
        return Directory(name=name, root=None, files=files, sub_directory=sub_directory)

    @staticmethod
    def add_file(self, name: str, direct: dir):
        return File(name=name, direct=direct)

    @staticmethod
    def remove_file(self, name: str, direct: dir):
        return File(name=name, direct=None)


class File:
    def __init__(self, name: str, direct: dir):
        self.name = name
        self.directory = direct


directory: Directory = Directory('python_example.py', '/', ['example'], ['/'])
file: File = File('py.py', 'exam/')
