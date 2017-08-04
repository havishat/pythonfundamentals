# input
list1 = []
word_list = ['hello','world','my','name','is','Anna']
char = set('o')
for word in word_list:
    if char & set(word):
        list1.append(word)
print list1


