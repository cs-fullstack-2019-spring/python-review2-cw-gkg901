def main():
    ex()


# Create a task list. A user is presented with the text below.
# Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.
# Make each option a different function in your program.
# Do NOT use Google. Do NOT use other students. Try to do this on your own.


def ex():
    # DELETE TASK FUNCTION
    def deleteTask(x):

        taskList.remove(x)

    taskList = ["Finish this project"]
    # PROGRAM START!!!!!!!!!!!!!!!!!!!
    print("Congratulations! You're running Gerren's Task List program.")

    userInput = ""
    while (userInput != 0):
        userInput = input(
            "What would you like to do next?\n 1. List all tasks.\n 2. Add a task to the list.\n 3. Delete a task.\n 0. to quit.\n")
        if userInput == "1":
            for items in taskList:
                print(items)


        elif userInput == "2":
            newTask = input("Enter your new task.\n")
            taskList.append(newTask)


        elif userInput == "3":
            print(taskList)
            ask = input("Delete which task?\n")
            if ask in taskList:
                deleteTask(ask)
            else:
                print("INVALID ENTRY")





        elif userInput == "0":
            break
        else:
            print("INVALID ENTRY")
            continue


if __name__ == '__main__':
    main()
