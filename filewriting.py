from sys import argv
from os.path import exists

script, from_file, to_file = argv
user_input = open(from_file)
indata = user_input.read()

if not exists(to_file):
	output = open(to_file, 'w')
	output.write(indata)
	output.close()
user_input.close()

