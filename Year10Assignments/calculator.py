#Version 10
#Square Root, Area and perimeter or shapes, more functions
def space(): #In this part of code I'm defining functions to be used later on. The functions I'm using are pieces of code that I often use, and instead of typing them each time, I can just call them.
  return(' \n---------------------------------------------------------\n ') #This function is one I use to print spacing between prtds of the interface, this can be used to direct the user's eyes and sort information
def area(answer, z):
  return(answer * z) #This function mulltiplies the two numbers in the bracket together. It is also used in area calculators
def pi(answer):
  return(answer * math.pi) #This function multiplies the numbaer in the brackets by pi, and is used in calculation involving circles and ellipses
Menu = 'n' #Here I am defining variables before the loop starts. I am doing this as they will be needed in the loop before they can be assigned, and I don't want them resetting every time the loop repeats
Choice = 0
exit = 'n'
import time #Parts of the python library are being imported to be used in the code. Time is being used to delay parts of my code.
import math #While, math is imported so that I can peform calculation utilising pi
MSG = ['Welcome to the CALCULATOR, (that\'s me)', 'I can peform calculations using many different types of operators.', #Here I create a list with pieces of writing/instructions that I use a lot. During the program I extract certain items of the code that I can display when I want.
'I can also find the area and perimeter of certain shapes',
'However for me to underdstand your human brains, please follow the prompts I give you', 'Please read the prompts and give me your answers!',
'If the answer is Yes or No, please type in y or n',
'Note: Not all prompts can be answered by using y or n, so please read the prompt before answering!',
'I do not understand the notion of \'BEDMAS\', so I will be peforming calculations from left to right', 'Now, time to get started!',
'The operators that can be entered are:', '+ (addition)', '- (subtraction)', 'x (multiplication)', '/ (division)',
'// (division without decimals, rounded down)', '% (the remainder left after division)', '** (Indices, to the power of)', 'r (Root, to the root of)',
'The shapes that can be entered are:', 'r (Rectangle)', 't (Triangle)', 'p (Parallelogram)', 'e (Ellipse(only area))', 'c (Circle)',
'cu (Custom(only perimeter))']
for i in range(0, 2): #This print loading twice and has a second delay after each print
  print("Loading....")
  time.sleep(1)
print('Staring primary systems......')
time.sleep(1.5)
print('Starting secondary systems..')
time.sleep(0.5)
print(' ')
print('All systems online')
while exit != 'y': #WHile this variable does not equal y the code in this loop will repeat
  wc = 0 #Here I am assigning variables inside the loop as I want them to reset every time the loop resets
  counter = 0
  counter2 = 0
  counter3 = 0
  bracket = 0
  R = 2
  AP = 'n'
  S = 'n'
  D = 'y'
  Intro = input('Do you want to view the starting instructions? ')
  if Intro == 'y': #this part of code prints the starting instructions each time the loop repeats.
    print(space())
    while wc < 9: #This loop will repeat while the variable wc is less than
      print('*', MSG[wc]) #In this line the code is printing an sterix, as it is similar to a dot point, along with a certain passage of text. The 1st position in a list is 0, with the 2nd being 1, etc. So if there was a list that had [x, y], x would be in the position labelled zero while y would be in the position labelled one. This piect of code MSG[wc] takes out whatever in the list MSG that has a position that is equivalen to mc. This will result in the printing of *(whatever the message is)
      wc += 1 #Here the variable wc is increased by 1 so that we can then take the next number of the list. It is also done so that the loop will break once wc is greater than 8
      time.sleep(1) #Here there is a 2 second time delay so that the user can read the information being printed, which is how the calculator is used
    print(space())
    Intro = 'n' #It then resets the variable so the Intro will not play automatically in the next repeat of the ,loop
  Menu = input('Do you want to peform calculations using shapes? ')
  if Menu == 'y':
    wc = 18 #Here if the user wants to use shapes the code splits into two parts.
    Menu = input('Do you want to view the shapes? ')
    if Menu == 'y': #Here if the user wants to view the shapes, it makes wc equal to 18 and increases to 25. This is because in the list MSG, the instructions regarding shapes are items 18 to 24.
      print(space()) #Here I call the function space to print a gap to break up the sections of the code
      while wc < 25:
        print('^', MSG[wc])
        wc += 1
        time.sleep(0.5)
      print(' ')
      Menu = 'n'
    print(space())
    S = input('What shape do you want to use? ')
    if S != 'cu':
      if S != 'e':
        AP = input('Do you want to calculate the area? ') #In this part of code, the user is aked if they want to calculate the area only if they don't pick an ellipse or a custom shape. This is because the code can only calculate an eliipse's area or a custome shape's perimeter.
    if S == 'e':
      AP = 'y' #Here the variable that decides if area is being calculated is automatically set to yes if the user chooses to use an ellipse
    if S == 'c':
      R = 1 #The variable R determines how many numbers are being taken to peform a calculation. WHile calculating the area of perimeter of a circel the only part of the formula that changes is the radius
      y = 0 #Here y is set to zero as the list that stores the numbers needs x and y, the first two numbers to have a value. Since a circle only needs one number, y does not need to be utilised.
      D = input('Are you using the radius? ') #Here this question is asked because if the user is not using the radius but the diameter, the code will later divide it by 2 to end up with the radius
    if AP == 'n':
      if S == 'r' or S == 'p': #Here the if statement is true if S is equal to r or p. THis happens because the code needs to do the same thing for both of them
        R = 2 #In this part of the code I am setting how many numbers will be requested for each shape. Eg: A rectangle has 2 pairs of sides while a triangle has 3 sides
      elif S == 't':
        R = 3
      elif S == 'cu':
        R = int(input('How many numbers do you want to use? ')) #The amount of numbers the user wants to use is only asked for a custom shape, as we don't know the number of sides it has
    if Choice != 1: #The code enables you to save numbers after completing calculations. If Choice is equal to 1, then that means someone already saved a number as x
      x = int(input('What is your first number? '))
    if Choice != 2:
      if S != 'c': #Here the user won't be asked for a second number if they are peforming calculation using circles, as for circles you only need one number
        y = int(input('What is your second number? '))
    if D == 'n': #here the diameter is converted to radius
      x /= 2
    MATH = [x, y] #The list MATH, which is going to store the numbers, is created with the 1st and 2nd numbers. It will also be reset to two numbers every time the loop repeats
    while R > 2: #This loop repeats until R is less than 2, as R is the amount of numbers being used, and two numbers have also been taken before
      R -= 1
      NewM = int(input('What is the next number? ')) #Here the user is asked for the next number each time the loop repeats, and it is then added to the list storing the numbers
      MATH.append(NewM)
    answer = MATH[counter] #Here the variable answer is assigned to the 1st item in the list MATH, as counter is equal to 0
    if S == 'c': #Here the number 0 is removed from the loop MATH if the user is using a circle. This is because 0 was assigned to y and added to the list beforehand, but we only want one number in the list
      MATH.remove(0)
    for i in MATH: #This loop will repeat for every item in the loop MATH
      z = MATH[counter] #z = whatever item is in position counter in MATH
      if counter != 0: #This will only happen if counter does not equal zero. This is because it peforms an operation between the variables answer and z. Since z is the same as answer while counter equals zero. We don't want to peform calculations between them when they're the same number
        if AP == 'y': #This splits up the calculations between area and perimeter formilas
          if S == 'r' or S == 'p' or S == 'e': #This piece of code will happen if the shape being used, 'S', is a rectangle, parallelogram or ellipse
            answer = area(answer, z) #Here the variable answer is set to the return of the function 'area'l. The two variables in the bracket will be the numbers used in the function
          elif S == 't':
            answer = area(answer, z)/2
        else:
          if S == 'r' or S == 'p':
            answer *= 2
            answer += 2*z #This happens because recatngles and paralleograms have two sets of equivalent sides. So to find the perimeter, two of the different sides are added together and they are mulitplied by 2, as P =2(l+w)
          elif S == 't' or S == 'cu':
            answer += z  #For triangles and custom shapes, the sides are just added together
      counter += 1 #The counter is incremented by 1, so that the next item of the list can be extracted.
    if AP == 'y':
      if S == 'e': #Ellispes have a formula of pi*a*b. a*b has already been done in the previos part of the code
        answer = pi(answer) #To complete the formula. The variable answer, which is the result of a*b, is assigned to the value of the function pi, with answer being used as the variable in it. The function pi multiplies the answer by pi
      elif S == 'c':
        answer = answer * pi(answer) #Since a circle being used causes only one number to be placed in the list MATH. No calculations were peformed while the other options would have been calculated. This is because the loop would only repeat once, and as counter starts off as one and increments by 1 with each loop, no calculation would be peformed as counter would equal
    else:
      if S == 'c': #This part of the code occurs if a circle's perimeter wants to be calculated, as you only need one number to calculate the perimeter
        answer = 2 * pi(answer)
    print(space())
    print('The calculation you peformed, along with the answer is:')  #Here the calculation and answer will be printed
    if AP == 'n':
      if S == 'r' or S == 'p': #While calculating the perimeter of rectangles and parallelograms, only 2 numbers were needed. Then calculator shows the calculation peformed as adding 4 sides together instead of the forrmula 2(l + w), as it is easier for the average person to understand
        counter += 2
        while counter2 != 2: #Here each number in the list MATH is added to the list again
          MATH.append(MATH[counter2])
          counter2 += 1
        counter2 = 0
      if S == 'c': #Here the entire calculation for a circle's perimeter isn't printed out, as it doesn't work with the actual method of displaying the calculations
        if D == 'y':
          print('2 * π *', MATH[counter2], end ='')
        else:
          print('2 * π * (', MATH[counter2]*2, '/2)', end ='')
    else: #These are extra bits that are needed to be added if area was calculated
      if S == 't':
        print('(', end ='')
      if S == 'e':
        print ('π *', end ='')
      if S == 'c':
        print ('π *', MATH[counter2], '** 2', end ='')
    while counter != 1: #during the loop where the calculations were peformed, counter increased to one less than the total numbers used
      if AP == 'y' : #If are was calculated, multiplication was shown, while addition was shown for perimeter
        print(MATH[counter2],  '* ', end ='') #Here the number in the position of what counter 2 is equal to in the list MATH is printed, the next part of the code "end =''", ensures that the the next item printed will be on the same line. This needs to happen as I'm only printing part of the calculation
      else:
        print(MATH[counter2], '+ ', end ='')
      counter -= 1 #Here counter increments negatively by 1 so that the loop can be broken
      counter2 += 1 #This is so the next item can be taken from the list
    if S != 'c':
      print(MATH[counter2], end ='') #For calculations using circles, the calculation has already been printed, for the rest of them, the last number has to be printed
    if AP == 'y':
      if S == 't':
        print(') / 2') #The calculation using triangles has brackets at the start and they need to be completed
    print(' = ', answer) #Finally the answer is printed
    print(space())
  else: #This part of the code is used when the user doesn't want to calculate with shapes.
    print(space())
    Menu = input('Do you want to view the operators? ')
    if Menu == 'y':
      wc = 9
      print(' ')
      while wc < 18: #This prints the operators with delay
        print('^', MSG[wc])
        wc += 1
        time.sleep(0.5)
      print(' ')
      Menu = 'n'
      print(space())
    R = int(input('How many numbers do you want to use? ')) #This part of the code asks how many numbers you want to use. It asks your first number, and then for every other numebr, it ask for an operator befoe it. The operator is what will happen to the two numbers on either side of it
    if Choice != 1:
      x = int(input('What is your first number? '))
    a = input('What is your first operator? ')
    if Choice != 2:
      y = int(input('What is your second number? '))
    MATH = [x, y] #Her list are made for the numbers and the operators
    OP = [a]
    while R > 2:
      R -= 1
      NewO = input('What is the next operator? ')
      OP.append(NewO)
      NewM = int(input('What is the next number? '))
      MATH.append(NewM)
    OP.append(' ')
    answer = MATH[counter]
    for i in MATH:
      z = MATH[counter] #This does the same as the shape calculations, except with a more diverse set of operators
      if counter != 0:
        if b == '+':
          answer += z
        elif b == '-':
          answer -= z
        elif b == 'x' or b == '*': #Since the function area peforms multiplication I use it here. 'x' and '*' both mean multiplication, with x being the failsafe for people not reading the instructions and instead assuming it
          answer = area(answer, z)
        elif b == '/':
          answer /= z
        elif b == '//':
          answer //= z
        elif b == '%':
          answer %= z
        elif b == '**':
          answer **= z
        elif b == 'r':
          answer **= (1/z)
      b = OP[counter]
      counter += 1
    print(space())
    print('The calculation you peformed, along with the answer is:')
    while counter3 < counter:
      if OP[counter3] == 'r': #With roots, the operator needs to be printed first for the loop later, as the first nuumber has alredy been taken
        print(MATH[counter2], end ='')
        MATH.append(' ')
        bracket = 1
        counter2 += 1
        while counter3 < counter: #This part of the code prints the calculation that happened if a root occured. NOTE: ONLY 1 ROOT CAN BE USED
          if bracket == 1: #This continues from the root. It finish the root calculation display
            print(' ** (1 /', MATH[counter2], ')', end ='')
            MATH.append(' ')
            counter2 += 1
            counter3 += 1
            bracket = 0
          if OP[counter3] == 'r': #Here, if a root wasn't the first number, it prints the next number is
            print('(', MATH[counter2], end ='')
            bracket = 1
          print(' ', OP[counter3], MATH[counter2], ' ', end ='') #If there is no root being used this time, it prints the code in continuation from the original root being used
          counter2 += 1
          counter3 += 1
      else:
        print( ' ', MATH[counter2], OP[counter3], end ='') #This happens if there is no root and prints the calculation in a normal order
      counter2 += 1
      counter3 += 1
    print('= ', answer)
    print(space())
  save = input('Do you want to continue using this number? ') #This code saves the number. It is indented so that it occurs for those who calculate with shapes or operators
  if save == 'y':
    Choice = int(input('Enter 1 to save it as the first number, 2 to save it as the second number: ')) #CHoice is set so that the number for x or y won't be asked wheen the code repeats
    if Choice == 1: #If the user wants to save the number as the 1st 1, it saves it as x, otherwsie y for the second.
      x = answer
    else:
      y = answer
  else:
    Choice = 0
    exit = input('Do you want to exit the program? ') #If the codes doesn't want to be repeated the whole loop breaks and exits, otherwise it repeats
print(space())
print('Thank you for using the CALCULATOR today!')
print('I hope you found me useful')
print(' ')
print(' ')
print('Shutting off secondary systems..')
time.sleep(0.5)
print('Shutting off primary systems......')
time.sleep(1.5)
for i in range(0, 2):
      print("Depowering....")
      time.sleep(1)
print(' ')
print('All systems offline')