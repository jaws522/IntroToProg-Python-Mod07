# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with exceptions and pickling,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# JBrecht,8.11.2020,Modified code to complete assignment 6
# JBrecht,8.20.2020,Modified code to complete assignment 7
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
import pickle
strFileName = "ToDoFile.dat"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows, (string) status
        """
        list_of_rows.clear()  # clear current data
        # error handling
        try:
            file = open(file_name, "rb")
            list_of_rows = pickle.load(file)  # the un-pickle
            file.close()
        except FileNotFoundError:
            file = open(file_name, "wb")
            file.close()
            print("Task list empty.")
        except EOFError:
            print("No data in file.")
        return list_of_rows, 'Success!'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds a new dictionary row into a list of dictionary rows

        :param task: (string) name of task
        :param priority: (string) priority of task (L,M,H)
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows, (string) status
        """
        lstTable.append({"Task": task, "Priority": priority})
        return list_of_rows, 'Success!'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes a specific dictionary row from a list of dictionary rows

        :param task: (string) name of task
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows, (string) status
        """
        list_of_rows = [dicRow for dicRow in list_of_rows if dicRow["Task"] != task]
        return list_of_rows, 'Success!'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows into a file

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows, (string) status
        """
        file = open(file_name, "wb")
        pickle.dump(list_of_rows, file)  # the pickle
        file.close()
        return list_of_rows, 'Success!'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks To Do are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority(task_message, priority_message):
        """ Gets a task name and priority from the user

        :param task_message: (string) request for task name
        :param priority_message: (string) request for task priority
        :return: (string) task name, task priority
        """
        return str(input(task_message)).strip().lower(), str(input(priority_message)).strip().lower()

    @staticmethod
    def input_task_to_remove(message):
        """ Gets a task name from the user for removal

        :param message: (string) request for task name
        :return: (string) task name
        """
        return str(input(message)).strip().lower()


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority("Enter task name: ", "Enter task priority (L,M,H): ")
        lstTable, strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = IO.input_task_to_remove("Which task do you want to remove? ")
        lstTable, strStatus = Processor.remove_data_from_list(strTask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
