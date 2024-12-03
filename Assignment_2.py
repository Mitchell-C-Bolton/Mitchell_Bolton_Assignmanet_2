# Initial global variables
task_list = [{'name':"Dishes", 'description': 'Wash the dishes.', 'dificulty': 4}, {'name':"Garbage", 'description': 'Take out the garbage.', 'dificulty': 7}]

# Exits the applicaiton if it receives "exit" from any input box within the application.
def exit_app(value):
    if value.lower() == 'exit':
        exit()
    
# Adds a task to the task_list list. 
def add_a_task():
    
    # Task Name: Loops until a user enters a valid input OR decides to exit the app.
    # Makes sure it's not blank and makes sure the task doesn't already exist
    task_name = input("\nWhat would you like to name your task: ")
    exit_app(task_name)
    if task_name == '':
        print("Task name can not be blank. Please try again.")
        add_a_task()
        return
    for item in task_list:
        if task_name.lower().strip() == item['name'].lower():
            print("Sorry, that task already exists, try again.")
            add_a_task()
            return
        
    # Task Description: Loops until a user enters a valid input OR decides to exit the app.
    # Makes sure it's not blank
    task_description_active = True
    while task_description_active:
        task_description = input("\nProvide a description for your task: ")
        exit_app(task_description)
        if task_description == '':
            print("Task name can not be blank. Please try again.")
            continue
        task_description_active = False

    
    # Task Dificulty: Loops until a user enters a valid input OR decides to exit the app.
    # Makes sure it's not blank
    task_dificulty_active = True
    while task_dificulty_active:
        try:
            task_dificulty = input("\nOn a scale of 1-10, how dificult is this taks?: ")
            exit_app(task_dificulty)
            task_dificulty = int(task_dificulty)
            if task_dificulty not in range(11):
                print('Sorry, Your task dificulty needs to be between 1-10.')
                continue
            task_dificulty_active = False
        except ValueError:
            print('Sorry, your task dificulty needs to be a whole number.')
        finally: 
            continue
            # I understand splitting finally from except ValueError is pointless in this case
            # I just did it to meet assignment requirements as it functions the same.
        
        
    # appends the three values to a dictionarry to the task_list list.
    task_list.append({'name':task_name.strip(), 
        'description':task_description.strip(), 
        'dificulty':task_dificulty})

# Deletes a dictionary from the task_list list.
def del_a_task():
    print()
    if task_list != []:
        deleted_task = False
        for key, item in enumerate(task_list):
            print(f"Task {key+1}: {item['name']}")
        task = input("Which task would you like to delete: ")
        exit_app(task)
        for key, dictionary in enumerate(task_list):
            if dictionary['name'].lower() == task.lower():
                del task_list[key]
                deleted_task = True
                if task_list != []:
                    delete_another_task = input("\nWould you like to delete another task? (y/n): ")
                    if delete_another_task.lower() == 'y':
                        del_a_task()
                    else:
                        break
        if deleted_task == False:
            print("\nThe task you listed doesn't exist.")
            print("Please make sure the task is spelled correctly and try again.")
            del_a_task()
    else:
        print("You have no tasks to delete!")
            

# Displays all tasks to the end user.
def show_tasks():
    if task_list != []:
        print("\n##############################################################")
        print("########################### Tasks ############################")
        print("##############################################################")
        for key, item in enumerate(task_list):
            print(f"#\n#  Task {key+1}: {item['name']}")
            print(f"#  Description: {item['description']}")
            print(f"#  Dificulty: {item['dificulty']}\n#")
            print("##############################################################")
    else:
        print("You have no tasks to show.")
    

# Initial text block for the customer that explains how to navigate the app.
print("\nWelcome to Taskly! Your one stop shop for task organization.\n")
print("########################## Commands ##########################")
print("# Add: Add a task to your list.")
print("# Delete: Delete a tack from your list.")
print("# View: Show your current tasks for the day.")
print("# Exit: Exit the app at any time.")
print("##############################################################")

# Customer decission tree decides based off an initial imput, what the user wants to do.
customer_decission_tree_active = True
while customer_decission_tree_active:
    customer_input = input("\nWhat would you like to do today? (Add/Delete/View/Exit): ")
    exit_app(customer_input)
    if customer_input.lower() == 'add':
        add_a_task()
    elif customer_input.lower() == 'delete':
        del_a_task()
    elif customer_input.lower() == 'view':
        show_tasks()
    else:
        print("\nSorry, that's not a valid input, please select if you want to add, delete, view, or exit.")