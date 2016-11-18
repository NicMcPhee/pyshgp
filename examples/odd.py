# _*_ coding: utf_8 _*_
"""
Created on 5/21/2016

@author: Eddie
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import random

import pysh
import pysh.instruction as instr
import pysh.utils as u
import pysh.pysh_interpreter as interp
from pysh.gp import gp
from pysh.instructions import boolean, code, common, numbers, string
from pysh.instructions import registered_instructions 

'''
This problem evolves a program to determine if a number is odd or not.
'''

def odd_error_func(program, debug = False):
	errors = []

	for i in range(10):
		# Create the push interpreter
		interpreter = interp.Pysh_Interpreter()
		interpreter.reset_pysh_state()
		
		# Push input number		
		interpreter.state.stacks["_integer"].push_item(i)
		interpreter.state.stacks["_input"].push_item(i)
		# Run program			
		interpreter.run_push(program, debug)
		# Get output
		prog_output = interpreter.state.stacks["_boolean"].stack_ref(0)
		#compare to target output
		target_output = bool(i % 2)

		if prog_output == target_output:
			errors.append(0)
		else:
			errors.append(1)
	return errors

odd_params = {
	"atom_generators" : u.merge_dicts(registered_instructions.registered_instructions,	# Use all possible instructions,
					                  {"f1" : lambda: random.randint(0, 100),			# and some integers
									   "f2" : lambda: random.random(),					# and some floats
									   "Input" : instr.Pysh_Input_Instruction(0)})	    # and an input instruction that pushes the input to the _integer stack.
}

def test_odd_solution():
	#print(registered_instructions.registered_instructions)
	#prog_lst = ['_integer_eq', 1, '_integer_mod', 2]
	prog_lst = [2, '_integer_mod', 1, '_integer_eq']
	prog = gp.load_program_from_list(prog_lst)
	errors = odd_error_func(prog, debug = True)
	print("Errors:", errors)


if __name__ == "__main__":
	gp.evolution(odd_error_func, odd_params)
	#test_odd_solution()
