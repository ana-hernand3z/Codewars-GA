import Definitions as d

INSTRUCTIONS = {
    "DAT":{
        "operation":d.DAT,
        "arguments": 1
    },
    "SPL":{
        "operation": d.SPL,
        "arguments": 1
    },
    "MOV":{
        "operation": d.MOV,
        "arguments": 1
    },
    "DJN":{
        "operation": d.DJN,
        "arguments": 1
    },
    "ADD":{
        "operation":d.MATH,
        "arguments": 2
    },
    "JMZ":{
        "operation":d.JMPZ,
        "arguments": 2
    },
    "SUB":{
        "operation":d.MATH,
        "arguments": 2
    },
    "MOD":{
        "operation":d.MATH,
        "arguments": 2
    },
    "SEQ":{
        "operation":d.SKIP,
        "arguments": 2
    },
    "JMP":{
        "operation": d.JMP,
        "arguments": 1
    },
    "JMN":{
        "operation":d.JMPZ,
        "arguments": 2
    },
    "SNE":{
        "operation":d.SKIP,
        "arguments": 2
    },
    "MUL":{
        "operation":d.MATH,
        "arguments": 2
    },
    "DIV":{
        "operation":d.MATH,
        "arguments": 2
    },
    "SLT":{
        "operation":d.SKIP,
        "arguments": 2
    },
    "NOP":{
        "operation": d.NOP,
        "arguments": 1
    }
}

CHALLENGER = {
    0: "imp.rc"
}