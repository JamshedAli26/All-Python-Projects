def task():
    tasks = []
    print(".......... WELCOME TO THE TASK MANAGEMENT APP.......")

    total_task = int(input("Enter how many task do you want to add: "))
    for i in range (1, total_task+1):
        task_name = input(f"Enter task{i}: ")
        tasks.append(task_name)
    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter\n1-add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/:"))
        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task {add} has been Successfully add")
            print(f"Total tasks : {total_task}")
        
        elif operation == 2:
            updated_val = input("Enter task you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task: ")
                idx = tasks.index(updated_val)
                tasks[idx] = up
                print(f"Updated task {up}")
                print(f"Total tasks : {total_task}")

        elif operation == 3:
            del_val = input("Which task do you want to delete: ")
            if del_val in tasks:
                idx = tasks.index(del_val)
                del tasks[idx]
                print(f"Task f{del_val} has been deleted successfully")
                print(f"Total tasks : {total_task}")
            
        
        elif operation == 4:
            print(f"Total tasks = {total_task}: {tasks}")
        
        elif operation == 5:
            print(f"Program closed...")
            break
            
        else:
            print("Invalid input")
task()