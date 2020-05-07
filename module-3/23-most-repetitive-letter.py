# task: printout most repetitive letter in sencence
from pprint import pprint

sentence = "this is a common interview question"

alphabet_occurance = {}

for letter in sentence:
    if letter in alphabet_occurance:
        alphabet_occurance[letter] += 1;
    else:
        alphabet_occurance[letter] = 1
        
alphabet_occurance_sorted = sorted(
    alphabet_occurance.items(), 
    key=lambda kv:kv[1], 
    reverse = True)
    
print(alphabet_occurance_sorted[0])