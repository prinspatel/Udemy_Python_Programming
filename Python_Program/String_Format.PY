print("Hellor, Welcome to Python Programming")

s = 'SIngle Cot use to print'
print(s)

#string length
print(len(s))

#check something present in string
# "cot" present in string ( True or F )
print("Cot" in s)

#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

#Print only if "free" is present:
txtt = "The best things in life are free!"
if "free" in txtt:
  print("Yes, 'free' is present.")

#Check if "expensive" is NOT present in the following text:
txxt = "The best things in life are free!"
print("expensive" not in txxt)


#print only if "expensive" is NOT present:
pri = "The best things in life are free!"
if "expensive" not in pri:
  print("No, 'expensive' is NOT present.")

#use {} to format string.
a = 1
b = "if you want to add object value in string use {}".format(a)
print(b)
