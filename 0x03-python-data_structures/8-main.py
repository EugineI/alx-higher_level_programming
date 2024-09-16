#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
sentene1 = ""
len1, first1 = multiple_returns(sentene1)
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
print("Length: {:d} - First character: {}".format(len1, first1))
