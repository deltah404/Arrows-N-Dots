from arrows_n_dots import Interpreter

i = Interpreter()

#######################

ex_script_1 = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" #       X causes a PointerIndexError - attempts to move pointer position outside of tape range
i.evaluate(ex_script_1)

#######################

ex_script_2 = "<" #                                                          X causes a PointerIndexError - attempts to move pointer position outside of tape range
i.evaluate(ex_script_2)

#######################

ex_script_3 = "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^." #                    - valid AND code, outputs "&"
i.evaluate(ex_script_3)