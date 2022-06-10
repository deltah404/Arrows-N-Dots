from curses import raw
from turtle import position
import numpy as np
import exceptions as exc
import time
import json
import os
import sys


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
        for c in script:
            if c in self.commands:
                raw_script += c
        for c in script:
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
                time.sleep(self.tape[self.pointer])
                continue
            
            print(f'POINTER: {self.tape[self.pointer]}')
            print(raw_script[self.position:]+" ")
            #print("\n ")
            print(res)

            time.sleep(self.speed)
            print("\033[K\033[A\033[K"*3, end="\r")
            res += command_out
        print("\033[4B", "\033[K\033[A\033[K"*4, f'\r{res}')
                

    def out_tape(self):
        return self.tape
