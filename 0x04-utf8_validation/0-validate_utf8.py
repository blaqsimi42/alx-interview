#!/usr/bin/python3
""" UTF-8 validation module.

"""


def validUTF8(data):
    """ Checks if a list of integers are valid UTF-8 codepoints.
    Args:
    data (list): data to be valdated
    Return:
    boolean: True if valid, false if invalid
    
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0x06:
                num_bytes = 1
            elif (byte >> 4) == 0x0E:
                num_bytes = 2
            elif (byte >> 3) == 0x1E:
                num_bytes = 3
            elif (byte >> 7) != 0x00:
                return False
        else:
            if (byte >> 6) != 0x02:
                return False
            num_bytes -= 1

    return num_bytes == 0
