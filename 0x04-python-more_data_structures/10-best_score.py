#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        bs = 0
        for k in a_dictionary:
            if a_dictionary[k] > bs:
                bs = a_dictionary[k]
        for key in a_dictionary:
            if a_dictionary[key] == bs:
                return key
