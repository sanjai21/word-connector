#importing the required modules
#these two for dictionary
import json
#this one for wordlist
import itertools
#creating the wordlist using the given words
data = json.load(open("dictionary.json"))
def main():
    letters = input("Enter the words without spaces in small letters : \t")
    exist = []
    dictionary = []
    final = []
    final2 = []
    minn =  int(input("Enter the minimum lenght of words:\t"))
    maxx = int(input("Enter the maximum lenght of words:\t"))
    while maxx>=minn:
        for x in itertools.product(letters,repeat=minn):
           xx = ''.join(x)
           exist.append(xx)
        minn+=1
    for y in data:
        dictionary.append(y)
    for z in exist:
        if z in dictionary:
            final.append(z)
            for i in final:
                if i not in final2:
                    final2.append(i)
    for m in final2:
        print(m)
        k = list(letters)
        for l in k:
            u = m.count(l)
            while u > 2:
                print(m)
    





main()

       
