string=input("enter string ")
print("characters in string ",len(string))
print("uppercase string ",string.upper())
contain="python" in string
print("contains python ",contain)
split=string.split()
print("split-string ",split)
print("hyphenated-string ","-".join(split))
rev=string[::-1]
print("reverse string ",rev)


