_INIT_ASSERT_MESSAGE_NONLEAF  = 'Invalid Huffman tree construction attempted.'
_GETCH_ASSERT_MESSAGE_NONLEAF = 'Method get_char() called on non-leaf node'

class HuffmanTree(object):

    def __init__(self, freq=0, char=None, left=None, right=None):
        """
        Purpose:
            Initializes the HuffmanTree object.
            To create a leaf node, children are None
                aleaf = HuffmanTree(freq=10, char='A')
                bleaf = HuffmanTree(freq=15, char='E')
            To create an internal node, children are given
                node = HuffmanTree(left=aleaf, right=bleaf)

        Pre-conditions:
            :param freq: a positive integer
            :param char: a character
            :param left: another Huffman Tree
            :param right: another HuffmanTree
        """
        self.__char = char
        self.left = left
        self.right = right

        if left is None and right is None:
            # leaf node: assign the frequency as given
            self.__freq = freq
        else:
            assert left is not None and right is not None, _INIT_ASSERT_MESSAGE_NONLEAF
            # non-leaf node: calculate the frequency from the given subtrees
            self.__freq = left.__freq + right.__freq

    def get_freq(self):
        """
        Purpose:
            Return the frequency data stored in the node.
        Return:
            :return: the frequency
        """
        return self.__freq

    def get_char(self):
        """
        Purpose:
            Return the character stored at a leaf node.
        Return:
            :return: the character at a leaf node
        """
        assert (self.left is None and self.right is None), _GETCH_ASSERT_MESSAGE_NONLEAF
        return self.__char

    def display(self, level=0):
        """
        Purpose:
            For debugging, display the tree.
            The structure of the tree is represented by indentation
            No other real purpose.
        Preconditions:
            :param level: indentation amount for subtrees.
        Return
            :return: None
        """
        if self.left is None and self.right is None:
            print(' '*level+'Leaf:', self.__char, self.__freq)
        else:
            print(' '*level+'Node:', self.__freq, 'Children:')
            self.left.display(level+1)
            self.right.display(level+1)

    def build_codec(self):
        """
        Purpose:
            Build a dictionary of char-code pairs from the Huffman tree.
        Return:
            :return: a dictionary with character as key, code as value
        """
        def build_codec_helper(HT, codes, code):
            """
            a helper method
            :param HT: a HuffmanTree
            :param codes: a dictionary of char-code pairs
            :param code: the code for a char
            :return: None
            """
            if HT.left is None and HT.right is None:
                codes[HT.get_char()] = code
            else:
                code += "0"
                build_codec_helper(HT.left, codes, code)
                code = code[:-1]
                code += "1"
                build_codec_helper(HT.right, codes, code)

        a_codes = {}
        a_code = ""
        if self.left is None and self.right is None:
            a_codes[self.get_char()] = "0"
        else:
            build_codec_helper(self, a_codes, a_code)
        return a_codes


if __name__ == '__main__':
    # build the tree
    # start with a colection of trees from a frequency list

    freqs = [(10,'A'), (3, 'C'), (4, 'D'), (15, 'E'), (2, 'G'), (6, 'I')]
    leafs = [HuffmanTree(freq=f,char=c) for f,c in freqs]

    # display to ensure correctness
    for l in leafs:
        l.display()

    # note that this example is not searching for trees to combine
    # the code was written knowing which trees to combine

    node = HuffmanTree(left=leafs[4], right=leafs[1])
    node.display()

    node = HuffmanTree(left=leafs[2], right=node)
    node.display()

    node = HuffmanTree(left=node, right=leafs[5])
    node.display()

    node2 = HuffmanTree(left=leafs[0], right=leafs[3])
    node2.display()

    node = HuffmanTree(left=node2, right=node)
    node.display()

    codec = node.build_codec()
    for k in codec:
        print(k +':' + codec[k])


