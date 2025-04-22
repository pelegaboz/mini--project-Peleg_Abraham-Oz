#peleg Abraham Oz_211698196
#Mission 2
user_choice = "empty"
list_of_tasks= list()

print("Welcome to the Task Manager!")

while True:
    print("""Choose an option:
    1. Add task
    2. Show tasks
    3. Remove task
    4. Mark task as done
    5. Count tasks with keyword
    6. Exit""")
    user_choice = input("Your choice: ")

    if not user_choice.isnumeric():#check if number
        print("Invalid input. Please enter a number.")
        continue
    user_choice = int(user_choice)
    #לשנות למשתנה שעולה במקום מספרים
    if not 1 <= user_choice <= 6:#check if between 1-6
        print("Invalid choice. Please choose a number from 1 to 6.")
        continue
    if(user_choice==1):#add task to the list
       print("Enter new task")
       user_action=input()
       list_of_tasks.append(user_action + "[]")
       continue
    elif (user_choice == 2):#print the list
        print("2")
        continue
    elif (user_choice == 3):#remove task from the list
        task_to_remove= input("Enter task name to remove:")
        task_to_remove=task_to_remove.lower()
        if(task_to_remove in list_of_tasks):
            list_of_tasks.remove(task_to_remove)
        else:
            print("Task not found.")
        continue
    elif (user_choice == 4):
        print("4")
        continue
    elif (user_choice == 5):
        print("5")
        continue

    break

