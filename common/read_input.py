import os

def read_input_text(input_location):
    with open(os.path.abspath(input_location)) as file:
        input_list = [line.rstrip() for line in file]
    return input_list