def read_file(path):
    return open(path).read()

class Directory:
    def __init__(self, name, parent=None, subdirectories=None) -> None:
        self.name = name
        self.total_size = 0
        self.parent = parent
        self.files = []
        self.subdirectories = []
        if subdirectories != None:
            for child in subdirectories:
                self.subdirectories.append(child)
    
    def change_directory(self, name):
        for child in self.subdirectories:
            if child.name == name:
                return child
        return None

    def back_directory(self):
        self.parent.total_size += self.total_size
        return self.parent
    
    def create_directory(self, name):
        directory = Directory(name, parent=self)
        self.subdirectories.append(directory)
    
    def create_file(self, name, size):
        file = File(name, size)
        self.total_size += size
        self.files.append(file)

class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

def format_input(input):
    return ('\n' + input).split('\n$ ')[1:]

def directory_size(path):
    file = read_file(path)
    commands = format_input(file)
    directory = organize_directories(commands)
    return sum_all_directory_under_100000(directory)

def organize_directories(commands):
    current_directory = Directory('/')
    for cmd in commands:
        io = cmd.split('\n')
        input = io[0].split(' ')
        outputs = io[1:]

        if input[0] == 'cd':
            if input[1] == '..':
                current_directory = current_directory.back_directory()
            else:
                if input[1] != '/':
                    current_directory = current_directory.change_directory(input[1])
                    if current_directory == None:
                        print('This directory does not exist: ', input[1])
        elif input[0] == 'ls':
            for output in outputs:
                description = output.split(' ')
                if description[0] == 'dir':
                    current_directory.create_directory(description[1])
                else:
                    current_directory.create_file(description[1], int(description[0]))
    while current_directory.parent != None:
        current_directory = current_directory.back_directory()
    return current_directory

def sum_all_directory_under_100000(directory):
    sum = 0
    if directory.total_size <= 100000:
        sum += directory.total_size
    for subdirectory in directory.subdirectories:
        sum += sum_all_directory_under_100000(subdirectory)
    return sum

path = '2022/day_7_no_space_left_on_device/terminal_output.txt'
print(directory_size(path))