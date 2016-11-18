# _*_ coding: utf_8 _*_
"""
Created on 7/29/2016

@author: Eddie
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import math
import random

from pysh.gp import gp
from pysh import pysh_interpreter
from pysh import instruction
from pysh.instructions import boolean, code, common, numbers, string
from pysh.instructions import registered_instructions as ri

'''
This problem evolves a program to determine if a number is odd or not.
'''

def target_function(x):
	return x**3 - (2*(x**2)) - x

def error_func(program):
	errors = []

	for x in range(20):
		# Create the push interpreter
		interpreter = pysh_interpreter.Pysh_Interpreter()
		interpreter.reset_pysh_state()
		
		# Push input number		
		interpreter.state.stacks["_integer"].push_item(x)
		interpreter.state.stacks["_input"].push_item(x)
		# Run program
		interpreter.run_push(program)
		# Get output
		top_int = interpreter.state.stacks["_integer"].stack_ref(0)

		if type(top_int) == int:
			# compare to target output
			target_int = target_function(x)
			# calculate error
			errors.append(abs(top_int - target_int))
		else:
			errors.append(1000)

	return errors

problem_params = {
	"atom_generators" : {"integer_div" : ri.get_instruction_by_name("integer_div"),
						 "integer_mult" : ri.get_instruction_by_name("integer_mult"),
						 "integer_add" : ri.get_instruction_by_name("integer_add"),
						 "integer_sub" : ri.get_instruction_by_name("integer_sub"),
                         "f1" : lambda: random.randint(0, 10),
                         "Input" : instruction.Pysh_Input_Instruction(0)},
    "epigenetic_markers" : [],
    "selection_method" : "epsilon_lexicase",
    "genetic_operator_probabilities" : {"alternation" : 0.5,
										"uniform_mutation" : 0.5},
	"alternation_rate" : 0.1,
	"uniform_mutation_rate" : 0.1
}


if __name__ == "__main__":
	gp.evolution(error_func, problem_params)
