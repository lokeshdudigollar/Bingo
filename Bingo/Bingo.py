import random
from random import randint

#intro

print("+-------------------------------+")
print("|            Options:           |")
print("|         1 - Play game         |")
print("|         2 - Quit game         |")
print("+-------------------------------+")

douwanttoplay = int(input('Please select an option from the above: '))

if douwanttoplay == 1:
#makes computer's grid
  compl = []
  while len(compl) <25:
    x = random.randint(1, 50)
    if x < 10:
      x = '0' + str(x)
    elif x not in compl:
      compl.append(x)


  #makes user's grid
  userl = []
  while len(userl) <25:
    x = random.randint(1, 50)
    if x < 10:
      x = '0' + str(x)
    elif x not in userl:
      userl.append(x)


  #prints user's grid
  #count is n
  n = 0
  print('             ')
  print("This is your grid:")
  for i in range(25):
    print(userl[i], end = ' ')
    n +=1
    if n == 5:
      print("\n")
      n = 0
  print('        ')

  #printing the computer grid 
  n = 0
  print("This is the Computer's grid:")
  for i in range(25):
    print(compl[i], end = ' ')
    n +=1
    if n == 5:
      print("\n")
      n = 0
  print('        ')

  #game starts________________

  #user game

  flag = 0
  while flag != 1 or flag != 2:
    for i in range(25):
      user = random.randint(1,50)
      comp = random.randint(1,50)
    for i in range(25):
      if user == userl[i]:
        userl[i] = 'xx'
      if comp == compl[i]:
        compl[i] = 'xx'


    i=0
    if userl[i] == userl[i+1] == userl[i+2] == userl[i+3] == userl[i+4] == 'xx' or userl[i+5] == userl[i+6] == userl[i+7] == userl[i+8] == userl[i+9] == 'xx' or userl[i+10] == userl[i+11] == userl[i+12] == userl[i+13] == userl[i+14] == 'xx' or userl[i+15] == userl[i+16] == userl[i+17] == userl[i+18] == userl[i+19] == 'xx' or userl[i+20] == userl[i+21] == userl[i+22] == userl[i+23] == userl[i+24] == 'xx':
      flag = 1
      break
    elif compl[i] == compl[i+1] == compl[i+2] == compl[i+3] == compl[i+4] == 'xx' or compl[i+5] == compl[i+6] == compl[i+7] == compl[i+8] == compl[i+9] == 'xx' or compl[i+10] == compl[i+11] == compl[i+12] == compl[i+13] == compl[i+14] == 'xx' or compl[i+15] == compl[i+16] == compl[i+17] == compl[i+18] == compl[i+19] == 'xx' or compl[i+20] == compl[i+21] == compl[i+22] == compl[i+23] == compl[i+24] == 'xx':
      flag = 2
      break

  print("This is your grid updated:")
  for i in range(25):
    print(userl[i], end = ' ')
    n +=1
    if n == 5:
      print("\n")
      n = 0
  print('             ')

  print("This is the updated Computer's grid:")
  for i in range(25):
    print(compl[i], end = ' ')
    n +=1
    if n == 5:
      print("\n")
      n = 0
  print('              ')


  if flag == 1:
    print('Well done! You win!')
  else:
    print('Oh no! The computer won')
elif douwanttoplay == 2:
  print('Bye!')
else:
  print('That is not a valid option. Please try again')
#code starts again!!___________________________
  douwanttoplay = int(input('Please select an option from the above: '))

  if douwanttoplay == 1:
  #makes computer's grid
    compl = []
    while len(compl) <25:
      x = random.randint(1, 50)
      if x < 10:
        x = '0' + str(x)
      elif x not in compl:
        compl.append(x)


    #makes user's grid
    userl = []
    while len(userl) <25:
      x = random.randint(1, 50)
      if x < 10:
        x = '0' + str(x)
      elif x not in userl:
        userl.append(x)


    #prints user's grid
    #count is n
    n = 0
    print('             ')
    print("This is your grid:")
    for i in range(25):
      print(userl[i], end = ' ')
      n +=1
      if n == 5:
        print("\n")
        n = 0
    print('        ')

    #printing the computer grid 
    n = 0
    print("This is the Computer's grid:")
    for i in range(25):
      print(compl[i], end = ' ')
      n +=1
      if n == 5:
        print("\n")
        n = 0
    print('        ')

    #game starts________________

    #user game

    flag = 0
    while flag != 1 or flag != 2:
      for i in range(25):
        user = random.randint(1,50)
        comp = random.randint(1,50)
      for i in range(25):
        if user == userl[i]:
          userl[i] = 'xx'
        if comp == compl[i]:
          compl[i] = 'xx'


      i=0
      if userl[i] == userl[i+1] == userl[i+2] == userl[i+3] == userl[i+4] == 'xx' or userl[i+5] == userl[i+6] == userl[i+7] == userl[i+8] == userl[i+9] == 'xx' or userl[i+10] == userl[i+11] == userl[i+12] == userl[i+13] == userl[i+14] == 'xx' or userl[i+15] == userl[i+16] == userl[i+17] == userl[i+18] == userl[i+19] == 'xx' or userl[i+20] == userl[i+21] == userl[i+22] == userl[i+23] == userl[i+24] == 'xx':
        flag = 1
        break
      elif compl[i] == compl[i+1] == compl[i+2] == compl[i+3] == compl[i+4] == 'xx' or compl[i+5] == compl[i+6] == compl[i+7] == compl[i+8] == compl[i+9] == 'xx' or compl[i+10] == compl[i+11] == compl[i+12] == compl[i+13] == compl[i+14] == 'xx' or compl[i+15] == compl[i+16] == compl[i+17] == compl[i+18] == compl[i+19] == 'xx' or compl[i+20] == compl[i+21] == compl[i+22] == compl[i+23] == compl[i+24] == 'xx':
        flag = 2
        break

    print("This is your grid updated:")
    for i in range(25):
      print(userl[i], end = ' ')
      n +=1
      if n == 5:
        print("\n")
        n = 0
    print('             ')

    print("This is the updated Computer's grid:")
    for i in range(25):
      print(compl[i], end = ' ')
      n +=1
      if n == 5:
        print("\n")
        n = 0
    print('              ')


    if flag == 1:
      print('Well done! You win!')
    else:
      print('Oh no! The computer won')

