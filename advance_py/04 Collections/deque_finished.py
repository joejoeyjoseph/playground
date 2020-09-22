# deque objects are like double-ended queues
# memory efficient to manipulate on the "ends" (beginning & end) of a list

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    for elem in d:
        #print(d)
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print('hi')
    print(d)

    # rotate the deque
    print(d)
    d.rotate(1)
    print(d)


if __name__ == "__main__":
    main()
