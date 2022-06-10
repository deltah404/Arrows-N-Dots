from curses import raw
from turtle import position
from os import get_terminal_size
import numpy as np
import exceptions as exc
import time
import json


class Interpreter:
    def __init__(self):
        self.tape = np.full(32, 0)
        self.pointer = 0
        self.line = 1
        self.col = 1
        self.position = 0
        with open('./config.json', 'r') as fp:
            f = json.load(fp)
            self.commands = f["operations"]
            self.speed = f["speed"]

    def evaluate(self, script: str):
        raw_script = ""
        res = ""
        time_to_add = 0
        for c in script:
            if c in self.commands:
                raw_script += c
        for c in script:
            width = get_terminal_size()[0]
            self.col += 1
            self.position += 1
            command_out = ""

            if c not in self.commands:
                if c == "\n":
                    self.line += 1
                    self.col = 1
                continue

            if c == ">":
                if self.pointer == len(self.tape):
                    raise exc.PointerIndexError(self)
                else:
                    self.pointer += 1
            elif c == "<":
                if self.pointer == 0:
                    raise exc.PointerIndexError(self)
                else:
                    self.pointer -= 1
            elif c == "^":
                self.tape[self.pointer] += 1
            elif c == "v":
                self.tape[self.pointer] -= 1
            elif c == ".":
                command_out = chr(self.tape[self.pointer])
            elif c == ":":
                command_out = str(self.tape[self.pointer])
            elif c == "-":
                time_to_add = self.tape[self.pointer]

            formatted_tape = ""
            longest_number_length = 0
            for num in self.tape:
                if len(str(num)) > longest_number_length:
                    longest_number_length = len(str(num))
            for num in self.tape:
                formatted_tape += str(num) + " " * \
                    (2+longest_number_length-len(str(num)))

            print(f'POINTER: {self.pointer} {"(Paused)"*(time_to_add != 0)}')
            print(formatted_tape[:width])
            print((" "*((2+longest_number_length)*self.pointer) + "^")[:width])
            print((raw_script[self.position:]+" ")[:width])
            print(res[:width])

            time.sleep(self.speed+time_to_add)
            time_to_add = 0
            print("\033[K\033[A\033[K"*5, end="\r")
            res += command_out
        print("\033[4B", "\033[K\033[A\033[K"*4, f'\r{res}')

    def out_tape(self):
        return self.tape
