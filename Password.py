
f = open("C:\\Users\\JennEric\\Documents\\Python\\AdventOfCode\\Day 2\\Part 2\\list.txt","r")
numbers = f.readlines()
#print(numbers)

validpasswords = 0

for x in numbers:
  x = x.split()
  rangecount = x[0]
  rangecount1 = ''
  rangecount2 = ''
  before = 'Y'
  #rangecount = rangecount.replace('-',',')
  letter = x[1][0]
  password = x[2]
  count = password.count(letter)
  
  for z in rangecount:
    if z != '-' and before == 'Y':
      rangecount1 += z
    elif z == '-':
      before = 'N'
    elif before == 'N':
      rangecount2 += z

  
  if password[int(rangecount1)-1] != password[int(rangecount2)-1]:
    if password[int(rangecount1)-1] == letter or password[int(rangecount2)-1] == letter:

      print (letter,password[int(rangecount1)-1],password[int(rangecount2)-1])
      validpasswords += 1
      print(validpasswords)




'''
  for y in range(int(rangecount1),int(rangecount2)+1):
    print(y,rangecount)


    
    if y == count and letter in password:
      validpasswords += 1 
      print('This password is valid: ',x,' and ',letter,' shows up ',count,' times')
      print(validpasswords)
'''
