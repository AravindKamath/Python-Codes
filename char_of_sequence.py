sentence=input("string ")
sentence=sentence.lower()
char_count={}
print("total numbers of characters in sentence ",len(sentence))
for char in sentence:
    if char.isalnum():
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
print(char_count)