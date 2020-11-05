
from ps1_partition import get_partitions
import time
import operator
import collections

def load_cows(filename):
    cow_dict = dict()
    f = open(filename, 'r')
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit):
    itemsCopy = sorted(cows.items(), key=operator.itemgetter(1), reverse = True)
    itemsCopy = collections.OrderedDict(itemsCopy)
    result = []
    while len(itemsCopy) > 0:
        weight = 0
        allcows = []
        for key, value in itemsCopy.items():
            if (weight + value) <= limit:
                allcows.append(key)
                weight += value
        for cow in allcows:
            if cow in itemsCopy:
                del itemsCopy[cow]
        result.append(allcows)
    return result


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    result = []
    for partition in get_partitions(cows.keys()):
        c = 1
        for item in partition:
            weight = 0
            for cow in item:
                weight += cows[cow]
                if weight > limit:
                    c = 0
                    break
            if c == 0:
                break
        if c == 1:
            result.append(partition)
    c = result[0]
    for i in range(len(result)-1):
        if len(c) > len(result[i+1]):
            c = result[i+1]
    
    return c
        
# Problem 3
def compare_cow_transport_algorithms():
    cows = load_cows("ps1_cow_data.txt")
    limit=10

    print(cows)
    print()

    start = time.time()
    greedy = greedy_cow_transport(cows, limit)
    end = time.time()
    print(end - start)
    print(greedy)
    print(len(greedy))
    print()

    start = time.time()
    bruteForce = brute_force_cow_transport(cows, limit)
    end = time.time()
    print(end - start)
    print(bruteForce)
    print(len(bruteForce))


compare_cow_transport_algorithms()