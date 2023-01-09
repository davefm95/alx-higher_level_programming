#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        s_tuple = (0, None)
    else:
        ch_1st = sentence[0]
        s_tuple = (len(sentence), ch_1st)
    return s_tuple
