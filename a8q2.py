# CMPT 145: Assignment 8 Question 2

# nan liu
# nal150
# 11214578
# CMPT145 02
# CMPT145 L08

#import sys as sys
import Huffman as HT
import HuffmanHeap as HP

DEFAULT_OUTPUT_FILE = 'encoded.txt'

def main():
    """
    Purpose:
        Application to read and encode a file using Huffman codes.
        Usage: python3 Encoder.py <filename>
        Sends output to DEFAULT_OUTPUT_FILE
    Return:
        :return: None
    """
    #if len(sys.argv) != 2:
    #    print('Usage: python3', sys.argv[0], '<filename>')
    #    print('-- sends output to', DEFAULT_OUTPUT_FILE, '-- ')
     #   return

    #fname = sys.argv[1]
    fname = "counting-example.txt"
    lines = read_file(fname)
    freqs = count_characters(lines)
    codec = build_codec(freqs)
    coded = encode(lines, codec)
    write_file(DEFAULT_OUTPUT_FILE, coded)


def read_file(fname):
    """
    Purpose:
        Read a file and return contents in a list of strings.
    Preconditions:
        :param fname: the name of a text file
    Return:
        :return: a list of strings, one string for each line
    """
    tfile = open(fname)
    lines = [l.rstrip() for l in tfile]
    tfile.close()
    return lines


def write_file(fname, lines):
    """
    Purpose:
        Write the data in lines to the named file.
        Warning: this will over-write any data in the named file!
    Preconditions:
        :param fname: the name of a text file
        :param lines: a list of strings
    Post-condition:
        The named file is created or over-written.
    Return:
        :return: None
    """
    tfile = open(fname, 'w')
    for line in lines:
        tfile.write(line + '\n')
    tfile.close()


def count_characters(contents):
    """
    Purpose:
        Count the characters in the contents.
    Pre-conditions:
        :param contents: a list of strings.
    Return:
        :return: a list of the character-frequency pairs
    """
    freqs = dict()
    for line in contents:
        for char in line:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
    return freqs.items()


def build_codec(freq_list):
    """
    Purpose:
        Build a dictionary containing character:code pairs from the frequency list.
    Pre-conditions:
        :param freq_list: A list of (frequency,character) pairs.
    Return:
        :return: a dictionary
    """
    def get_frequency(a_HuffmanTree):
        """
        helper function for sorting the list according to frequency of the char
        :param a_HuffmanTree:
        :return:
        """
        return a_HuffmanTree.get_freq()

    leafs = [HT.HuffmanTree(freq=f, char=c) for c,f in freq_list]
    leafs.sort(key=get_frequency)
    heap = HP.HuffmanHeap(leafs, [])
    while len(heap.old) != 0:
        temp1 = heap.dequeue()
        temp2 = heap.dequeue()
        item3 = HT.HuffmanTree(temp1.get_freq()+temp2.get_freq(),left=temp1,right=temp2)
        heap.enqueue(item3)
    if len(heap.new) >= 2:
        while True:
            temp1 = heap.dequeue()
            temp2 = heap.dequeue()
            item3 = HT.HuffmanTree(temp1.get_freq() + temp2.get_freq(), left=temp1, right=temp2)
            if len(heap.new) == 0:
                heap.enqueue(item3)
                break
            heap.enqueue(item3)
    return heap.new[0].build_codec()


def encode(strings, codec):
    """
    Purpose:
        Use the codec to create the data to be sent to the output file.
    Pre-conditions:
        :param strings: A list of strings to encode.
        :param codec: A dictionary containing character-code pairs
    Return:
        :return: a list of strings including:
            the number of codes the number of coded lines,
            the codes
            the coded lines
        to be sent to the output
    """
    a = len(codec)
    counter = 0
    for line in strings:
        if line == "":
            counter += 1
    b = len(strings) - counter
    output = [str(a)+" "+str(b)]
    for key in codec:
        output.append(codec[key]+":'"+key+"'")
    for line in strings:
        buffer = ""
        for character in line:
            buffer += codec[character]
        output.append(buffer)
    return output


if __name__ == '__main__':
    main()
