print("                         \nWELCOME! TO YOUR 'TO-DO-LIST'")

tasks = ["Python","Web Development","Reading books"]
while True:
    def display_tasks(tasks):
        if not tasks:
            print("There are no tasks")
        else:
            for i, task in enumerate(tasks):  
                print(f"{i+1}. {task}")  
                



    def add_tasks(tasks):
        t = input("Enter your new task: ")
        tasks.append(t)
        print(f"\nYour new tasks are:")
        for i, task in enumerate(tasks):  
            print(f"{i+1}. {task}")  



    def remove_tasks(tasks):
        r = input("Enter the task you want to remove: ")
        tasks.remove(r)

        print(f"\nYour new tasks are:")
        for i, task in enumerate(tasks):  
            print(f"{i+1}. {task}")  



    def main():
        try:
            a = int(input("Hello there!, Type: '1' for Displaying tasks, '2' for adding tasks and '3' for removing tasks: "))
        except:
            print("Invalid Input, please try again.")

        if a == 1: 
            print("Sure here are your tasks: ")
            return display_tasks(tasks)
        elif a == 2:
            return add_tasks(tasks)
        try:
            if a == 3:
                return remove_tasks(tasks)
        except:
            print("Please enter the correct name of the task")
    main()
