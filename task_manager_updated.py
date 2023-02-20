#=====importing libraries===========
# import date and time functions
from datetime import date               
from datetime import datetime

# Creating the requested functions
# The first function: reg_user
def reg_user():
    # Starting the function
    print("\n-----------------\nYou are registering a new user. \n")
                
    # Getting the input
    newUserName = input("Please enter a new username: ")  
    
    # Check if the new username is already in the system or not. If yes, error message appears and ask the user to add another username. Check again the condition after that.
    while newUserName in userName:
        print("Sorry, the username you have entered already exists in the system.")
        newUserName = input("Please try another username: ")

    newPass = input("Thanks! Please enter a new password: ")
    confirmPass = input("Please confirm the new password: ")
                
    # Check the condition of correct confirming password
    while (confirmPass != newPass):
        confirmPass = input("Error! Passwords do not match. Please confirm your password again: ")

    # Open and add more data on user.txt file with the input data 
    print("\nThanks! The new user has been registered. \n-----------------\n")
    with open('user.txt', 'a') as file:
        file.write(f"\n{newUserName}, {newPass}")

# The second function: add_task
def add_task():
    # Starting the function
    print("\n-----------------\nYou are adding a new task. \n")
    # Getting the input
    newPerson = input("Please enter the name of the person doing the new task: ")
    newTask = input("Please enter title of the task: ")
    newDescription = input("Please enter the description of the task: ")
    newDueDate = input("Please enter the due date of the task: (Please write in 'DD MMM YYYY' format, ex: '20 Oct 1994') ")
            
    # Generate the current date
    today = date.today()
    todayFormated = today.strftime("%d %b %Y")       # I used the website https://www.programiz.com/python-programming/datetime/current-datetime to learn about adding the date and formatting it

    # Open and add more data on task.txt file with the input data 
    with open('tasks.txt', 'a') as file:
        file.write(f"\n{newPerson}, {newTask}, {newDescription}, {todayFormated}, {newDueDate}, No")

    print("\nThanks! A new task has been added. \n-----------------\n")

# The third function: view_all
def view_all():
    print("\n-----------------\nAll tasks will be shown: ")

    # Read and get data from tasks.txt file, then add them to the taskContent
    taskContent = ""
    with open('tasks.txt', 'r') as file:
        for i in file:
            taskContent += i

            # Filter the data and create a list of words using split function with delimiter are " " and ","
    taskContent = taskContent.replace("\n",", ")
    taskContentSplited = taskContent.split(', ')

            # Divide the list into small lists of information
    taskPerson = taskContentSplited[0:len(taskContentSplited):6]
    taskTitle = taskContentSplited[1:len(taskContentSplited):6]
    taskDescription = taskContentSplited[2:len(taskContentSplited):6]
    taskAssignedDate = taskContentSplited[3:len(taskContentSplited):6]
    taskDueDate = taskContentSplited[4:len(taskContentSplited):6]
    taskStatus = taskContentSplited[5:len(taskContentSplited):6]

            # Print the outcome nicely
    for i in range((len(taskPerson))):
                print(f"""
                _________________________________________ \n
                Task number:         {i}
                Task:                {taskTitle[i]}
                Assigned to:         {taskPerson[i]}
                Date assigned:       {taskAssignedDate[i]}
                Due date:            {taskDueDate[i]}
                Task completed?      {taskStatus[i]}
                Task description:    {taskDescription[i]} """)
            
    print("\nAll tasks have been shown. \n-----------------\n")

# The fourth function: view_mine
def view_mine():
    print("\n-----------------\nBelow is your task(s):")

    # Read and get data again from tasks.txt file (since the date may have changed already), then add them to the taskContent
    taskContent = ""
    with open('tasks.txt', 'r') as file:
        for i in file:
            taskContent += i
            
    # Filter the data and create a list of words using split function with delimiter are " " and ","
    taskContent = taskContent.replace("\n",", ")
    taskContentSplited = taskContent.split(', ')
            
    # Divide the list into small lists of information
    taskPerson = taskContentSplited[0:len(taskContentSplited):6]
    taskTitle = taskContentSplited[1:len(taskContentSplited):6]
    taskDescription = taskContentSplited[2:len(taskContentSplited):6]
    taskAssignedDate = taskContentSplited[3:len(taskContentSplited):6]
    taskDueDate = taskContentSplited[4:len(taskContentSplited):6]
    taskStatus = taskContentSplited[5:len(taskContentSplited):6]
    
    # Use enumerate function over taskPerson list then cast to a dictionary with key is the task number and key's value is the name of the person doing the task
    enumerateTaskPerson = enumerate(taskPerson)
    taskPersonDict = dict(enumerateTaskPerson)

    # Add one condition while the for loop is running
    # Print the outcome nicely 
    for i in range(len(taskPerson)):
        if nameInput not in taskPerson:
            print("You do not have any tasks!")
            break
        elif nameInput == taskPerson[i]:
            print(f"""_________________________________________ \n
                Task number:         {i}
                Task:                {taskTitle[i]}
                Assigned to:         {taskPerson[i]}
                Date assigned:       {taskAssignedDate[i]}
                Due date:            {taskDueDate[i]}
                Task completed?      {taskStatus[i]}
                Task description:    {taskDescription[i]} """)

    # Get input about the task the user want to edit with defensive coding
    while True:         # I learned from L1T27 docs about this block and I applied that into this project
        try:
            taskModifyNum = int(input("""\nDo you want to modify any task?
    If yes, please only enter the number of the task (above) that you want to modify.
    If no, please enter '-1' to come back the main menu
    Your choice: """))
            break
        except ValueError:
            print("Sorry! That was not a valid number. Please try again! ")

    # The code below guarantee that the user put the number in range of -1 and total number of tasks
    while  taskModifyNum >= len(taskTitle) or taskModifyNum < -1:
            taskModifyNum = int(input("""\nSorry, you entered a wrong number or the input number was too big.
            Please choose your task's number or '-1' to come back: """))

    # Check the condition to guarantee that the user input the number of their task only
    # Also, only allow the user to modify the task with "No" in status
    if taskModifyNum > -1 and taskPersonDict[taskModifyNum] == nameInput and taskStatus[taskModifyNum] == "No": 

        # Get input about the action wanted to do, then let the user follow the instructions to complete the action they want to do
        taskAction = input(f"""\nWhat do you want to with task {taskModifyNum}: 
                a - Mark the task as complete
                b - Edit the task
                Your choice is: """).lower()
        if taskAction == "a":
            taskStatus[taskModifyNum] = "Yes"
            print(f"\nThanks! The status of the task {taskModifyNum} has been updated.")
        elif taskAction == "b":
            taskEdit = input("""\nWhat do you want to edit?:
                    a - The person doing the task
                    b - The task's due date
                    Your choice: """).lower()
            if taskEdit == "a":
                newTaskPerson = input("\nWho is the new person doing the task?: ")
                taskPerson[taskModifyNum] = newTaskPerson
                print("\nThanks! The person doing the task has been updated.")
            elif taskEdit == "b":
                newTaskDueDate = input("\nWhat is the new due date of the task?: (please write in DD MMM YYYY format, ex: 20 Oct 1994) ")
                taskDueDate[taskModifyNum] = newTaskDueDate
                print("\nThanks! The task's due date has been updated.")
            else:
                print("\nSorry, you had a wrong choice. Try again later.")
        else:
            print("\nSorry, you had a wrong choice. Try again later.")

    elif taskModifyNum > -1 and taskPersonDict[taskModifyNum] == nameInput and taskStatus[taskModifyNum] == "Yes":
        print("\nSorry, this task has already been completed, so you cannot modify it anymore. See you later!")

    elif taskModifyNum > -1 and taskPersonDict[taskModifyNum] != nameInput:
        print("\nSorry, you chose the task of another person. Try again later!")

    elif taskModifyNum == -1:
        print("\nThanks! See you later!")

    # Overwrite the new task information on the file tasks.txt 
    with open("tasks.txt","w") as file: 
        for i in range(len(taskPerson)-1):  # This code has range(len(taskPerson)-1) to prevent adding the /n in the end of the new tasks.txt file   
            file.write(f"{taskPerson[i]}, {taskTitle[i]}, {taskDescription[i]}, {taskAssignedDate[i]}, {taskDueDate[i]}, {taskStatus[i]}\n")
        
        # This code also is here to add the last task and to prevent adding the /n in the end of the new tasks.txt file 
        file.write(f"{taskPerson[len(taskPerson)-1]}, {taskTitle[len(taskPerson)-1]}, {taskDescription[len(taskPerson)-1]}, {taskAssignedDate[len(taskPerson)-1]}, {taskDueDate[len(taskPerson)-1]}, {taskStatus[len(taskPerson)-1]}")     
              
    print("\n-----------------\n")

def generate_reports():
    # Getting and filtering the content about the tasks again because the content may have changed already 
    taskContent = ""
    with open('tasks.txt', 'r') as file:
        for i in file:
            taskContent += i

    taskContent = taskContent.replace("\n",", ")
    taskContentSplited = taskContent.split(', ')

    taskPerson = taskContentSplited[0:len(taskContentSplited):6]
    taskTitle = taskContentSplited[1:len(taskContentSplited):6]
    taskDueDate = taskContentSplited[4:len(taskContentSplited):6]
    taskStatus = taskContentSplited[5:len(taskContentSplited):6]

    # Create the yesTasks list and add there the tasks with "yes" status in taskStatus
    yesTasks = []
    for i in taskStatus:
        if i == "Yes":
            yesTasks.append(i)

    # Generate the number of completed and incompleted tasks
    completeTasks = len(yesTasks)
    incompleteTasks = len(taskStatus) - completeTasks

    # Convert the time string to date format, then add to the taskDueDateFormated list
    taskDueDateFormated = []
    for i in taskDueDate:
        taskDueDateFormated.append(datetime.strptime(i, "%d %b %Y"))   # I used the website https://stackoverflow.com/questions/32287708/python-compare-the-date-in-the-string-with-todays-date to know about how to convert the string to date time format

    # Compare the task due date with today, then add the overdue date to the created list
    overdueTask = []
    for i in range(len(taskStatus)):
        if taskDueDateFormated[i] < datetime.today() and taskStatus[i] == "No":
            overdueTask.append(taskStatus[i])

    # Generate the number of overdue tasks
    overdueTaskNum = len(overdueTask)        

    # Create and write on the file task_overview.txt the outcomes about the tasks (string overviewTasks)
    overviewTasks = f"""The total number of tasks that have been generated and tracked using the task_manager.py: {len(taskTitle)} task(s)
The total number of completed tasks: {completeTasks} task(s)
The total number of uncompleted tasks: {incompleteTasks} task(s)
The total number of tasks that haven't been completed and that are overdue: {overdueTaskNum} task(s)
The percentage of tasks that are incomplete: {round(incompleteTasks/len(taskTitle)*100,2)}% ({incompleteTasks}/{len(taskTitle)} task(s)) 
The percentage of tasks that are overdue: {round(overdueTaskNum/len(taskTitle)*100,2)}% ({overdueTaskNum}/{len(taskTitle)} task(s))"""
    
    with open("task_overview.txt", "w") as file:
        file.write(overviewTasks)

    # Getting and filtering the content about the  users again because the content may have changed already
    userContent = ""
    with open('user.txt', 'r') as file:
        for i in file:
            userContent += i 
    
    userContent = userContent.replace("\n",", ")
    userList = userContent.split(', ')
    userName = userList[0:len(userList):2]

    # Creat a list containing lists of counters
    countList = []
    for i in userName:                      # Iteraing over the username list
        count = [0,0,0]                     # Restart the counter list
        for u in range(len(taskPerson)):    # Iteraing over the taskPerson list
            if i == taskPerson[u] and taskStatus[u] == "No" and taskDueDateFormated[u] < datetime.today():
                count[0] += 1               # This counter is for the task hasn't been completed and overdued of user i
            elif i == taskPerson[u] and taskStatus[u] == "No":
                count[1] += 1               # This counter is for the incompleted tasks of user i
            elif i == taskPerson[u] and taskStatus[u] == "Yes":
                count[2] += 1               # This counter is for the completed tasks of user i
        countList.append(count)             # Add to the list before restarting and moving on to the next user

    # Create and write on the file user_overview.txt the outcomes about the users
    with open("user_overview.txt", "w") as file:
        file.write(f"The total number of users registered with task_manager.py: {len(userName)} user(s)\n")
        file.write(f"The total number of tasks that have been generated and tracked using task_manager.py: {len(taskTitle)} task(s)\n")
        for i in range(len(userName)):
            file.write(f"\nOverview about user '{userName[i]}':")
            if sum(countList[i]) == 0:
                file.write(f"\n\t'{userName[i]}' does not have any tasks!")
            else:
                file.write(f"""
        The total tasks assigned: {sum(countList[i])} task(s)
        The percentage of the total number of tasks that have been assigned compared to total tasks: {round(sum(countList[i])/len(taskTitle)*100,2)}% ({sum(countList[i])}/{len(taskTitle)} task(s))
        The percentage of the tasks assigned that have been completed: {round(countList[i][2]/sum(countList[i])*100,2)}% ({countList[i][2]}/{sum(countList[i])} task(s))
        The percentage of the tasks assigned to that user that must still be completed: {round(countList[i][1]/sum(countList[i])*100,2)}% ({countList[i][1]}/{sum(countList[i])} task(s))
        The percentage of the tasks assigned to that have not yet been completed and are overdue: {round(countList[i][0]/sum(countList[i])*100,2)}% ({countList[i][0]}/{sum(countList[i])} task(s))""")

def display_statistics():
    generate_reports()              # I call the function generate_report() before the block code of display statistics function, just in case the admin did not generate the reports before displaying them.
    print("\n-----------------\nBelow is the statistics of the system:")
    
    print("\nOverview about tasks:\n")
    
    taskOverviewContent = ""        # Read the content in task_overview.txt
    with open("task_overview.txt", "r") as file:
        for i in file:
            taskOverviewContent += i

    print(taskOverviewContent)      # Print out the report

    print("\nOverview about users:\n")

    userOverviewContent = ""        # Read the content in user_overview.txt
    with open("user_overview.txt", "r") as file:
        for i in file:
            userOverviewContent += i

    print(userOverviewContent)      # Print the report

    print("\n-----------------\n")

#====Login Section====
print("Hello! Welcome to the task manager.")  
# Get the input about username and password
userContent = ""
with open('user.txt', 'r') as userFile:
    for i in userFile:
        userContent += i 

userContent = userContent.replace("\n",", ") # Bring lines in one line and words now are divides by "," and " " 
userList = userContent.split(', ')           # Split the line into list of words with delimiters are "," and " "
    
# Create lists of usernames and passwords
userName = userList[0:len(userList):2]
userPass = userList[1:len(userList):2]

# Create a list of pairs containing username and its correspondent password. 
# Used tuple knowledge from: https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuples
userLogin = []
for i in range(len(userName)):
    userLogin.append((userName[i],userPass[i]))

# Get the input about login data from the user
nameInput = input("Please enter your username: ")
passInput = input("Please enter your password: ")

# Checking username and password repeatedly using While loop
while (nameInput,passInput) not in userLogin:
    if (nameInput in userName) and (passInput not in userPass):
        print("Username is correct but password is incorrect! Try again.")
        passInput = input("Try another password: ")

    elif (nameInput not in userName) and (passInput in userPass):
        print("Password is correct but username is incorrect! Try again.")
        nameInput = input("Try another username: ")

    elif (nameInput not in userName) and (passInput not in userPass):
        print("Both username or password are incorrect! Try again.")
        nameInput = input("Try another username: ")
        passInput = input("Try another password: ")

    else:
        print("Username and Password are not matched! Try again.")
        nameInput = input("Please enter another username: ")
        passInput = input("Please enter another password: ")

# After passing the login section, if the username is "admin" (and of course the its password was correct before that already), 
# the menu with an added option is opened
if nameInput == "admin":
    print("\nAccess is granted as an admin! \n")
    # Opening the menu
    while True:
        menu = input('''Select one of the following options below:
    r  - Register a user
    a  - Add a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e  - Exit
    Your choice is: ''').lower()
     
    # Option 1: Registering a user 
        if menu == 'r':
            reg_user()

    # Option 2: Adding a task
        elif menu == 'a':
            add_task()

    # Option 3: View all tasks   
        elif menu == 'va':
            view_all()

    # Option 4: View the tasks of the user having nameInput username   
        elif menu == 'vm':
            view_mine()

    # Option 5: Generate reports
        elif menu == "gr":
            generate_reports()
            print("\n-----------------\n\nThanks! Two reports task_overview.txt and user_overview.txt have been generated")
            print("\n-----------------\n")

    # Option 6: Display statistics of the system
        elif menu == "ds":
            display_statistics()

    # Last options
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice! Please try again.")

# After passing the login section, if the username is not "admin", a normal menu is opened

else: 
    print("\nAccess is granted! \n")

    while True:
        menu = input('''Select one of the following options below:
    a  - Add a task
    va - View all tasks
    vm - View my task
    e  - Exit
    Your choice is: ''').lower()

        if menu == 'a':
            add_task()
        
        elif menu == 'va':
            view_all()
    
        elif menu == 'vm':
            view_mine()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice! Please try again.")