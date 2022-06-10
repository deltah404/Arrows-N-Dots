class PointerIndexError(Exception):
    def __init__(self, i):
        self.i = i

    def __str__(self):
        return f'[AND] at {self.i.line}:{self.i.col} - Attempted to move pointer out of range of tape: 0-{len(self.i.tape)}'
