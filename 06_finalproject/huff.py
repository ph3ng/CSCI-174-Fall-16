from __future__ import (absolute_import, division, print_function,)
#                        unibits_literals)
# Pheng Vang
# 105181778
# CSCI 174 - Final Project
import collections
import heapq
import sys

def huffmanTree(node, result, bits=''):
    # Descend the tree recursively creating the bits
    if len(node[2]) > 1:
        huffmanTree(node[3][0], result, bits + '0')
        huffmanTree(node[3][1], result, bits + '1')
    else:
        # Once at the root, return all calculated bits
        result[node[2]] = bits


if __name__ == '__main__':
    # Taking input from file
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        ls = line.rstrip('\n')
        # Creating string input from file after each newline symbol
        freq = collections.Counter(ls)
        heep = [(freq[s], -1, s, (None, None)) for s in freq]
        heapq.heapify(heep)

        while(len(heep) > 1):
            l, r = heapq.heappop(heep), heapq.heappop(heep)
            heapq.heappush(heep, (l[0] + r[0], l[1] + r[1], l[2] + r[2], (l, r)))
        # Putting frequency of each letter in a dictionary
        letter = dict()
        huffmanTree(heep.pop(), letter)
        # Printing out result with a sorted dictionary
        result = ' '.join(('%s: %s;' % (k, letter[k]) for k in sorted(letter)))
        print(result)

    test_cases.close()
