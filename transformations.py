from Warriors import Warrior

import Warriors as warrior
import Redcode as redcode
import numpy as np

import re


# Matches a pattern with 
def separate_instruction(instruction) -> list:
    pattern = r"\s*([^\t]+)\t([^\t]+)\t([^\t]+)\t,\t([^\t]+)\t([^\t]+)\n"
    
    match = re.match(pattern, instruction)
    
    if match:
        variable1 = match.group(1)
        variable2 = match.group(2)
        variable3 = match.group(3)
        variable4 = match.group(4)
        variable5 = match.group(5)
    
        instruction = variable1.split('.') + [variable2, variable3, variable4, variable5]
        return instruction
    else:
        print("...")

# receives a list of instructions that have been split, and returns a list of strings
def parse_instructions(instructions: list) -> list:
    insts = []
    for i in instructions:
        insts += [f'\t{i[0]}.{i[1]}\t{i[2]}\t{i[3]}\t,\t{i[4]}\t{i[5]}\n']
    return insts

def change_operation(w: Warrior) -> None:
    instructions = [separate_instruction(i) for i in w.instructions]
    length = len(instructions)
    for i in range(length):
        tmp = np.random.choice(list(redcode.INSTRUCTIONS.keys()))
        instructions[i][0] = tmp
    w.instructions = parse_instructions(instructions)

def change_address_modifier(w: Warrior) -> None:
    address_modes_s = ["$", "#", "@", "<", ">", "*", "{", "}"]
    address_modes_w = [.27, .24, .23, .05, .05, .1, .03, .03]

    instructions = [separate_instruction(i) for i in w.instructions]
    length = len(instructions)
    for i in range(length):
        tmp = np.random.choice(address_modes_s, p=address_modes_w, size=2)
        instructions[i][2] = tmp[0]
        instructions[i][4] = tmp[1]
    w.instructions = parse_instructions(instructions)

def change_instruction_modifer(w: warrior) -> None:
    instruction_modifier_s = ["A", "B", "AB", "BA", "F", "X", "I"]
    
    instructions = [separate_instruction(i) for i in w.instructions]
    length = len(instructions)
    for i in range(length):
        tmp  = np.random.choice(instruction_modifier_s)
        instructions[i][1] = tmp
    w.instructions = parse_instructions(instructions)

def change_sources(w: warrior) -> None:
    instructions = [separate_instruction(i) for i in w.instructions]
    length = len(instructions)
    for i in range(length):
        src = int(np.random.normal(0, length, 1))
        dst = int(np.random.normal(0, length, 1))
        instructions[i][3] = src
        instructions[i][5] = dst
    w.instructions = parse_instructions(instructions)





    
