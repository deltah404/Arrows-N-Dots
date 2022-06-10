import numpy as np
import exceptions as exc
import json


class Interpreter:
    def __init__(self):
        self.tape = np.full(32, 0)
        self.pointer = 0
        self.line = 1
        self.col = 1
        with open('./config.json') as fp:
            self.commands = json.load(fp)["operations"]

    def evaluate(self, script: str):
        res = ""
        for c in script:
            self.col += 1
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
                res += chr(self.tape[self.pointer])
            elif c == ":":
                res += str(self.tape[self.pointer])
        print(res)

    def out_tape(self):
        return self.tape
