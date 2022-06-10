from arrows_n_dots import Interpreter

i = Interpreter()
script = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" # causes a PointerIndexError - attempts to move pointer position outside of tape range
i.evaluate(script)