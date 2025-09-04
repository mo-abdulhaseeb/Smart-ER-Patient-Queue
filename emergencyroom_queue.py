from datetime import datetime

patients = []

def add_patient(name, level, time_str):
    
    time_obj = datetime.strptime(time_str, "%I:%M %p").time()
    patients.append((name, level, time_obj))
    show_queue()

def next_patient():
    if not patients:
        print("No patients in queue.\n")
        return
    patients.sort(key=lambda x: (x[1], x[2]))
    name, level, time = patients.pop(0)
    print(f"\nNEXT: {name} (Level {level}, Arrived: {time.strftime('%I:%M %p')})\n")
    show_queue()

def show_queue():
    if not patients:
        print("Queue is empty.\n")
    else:
        print("Current Queue:")
        patients.sort(key=lambda x: (x[1], x[2]))
        for p in patients:
            print(f"{p[0]} (Level {p[1]}, Arrived: {p[2].strftime('%I:%M %p')})")
        print()

print("Smart ER Queue")
print("Type patient name to add, 'next' to treat, 'quit' to exit.\n")

while True:
    name = input("Enter: ")

    if name.lower() == "quit":
        print("System closed.")
        break

    elif name.lower() == "next":
        next_patient()

    else:
        level = input("Enter urgency level (1-5): ")
        time_input = input("Enter arrival time (HH:MM AM/PM): ")
        if level in "12345":
            add_patient(name, int(level), time_input)
        else:
            print("Error: Level must be 1-5\n")
