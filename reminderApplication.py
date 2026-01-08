import time
import threading

reminders = {}
def add_reminder():
    reminder_time = input("Enter reminder time (HH:MM, 24-hour format): ")
    message = input("Enter reminder message: ")
    
    reminders[reminder_time] = message
    print(f"Reminder set for {reminder_time}.")

def view_reminders():
    if not reminders:
        print("No reminders set.")
    else:
        print("\nYour Reminders:")
        for time_str, msg in reminders.items():
            print(f"At {time_str} -> {msg}")
    print()

def reminder_checker():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time in reminders:
            print(f"\n Reminder! {reminders[current_time]}")
            del reminders[current_time]  
        time.sleep(30) 

threading.Thread(target=reminder_checker, daemon=True).start()

while True:
    print("\nSimple Reminder App")
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_reminder()
    elif choice == "2":
        view_reminders()
    elif choice == "3":
        print("Exiting Reminder App. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
