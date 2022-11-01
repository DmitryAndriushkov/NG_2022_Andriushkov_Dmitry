def encrypt(string, shift):

  cipher = ''
  for abc in string:
    if abc == ' ':
      cipher = cipher + abc
    elif  abc.isupper():
      cipher = cipher + chr((ord(abc) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(abc) + shift - 97) % 26 + 97)

  return cipher

text = input("enter string: ")
s = int(input("enter shift number: "))
print("original string: ", text)
print("after encryption: ", encrypt(text, s))