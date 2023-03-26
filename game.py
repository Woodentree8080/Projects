import time #For delays
import pandas as pd #For the dataset manipulation
import numpy as np #For maths (polynomial)
import regex as rg # For find and replace characters
import matplotlib.pyplot as plt #For graphing
import seaborn as sns #For graphing

#Plan
#3? main functions of code - Call certain parts of database, graph certain parts of databse and discover trends in database(not sure
#Have 3 seperate functions for each of these
#For first part be able to choose what columns and rows you want
#For graph be able to pickx and y-axises
#Foor discover trends not fully sure yet (maybe look at predicted next platform/cost/rating/sales, best companies/platforms, etc.)
#game.drop_duplicates to filter out dupicates names in columns
#.groupby makes it so that the databse in grouped by that column
#applymap = apply to whole database

MSG = ['Name', 'Genre', 'ESRB_rating', 'Platform', 'Publisher', 'Developer', 'Critic_Score', 'User_Score',
       'Average_Score','Total_Shipped','Global_Sales', 'NA_Sales', 'PAL_Sales' , 'JP_Sales' ,'Other_Sales', 'Year',
        'Column Graph', 'Histogram', 'Scatter Plot'] #List with column names and possible things to do with program


gamedataa = pd.read_csv("gamedataa.csv", delimiter=',')
#Making the code take the csv and store it in gamedataa, with a comma as the seperator
gamedatab = pd.read_csv("gamedatab.csv", delimiter=',') #Same as above but for b
gamedata = pd.concat([gamedataa, gamedatab]) #Combine datasets
sns.set(style="ticks") #Changes style of the graph
pd.set_option('display.expand_frame_repr', False) #Makes it so that when I show a row from the dataset, it shows the full column
millionizer = lambda x: x*1000000 #A lambda function, whcih multiples x by a million
gamedata[['Total_Shipped','Other_Sales','Global_Sales','NA_Sales','PAL_Sales','JP_Sales']] \
  = gamedata[['Total_Shipped','Other_Sales','Global_Sales','NA_Sales','PAL_Sales','JP_Sales']].apply(millionizer)
#Applies the lamda function to each of the columns, multiplying each by 1 million

def OG(): #Orifginal fuction which gathers user's inputa to usw later on
  counter = 0 #Defining variabel
  choice = input(' Do you want to know the types of data: y/n \n >> ')
  #Input where the answer gets stored in the previously defined variable, asks the user what to do
  if choice == 'y': #If statement that runs if this is true, and is skipped over if it is false
    while counter < 15: #while loops mean that this will keep happening unti the conditions are met
      print('*', MSG[counter]) #Instead of having a long print statement, I can just grab these from the list and print them one by one
      counter += 1 #For next item in the list
      time.sleep(1) #A delay was added to give time to process rather than it just being an info dump
  datachoice = input(' What type of data do you want to analyse? \n >> ') #Asks the user what thype of data they want to analyse
  choicelist.append(datachoice) #Stores this information in a list to be used later on
  choice = input(' Do you want to use graphs: y/n \n >> ')
  if choice == 'y':
    choice = input(' Do you want to know the types of graphs: y/n \n >> ')
    if choice == 'y':
      counter = 15 #Just in case the user didn't run the previous counter code
      while counter < 19:
        print('*', MSG[counter])
        counter += 1
        time.sleep(1)
    datachoice = input(' What type of graph do you want to use? \n >> ')
    choicelist.append(datachoice) #Adds what the user is doing to the data to the list
  elif choice == 'no': #elif means that if the previous if statement was true, this one will be skipped over.
    #It is done to improve efficiency and optomise the code instead of checking multiple if statements
    choice = input(' Do you want to know what you can do: y/n \n >> ')
    if choice == 'y':
      counter = 21
      while counter < 25:
        print('*', MSG[counter])
        counter += 1
        time.sleep(1)
    datachoice = input(' What do you want to use? \n >> ')
    choicelist.append(datachoice)

def TGO(): #This is the function where the actual data analysis wil happen
  datavar = choicelist[0] #The first item in the list (lists start from 0) is assigned to a variable to make it easier to use (data type)
  if choicelist[1] == 'Column Graph': #Checks second item, the method of analysing
    gamedata[datavar].value_counts().plot.bar() #This adds up all of the same item with the column.
    #Eg: For year, it would count how meany there are of each year
    plt.title('Top ' + datavar + ' with most games') #Sets teh title to 'top whatever the data is with most games
    plt.yscale('log')  #Changes the scale to log as with the values present, a normal graph would be hard to interpret
    plt.show() #shows graph
  elif choicelist[1] == 'Histogram':
    try: #It will try and execute this code, but if it doesn't work, it will go to the exept part on line 80
      #This is because histograms will give an error when there aare non-numerical values, and this stops the code from breaking
      gamedata.hist(column=datavar); #Makes a histogram with the value being graphed being the column of whatever data the user wanted
      plt.show()
    except:
      print("You can't make a Histogram with non-numerical values")  # Informs the user of their mistake
  elif choicelist[1] == 'Scatter Plot':
    datachoice = input(' What data do you want to compare this data too? \n >> ')
    #For a scatter plot, we need a second data type to compare the two
    #Later, this will eb integrated into the OG function
    choicelist.append(datachoice) #Adds the choice to a list
    datavar2 = choicelist[2] #Makes it a variable to be used later
    sns.regplot(gamedata[datavar], gamedata[datavar2])
    #This uses seaborn to graph the data as is provides a line of best fit, which matplotlib doesn't without significant work
    #gamedata.plot.scatter(x = datavar, y = datavar2, s=100, c='black');
    # Show line of best fit formula
    z = gamedata[[datavar, datavar2]].copy() #Makes a copy of the column I used before for later use
    z.dropna(inplace=True)  #Drops all n/a values as they can cause errors
    x = z[datavar] #Assigns the first column a variable
    y = z[datavar2] #Assigns the 2nd column a variable
    m, b = np.polyfit(x, y, 1) #m=slope, b=intercept, numpy.polyfit finds polynonmial, (x-axis, y-axis, degree)
    print( 'The ', datavar2, ' can be found through the formula: ', datavar2, ' = ', m,'*', datavar,' + ', b )
    #Prints the formula for finding the 2nd datavalue based on what the first datavalue is
    plt.show() #shows the graph
    choice = input('Do you want to predict the expected value based off your value? \n >> ')
    #Allows the user to predict their value, by analysing previous one
    if choice == 'yes':
      value = float(input('What is your value? \n >> ')) #The float allows it to be seen as a number which is allowed a decimal plance
      value = m * value + b  #predicts the value by multiplying it by the gradient and adding the y-intercept
      print(value)  #rints out the value



  #elif choicelist[1] == 'Radar Graph':
  #elif choicelist[1] == 'Pie Chart':
  #elif choicelist[1] == '':



#OG()

#Set seaborn graphs to a better style


#Group by platform
#platform = gamedata.groupby('Platform').sum()[1:11]

#gamedata["Platform"].value_counts().plot.bar()

#plt.title('10 Platforms with most games')

#plt.yscale('log')
#plt.show()



#plt.show()

#print(gamedata.head(25))


exit = 'start'
confirm = 'start'

while exit != 'no':
  #This will loop till exit equals no, letting the user rerun the code multiple times without starting and stopping the program
  while confirm != 'yes': #same thing as before but yes
    choicelist = []  # Defining list that I will add what the user wants to do into
    OG() #Runs the function OG, which stands for original, where the user will decide what they want to do
    print(choicelist) #prints the list that contains what the user wants to do
    confirm = input('Is this what you want to do?, (yes/no) ').lower()
    #The user decides whether they want to use what they entered, or pick something else, as the code will rerun if the don't agrre to using it
  confirm = 'start'
  #As I use confirm again next line, zI have to reset it so that it won't skip the next bit of code from already being yes
  while confirm != 'yes':
    TGO() #Runs the fuction TGO which executes what the user wants
    confirm = input('Is this what you want to do?, (yes/no) ').lower() #Confirmation of what they want, otherwise code will re run
  confirm = 'start'
  exit = input('Would you like me to do anything else for you today?, (yes/no) ').lower() #nFinal Confirmation before code ends

