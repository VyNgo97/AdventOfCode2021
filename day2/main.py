import logging
import sys
sys.path.append('..')

from re import findall
from common.read_input import read_input_text



def p1(data):
    position_x = 0
    position_y = 0

    for command in data:
        val = int((movement := findall('[0-9]+', command)[0]))
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
        val = int((movement := findall('[0-9]+', command)[0]))
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
    p1(read_input_text("input.txt"))
    p2(read_input_text("input.txt"))

