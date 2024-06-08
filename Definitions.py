import numpy as np
from time import time
from Config import config

"""
The following instructions are generated using the default modifiers for ICWS'88 emulation: https://corewar.co.uk/standards/icws94.htm#6.3.1
"""

"""
   To get the addres mode for the instruction we run:
   np.random.choice(address_modes_s, weights=address_modes_w, k=2) to get two symbols
"""
address_modes_s = ["$", "#", "@", "<", ">", "*", "{", "}"]
address_modes_w = [.27, .24, .23, .05, .05, .1, .03, .03]

instruction_modifier_s = [".A", ".B", ".AB", ".BA", ".F", ".X", ".I"]

np.random.seed(int(time()))

"""
    MOV copies an instruction from one address space to the other.
    This function will receive the length of the program

    The function will create:
      - a random src integer between 0 and the length of the program 
      - a random dst integer between 1 and the length of the address space with normal distribution around the double of the program. This will avoid the probability of the MOV instruction copying an instruction in the program space

    The function will return an instruction in the form of MOV src, dst
"""

def MOV(p_s: int) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=1)
    modf = np.random.choice(["I", "A", "B", "AB"])
    src = np.random.randint(0, p_s)
    dst = int(np.random.normal(p_s*2, config.max_address_space, 1))
    return f'\tMOV.{modf}\t#\t{src}\t,\t{mode[0]}\t{dst}\n'

"""
    ADD, SUB, MUL, DIV, and MOD

    The function will receive the length of the program and the operation string

    The function will:
    - create a random src != 0 between a defined range that considers the length and a constant defined by the user. It will not be zero
    - create a random destination in the program (dst)

    Return any instruction of the form ADD, SUB, MUL, DIV or MOD
"""

def MATH(p_s: int, op: str) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=1)
    modf = np.random.choice(["A", "B", "AB"])
    src = int(np.random.normal(0, p_s+config.MATH_OFFSET, 1))
    if(src == 0): src = 1
    dst = np.random.randint(0, p_s)
    return f'\t{op}.{modf}\t#\t{src}\t,\t{mode[0]}\t{dst}\n'

"""
    JMP
    The function will receive the length of the current program

    The function will generate a random src that will determine where the JMP will go anywhere in the program
"""
def JMP(p_s: int) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=1)
    src = int(np.random.normal(0, p_s, 1))
    return f'\tJMP.B\t{mode[0]}\t{src}\t,\t$\t0\n'

"""
    JMZ and JMN
    The function will receive the length of the current program and the instruction.

    The function will create a source registers anywhere in the program and the destination as well
"""
def JMPZ(p_s: int, op: str) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=2)
    src = int(np.random.normal(0, p_s, 1))
    dst = int(np.random.normal(0, p_s, 1))
    return f'\t{op}.B\t{mode[0]}\t{src}\t,\t{mode[1]}\t{dst}\n'

""" 
    DAT kills any process, it will generate a random dst value to be meddled by any other instruction

    The funciton will receive the length of the program and return the instruction

    
"""
def DAT(p_s:int) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=1)
    dst = np.random.randint(0, p_s)
    return f'\tDAT.F\t$\t0\t,\t{mode[0]}\t{dst}\n'

"""
    SNQ, SNE, SLT

    Creates random src and random dst of th size of the program. This to make
"""
def SKIP(p_s: int, op: str) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=2)
    src = np.random.randint(0, p_s)
    dst = np.random.randint(0, p_s)
    return f'\t{op}.B\t{mode[0]}\t{src}\t,\t{mode[1]}\t{dst}\n'

def DJN(p_s: int) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=1)
    src = int(np.random.normal(0, p_s, 1))
    dst = np.random.randint(0, p_s)
    return f'\tDJN.B\t$\t{src}\t,\t{mode[0]}\t{dst}\n'

def SPL(p_s: int) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=1)
    src = int(np.random.normal(0, p_s+config.MATH_OFFSET, 1))
    if(src == 0): src = 1
    dst = np.random.randint(0, p_s)
    return f'\tSPL.B\t#\t{src}\t,\t{mode[0]}\t{dst}\n'

"""
    NOP
    
    Generates random numbers 
"""
def NOP(p_s: int) -> str:
    mode = np.random.choice(address_modes_s, p=address_modes_w, size=2)
    src = np.random.randint(0, p_s)
    dst = np.random.randint(0, p_s)
    return f'\tNOP.F\t{mode[0]}\t{src}\t,\t{mode[1]}\t{dst}\n'