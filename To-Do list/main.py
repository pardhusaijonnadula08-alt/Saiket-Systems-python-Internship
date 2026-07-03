class Task:
    def __init__(self,lists):
        self.lists = lists
        self.completed = False
    def mark_completed(self):
        self.completed = True

tasks = {}
counter = 1
while True:
    print("\n TO-Do list applicatiom ")
    print(" 1.Add Task \n 2.Show Tasks \n 3.Mark as Complete [✓] \n 4.Delete Task \n 5.Exit App")
    
    choices = input("Enter your choice (1-5): ")

    #1 Adding tasks
    if choices == '1':
        lists = input("Enter the tasks to be added: ")
        task = Task(lists)
        tasks[counter]=task
        print(f"Task added as ID {counter}")
        counter += 1

    #2 showing the existed tasks
    elif choices == '2':
        if not tasks:
            print("To-Do list is empty..!")
        else:
            print("\n your tasks are: ")
            for task_id , task_obj in tasks.items():
                status = "[✓]" if task_obj.completed else "[]"
                print (f"ID {task_id}: {status} {task_obj.lists}")

    #3 Mark as complete
    elif choices == '3':
        if not tasks:
            print("No tasks available to mark as complete.!")
        else:
            try:
                target_id = int(input("Enter the task ID to be marked as completed: "))
                if target_id in tasks:
                    tasks[target_id].mark_completed()

                    # Deletes automatically
                    tasks.pop(target_id)
                    print(f"Auto-Delete task ID {target_id} removed from your list")
                else:
                    print("Invalid ID, Task not Found..!")
            except ValueError:
                print("Please enter a valid numeric ID ")

    #4 Deleting tasks
    elif choices == '4':
        if not tasks:
            print("No task is available to delete..!")
        else:
            try:
                target_id = int(input("Enter the ID of Task to  Delete: "))
                if target_id in tasks:
                    removed_task = tasks.pop(target_id)
                    print(f"Task {removed_task.lists} has been deleted..!")
                else:
                    print("Invalid ID,Task not Found..!")
            except ValueError:
                print("Please enter the valid numeric ID ")
        
    #5 Exiting app
    elif choices == '5':
        print("\n Goodbye..! Have a goodDay..!!")
        break
    else:
        print("Invalid choice please enter the number from (1-5): ")
