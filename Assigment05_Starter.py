# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Derek Janusz>,<11/15/2021>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
saveFile= "ToDoToDoList.txt" #create file to save dat
strTask =""
strPriority=""
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(strFile, "w")
dicRow = {"Task":"Work","Priority": "1"}
objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
dicRow = {"Task":"Excercise","Priority": "2"}
objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")  # Returns a list!
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
            print(dicRow)
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        objFile = open(strFile, "a")
        strTask= input("Enter a task: ")
        strPriority = input("Enter a priority: ")
        dicRow= {"Task": strTask, "Priority": strPriority} #got the dictionary to work after yusing a lstTable
        objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + '\n')
        #lstTable= [dicRow["Task"], dicRow["Priority"]] #this was my trial, using this as it says to use a table
        #objFile.write(lstTable[0]+ "," + lstTable[1] +'\n') #puts info into the file
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        with open(strFile, "r") as File:
        #objFile = open(strFile, "r")
            lines=File.readlines()
            #objFile =  open(strFile, "w")
        remove= input("Enter the line you would data you want to remove as in the following format Work,priority. Example, if entered Clean and priority 3, you would enter: Clean,3")
        with open(strFile,"w") as File:
            for line in lines:
                if line.strip("\n") != remove :
                    File.write(line)
        #objFile.close()
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        #create a new file to save it in
        copyFile = open(strFile, "r") # read the data in the ToDO list
        objFile = open(saveFile, "w")
        #save data from text file to this one, and save it when the program exits
        for row in copyFile:
            lstRow = row.split(",")  # Returns a list!
            dicRow = {"Name": lstRow[0], "Value": lstRow[1]}
            objFile.write(dicRow["Name"] + ',' + dicRow["Value"] + '\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
