word = input()
word_list = []

for i in range(len(word)):
    word_list.append(word[i:])
    
word_list.sort()
for w in word_list:
    print(w)