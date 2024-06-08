from Config import config

import Redcode as redcode
import numpy as np

import string

# Index:
# generate_instructions()
# generate_instruction()
# class Warrior
#       __init__

# gets the count and program_length and calls generate_instruction. This returns a list of instructions
def generate_instructions(cout: int, program_length: int) ->  list:  
    instructions = []

    for _ in range(cout):
        tmp = np.random.choice(list(redcode.INSTRUCTIONS.keys()))
        
        instructions += [generate_instruction(program_length, tmp)]
    
    return instructions

# generates a single instruction by receiving program_length and the instruction to generate
def generate_instruction(program_length: int, tmp) -> str:
    inst = redcode.INSTRUCTIONS[tmp]
    args = inst["arguments"]

    if args == 1:
        instructions = inst["operation"](program_length)
    else:
        instructions = inst["operation"](program_length, tmp)
    
    return instructions


def generate_name() -> str:
    length = np.random.randint(1, 10)
    return ''.join(np.random.choice(list(string.ascii_letters), size=length))

# __init__
# grade
# sort_by_grade
class Warrior:
    def __init__(self):
        self.instructions = generate_instructions(config.INIT_INSTRUCTIONS, config.INIT_INSTRUCTIONS)
        self.score = 0
        self.name = generate_name()
    
    def grade(self, result: int):
        self.score += result
        if(self.score >= config.MAX_SCORE):
            self.score = config.MAX_SCORE

    def sort_by_fitness(self):
        return self.score

    def restart(self):
        length = len(self.instructions)
        if(length < config.INIT_INSTRUCTIONS):
            length = config.INIT_INSTRUCTIONS
        
        self.instructions = generate_instructions(length, length)
        self.score = 0

    def print_information(self):
        print(f'Name:\t{self.name}')
        print(f'Score:\t{self.score}')
        for i in self.instructions:
            print(i)