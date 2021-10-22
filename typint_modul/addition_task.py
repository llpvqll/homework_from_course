class Directory:
    def __init__(self, name: str, root: dir, files: list, sub_directory: list[dir]):
        self.name = name
        self.root = root
        self.files = files
        self.sub_directory = sub_directory


class File:
    def __init__(self, name: str, direct: dir):
        self.name = name
        self.directory = direct


def add_sub_directory(name: str, root: dir, files: list, sub_directory: list[dir]) -> Directory:
    return Directory(name=name, root=root, files=files, sub_directory=sub_directory)


def remove_sub_directory(name: str, root: dir, files: list, sub_directory: list[dir]) -> Directory:
    return Directory(name=name, root=None, files=files, sub_directory=sub_directory)


def add_file(name: str, direct: dir) -> File:
    return File(name=name, direct=direct)


def remove_file(name: str, direct: dir) -> File:
    return File(name=name, direct=None)


directory: Directory = add_sub_directory('python_example.py', '/', ['example'], ['/'])
file: File = add_file('py.py', 'exam/')
