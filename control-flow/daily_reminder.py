task_var = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match task_priority.lower():
    case 'high':
        if time_bound.lower() == "yes":
            print(f"Reminder:'{task_var}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task_var}' is a high priority task. Aim to schedule time for it today.")
    
    case 'medium':
        if time_bound.lower() == 'yes':
            print(f"Reminder: '{task_var}' is a medium priority task with a deadline. Plan accordingly.")
        else:
            print(f"Note: '{task_var}' is a medium priority task. Schedule time for it this week.")

    case 'low':
        if time_bound.lower() == 'no':
            print(f"'{task_var}' is a low priority task. Consider completing it when you have free time")
        else:
            print(f"Note: '{task_var}' is low priority but time-bound. Ensure it is completed before the deadline.")



