import logging
import re

def read_input():
    with open("input.txt") as file:
        input_list = [line.rstrip() for line in file]
    return input_list

def p1(data):
    
    position_x = 0
    position_y = 0

    for command in data:
        val = int((movement := re.findall('[0-9]+', command)[0]))
        if "forward" in command:
            position_x += val
        elif "down" in command:
            position_y += val
        elif "up" in command:
            position_y -= val

    logging.info('Horizontal: %s Vertical: %s Multiplied: %s', position_x, position_y, position_x*position_y)
    
    return position_x*position_y


def p2(data):
    
    aim = 0
    position_x = 0
    position_y = 0
    
    for command in data:
        val = int((movement := re.findall('[0-9]+', command)[0]))
        if "forward" in command:
            position_x += val
            position_y += (aim * val)
        elif "down" in command:
            aim += val
        elif "up" in command:
            aim -= val

    logging.info('Horizontal: %s Vertical: %s Multiplied: %s', position_x, position_y, position_x*position_y)
    return position_x*position_y

    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    p1(read_input())
    p2(read_input())

