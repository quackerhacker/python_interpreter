bytecode = {
    "instructions": [
        ("LOAD_VALUE", 0), # the first number
        ("LOAD_VALUE", 1), # the second number
        ("ADD_TWO_VALUES", None),
        ("LOAD_VALUE", 2),
        ("ADD_TWO_VALUES", None),
        ("PRINT_ANSWER", None)],
    "numbers": [7, 10, 8]
}

class Interpreter:
    def __init__(self):
        self.stack = []

    def load_value(self, number):
        self.stack.append(number)

    def print_answer(self):
        answer = self.stack.pop()
        print(answer)

    def add_two_values(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def run_code(self, bytecode):
        instructions = bytecode["instructions"]
        numbers = bytecode["numbers"]

        for each_step in instructions:
            instruction, argument = each_step

            if instruction == "LOAD_VALUE":
                number = numbers[argument]
                self.load_value(number)
            elif instruction == "ADD_TWO_VALUES":
                self.add_two_values()
            elif instruction == "PRINT_ANSWER":
                self.print_answer()
