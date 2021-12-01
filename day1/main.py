def read_input():
    input_list = []
    with open("input.txt") as file:
        for line in file:
            input_list.append(int(line))

    return input_list

def find_count():
    data = read_input()
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

    print(count)
    return count

find_count()