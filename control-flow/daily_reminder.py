task_var = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match task_priority:
    case n if n == 'high':
        if time_bound == "Yes":
            print(f"'{task_var}' is a high priority task that requires immediate attention today!")
        else:
            print()
    case n if n == 'low':
        if time_bound == 'No':
            print(f"'{task_var}' is a low priority task. Consider completing it when you have free time")