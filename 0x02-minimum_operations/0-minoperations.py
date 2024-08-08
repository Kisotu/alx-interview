#!/usr/bin/python3
"""write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file
"""


def minOperations(n):
    """finds the fewest number of operations needed to result
    in exactly n H characters.
    """
    if not isinstance(n, int):
        return 0
    operations_count = 0
    buffer_Mem = 0
    done = 1
    while done < n:
        if buffer_Mem == 0:
            buffer_Mem = done
            done += buffer_Mem
            operations_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            buffer_Mem = done
            done += buffer_Mem
            operations_count += 2
        elif buffer_Mem > 0:
            done += buffer_Mem
            operations_count += 1
    # print('')
    return operations_count
