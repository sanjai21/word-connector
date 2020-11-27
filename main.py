#importing the required modules
import json
#this one for wordlist
import itertools
#storing the words in he dictionary in data
data = json.load(open("dictionary.json"))
#main function
def main():
    ex = input("Enter the letters without spaces in any oder: \t")
    letters = ex.lower()
    possible_combinations = [] #possible combinations of the given letters 
    dictionary_list = [] 
    possible_words = []
    possible_words_without_repeating = []
    min_lenght =  int(input("Enter the minimum lenght of the words:\t"))
    max_lenght = int(input("Enter the maximum lenght of the words:\t"))
    print("\t\n------------------ Wait a few seconds -----------------\n")
    while max_lenght>=min_lenght:
        for x in itertools.product(letters,repeat=min_lenght):
           combinations = ''.join(x)
           possible_combinations.append(combinations)
        min_lenght+=1
    for y in data: #storing the words in the dictionaries as a list for looping purpose 
        dictionary_list.append(y)
        #removing the repeating words
    for z in possible_combinations:
        if z in dictionary_list:
            possible_words.append(z)
            for i in possible_words:
                if i not in possible_words_without_repeating:
                    possible_words_without_repeating.append(i)
    for m in possible_words_without_repeating:

        print(m)

#initiating                
main()

       
