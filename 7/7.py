from main import get_input_data, results

file_system = None


class File:
    def __init__(self, name, size=None):
        self.name = name
        if size:
            self.size = size


class Directory(File):
    def __init__(self, name, parent=None):
        super().__init__(name)
        self.files = []
        self.parent = parent

    @property
    def size(self):
        return sum([f.size for f in self.files])


class FileSystem:
    def __init__(self):
        self.root = Directory('/')
        self.pwd = self.root


def _init_file_system():
    global file_system
    file_system = FileSystem()

    i = 0
    while i < len(data):
        assert data[i].startswith('$ ')
        command = data[i][2:]
        if command.startswith('cd '):
            new_dir = command[3:]
            if new_dir == '..':
                file_system.pwd = file_system.pwd.parent
            elif new_dir == '/':
                file_system.pwd = file_system.root
            else:
                found = False
                for f in file_system.pwd.files:
                    if f.name == new_dir:
                        file_system.pwd = f
                        found = True
                        break
                if not found:
                    raise Exception(
                        f"Did not find {new_dir} in {file_system.pwd.name}: {[f.name for f in file_system.pwd.files]}")
            i += 1
        elif command == 'ls':
            i += 1
            while i < len(data) and not data[i].startswith('$'):
                file_info = data[i].split(' ')
                if file_info[0] == 'dir':
                    file_system.pwd.files.append(Directory(file_info[1], parent=file_system.pwd))
                else:
                    file_system.pwd.files.append(File(file_info[1], size=int(file_info[0])))
                i += 1
            pass
        else:
            raise ValueError


def _all_dirs():
    global file_system

    def _find_sub_dirs(dir):
        for f in dir.files:
            if isinstance(f, Directory):
                all_dirs.append(f)
                _find_sub_dirs(f)

    all_dirs = [file_system.root]
    _find_sub_dirs(file_system.root)
    return all_dirs


def _sum_smallest_directories():
    global file_system

    return sum([d.size for d in _all_dirs() if d.size <= 100000])


def _size_dir_to_delete():
    TOTAL_DISK_SPACE = 70000000
    TOTAL_SPACE_NEEDED = 30000000
    for d in sorted(_all_dirs(), key=lambda x: x.size):
        if d.size >= TOTAL_SPACE_NEEDED - (TOTAL_DISK_SPACE - file_system.root.size):
            return d.size


def first():
    _init_file_system()
    return _sum_smallest_directories()


def second():
    return _size_dir_to_delete()


data = get_input_data()
results(first, second)
