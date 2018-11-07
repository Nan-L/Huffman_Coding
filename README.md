# Huffman_Coding
Huffman Coding is one of the lossless data compression techniques. It assigns variable-length codes to the input characters, based on the frequencies of their occurence. The most frequent character is given the smallest length code. 

## Implementation Idea

* Building frequency dictionary

* Select 2 minimum frequency symbols and merge them repeatedly: Used Min Heap

* Build a tree of the above process: Created a HeapNode class and used objects to maintain tree structure

* Assign code to characters: Recursively traversed the tree and assigned the corresponding codes

* Encode the input text. Added padding to the encoded text, if it’s not of a length of multiple of 8. Stored this padding information, in 8 bits, in the beginning of the resultant code.

* Write the result to an output binary file, which will be our compressed file.
