task_var = input("Your task Description: ")
task_priority =  input("Priority Level (high, medium, low): ")
time_bound = input("Is the task time bound? (Yes or No): ")

match task_priority:
    case n if n == 'high':
        if time_bound == "Yes":
            print(f"'{task_var}' is a high priority task that requires immediate attention today!")
        else:
            print()
    case n if n == 'low':
        if time_bound == 'No':
            print(f"'{task_var}' is a low priority task. Consider completing it when you have free time")