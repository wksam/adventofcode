import math

class Monkey():
    def __init__(self, name, operation, test, if_true, if_false, items=None) -> None:
        self.name = name
        self.items = []
        if items != None:
            for item in items:
                self.items.append(item)
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0
    
    def get_first_item(self):
        self.inspected += 1
        return self.items.pop(0) if self.has_items() else -1
    
    def has_items(self):
        return len(self.items) > 0
    
    def calculate_worry_level(self, item):
        a, operator, b = self.operation
        a = self.get_operand(a, item)
        b = self.get_operand(b, item)
        return a + b if operator != '*' else a * b
    
    def get_operand(self, operand, item):
        return int(operand) if operand != 'old' else item
    
    def gets_bored(self, item):
        return math.floor(item / 3)
    
    def throw_item_to(self, item):
        return self.if_true if item % self.test == 0 else self.if_false

def read_file(path):
    return open(path).read()

def get_monkeys(file):
    monkey_list = file.split('\n\n')
    monkeys = []
    for monkey_file in monkey_list:
        monkey_file = [m.strip() for m in monkey_file.splitlines()]
        monkey_name = int(monkey_file[0][:-1].split(' ')[-1:].pop())
        monkey_items = [int(item) for item in monkey_file[1][16:].split(', ')]
        monkey_operation = monkey_file[2].split(' ')[-3:]
        monkey_test = int(monkey_file[3].split(' ')[-1:].pop())
        monkey_if_true = int(monkey_file[4].split(' ')[-1:].pop())
        monkey_if_false = int(monkey_file[5].split(' ')[-1:].pop())
        monkey = Monkey(monkey_name, monkey_operation, monkey_test, monkey_if_true, monkey_if_false, monkey_items)
        monkeys.append(monkey)
    return monkeys

def active_monkeys(path):
    file = read_file(path)
    monkeys = get_monkeys(file)
    for _ in range(20):
        for monkey in monkeys:
            while monkey.has_items():
                item = monkey.get_first_item()
                item = monkey.calculate_worry_level(item)
                item = monkey.gets_bored(item)
                m = next((m for m in monkeys if m.name == monkey.throw_item_to(item)), None)
                m.items.append(item)
    
    times_inspected = []
    for monkey in monkeys:
        times_inspected.append(monkey.inspected)
    first_largest = max(times_inspected)
    times_inspected.remove(first_largest)
    second_largest = max(times_inspected)
    return first_largest * second_largest

path = '2022/day_11_monkey_in_the_middle/notes.txt'
print(active_monkeys(path))