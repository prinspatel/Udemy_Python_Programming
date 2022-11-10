file = open('text_file.txt') #file name
#print(file.read()) #read whole file
#print(file.readline()) #read one single line at a time
'''
#read file using while loop
line = file.readline()
while line !="":
    print(line)
    line = file.readline()
'''

#Using readlines store file data as a list.
for list in file.readlines():
    print(list)

file.close() #close file