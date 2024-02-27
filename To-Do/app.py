

def menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")
my_tasks = []
def add():
      task = input("Add your task description ")
      my_tasks.append(task)
      print("Task added succesfully! ")
def view():
      if my_tasks.count != 0:
        for index, task in enumerate(my_tasks, start=1):
            print(f"{index}. {task}")

def mark():
    if(my_tasks.count != 0):
        view()
        remove = int(input("Enter the number of task you want to complete: ")) - 1
        my_tasks.pop(remove)
    else:
         print("No task left")
print

def main():
     
        
        while True:
            menu()
            choice = input("Choose from the above menu: ")
            if choice == "1":
                    add()
            elif choice == "2":
                  view()
            elif choice == "3":
                  mark()
            else:
                  print("Goodbye!")
                  break 
            

if __name__ == "__main__":
    main()