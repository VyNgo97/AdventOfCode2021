import logging

def read_input():
    with open("input.txt") as file:
        input_list = [int(line) for line in file]
    return input_list

def find_count_p1(data):
    count = 0 
    curr = data[0]
    for x in range(1, len(data)):
        if(data[x] > curr):
            count += 1
        curr = data[x]
    logging.info('P1 count is %s', count)
    return count

def find_count_p2(data):
    first = 0
    second = 3
    count = 0
    curr = sum(data[first:second])

    while(second <= len(data)):
        if(sum(data[first:second]) > curr):
            count+=1
        curr = sum(data[first:second])
        first+=1
        second+=1

    logging.info('P2 count is %s', count)
    return count

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    find_count_p1(read_input())
    find_count_p2(read_input())
