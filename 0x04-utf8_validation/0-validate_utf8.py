#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints
    """
    skip_count = 0
    n = len(data)
    for i in range(n):
        if skip_count > 0:
            skip_count -= 1
            continue
        if not isinstance(data[i], int) or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skip_count = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-bytes utf-8 character encoding
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip_count = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-bytes utf-8 character encoding
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip_count = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-bytes utf-8 character encoding
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip_count = span - 1
            else:
                return False
        else:
            return False
    return True
