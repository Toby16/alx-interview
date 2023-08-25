#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    A method that determines
    if a given data set represents a valid UTF-8 encoding

    Args:
        data -> given set of data
    """
    index = 0

    # Iterate through the list of integers representing the data
    while index < len(data):
        current_byte = data[index]

        # Check if the current_byte is a valid start byte
        if (current_byte >> 7) == 0b0:
            num_bytes = 1
        elif (current_byte >> 5) == 0b110:
            num_bytes = 2
        elif (current_byte >> 4) == 0b1110:
            num_bytes = 3
        elif (current_byte >> 3) == 0b11110:
            num_bytes = 4
        else:
            return False  # Invalid start byte

        # Check if there are enough bytes for the current character
        if (index + num_bytes) > len(data):
            return False

        # Check that subsequent bytes are valid continuation bytes
        for i in range(1, num_bytes):
            if (data[index + i] >> 6) != 0b10:
                return False  # Invalid Continuation byte

        # Move the index to the next character
        index += num_bytes

    return True  # All characters are valid


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110,
            32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
