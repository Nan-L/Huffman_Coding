# CMPT 145: Assignment 8 Question 3
#

import sys as sys

DEFAULT_OUTPUT_FILE = '<console>'

def main():
    """
    Purpose
        The main program.
        Usage: python3 Decoder.py <filename>
        Sends output to DEFAULT_OUTPUT_FILE
    Return:
        :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3', sys.argv[0], '<filename>')
        print('-- sends output to', DEFAULT_OUTPUT_FILE, '-- ')
        return

    s = read_file(sys.argv[1])
    sizes = s[0].split()
    code_size = int(sizes[0])
    message_size = int(sizes[1])
    codes = s[1:code_size + 1]
    encoded = s[code_size + 1:code_size + message_size + 1]

    dc = build_decoder(codes)
    for enc in encoded:
        message = decode_message(enc, dc)
        print(message)


def build_decoder(code_lines):
    """
    Purpose:
        Build the dictionary for decoding from the given list of code-lines
    Preconditions:
        :param code_lines: A list of strings of the form "CODE:'<char>'"
    Return:
        :return: a dictionary whose keys are 'CODE' and values are <char>
    """
    codec = {}
    for code_str in code_lines:
        cchr = code_str.split(':')
        code = cchr[0]
        char = cchr[1]
        codec[code] = char[1]   # The input file has ' ' around the character
    return codec


def decode_message(coded_message, codec):
    """
    Purpose:
        Decode the message using the decoder.
    Preconditions:
        :param coded_message: An encoded string consisting of digits '0' and '1'
        :param codec: a Dictionary of coded_message-character pairs
    Return:
        :return: A string decoded from coded_message
    """
    decoded_chars = []
    first = 0
    last = first + 1
    while first < len(coded_message):
        partial_code = coded_message[first:last]
        if partial_code in codec:
            decoded_chars.append(codec[partial_code])
            first = last
            last = first + 1
        else:
            last += 1
    return ''.join(decoded_chars)


def read_file(fname):
    """
    Purpose:
        Read the file with the given name.
    Preconditions:
        :param fname: a file name
    Return:
        :return: a list of strings consisting of the contents of the file
    """
    f = open(fname)
    lines = [l.rstrip() for l in f if l]
    f.close()
    return lines


if __name__ == '__main__':
    main()


