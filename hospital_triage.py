class Patient:
    def __init__(self, name, triage_level, arrival_time):
        self.name = name
        self.triage_level = triage_level
        self.arrival_time = arrival_time

    def __str__(self):
        return f"{self.name} (Level: {self.triage_level}, Arrived: {self.arrival_time})"

class TriageQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _has_left_child(self, index):
        return self._left_child(index) < self.size

    def _has_right_child(self, index):
        return self._right_child(index) < self.size

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def add_patient(self, patient):
        self.heap.append(patient)
        self.size += 1
        self._bubble_up(self.size - 1)

    def _bubble_up(self, index):
        while index > 0:
            parent_idx = self._parent(index)
            if self.heap[parent_idx].triage_level > self.heap[index].triage_level:
                self._swap(parent_idx, index)
                index = parent_idx
            else:
                break

    def get_next_patient(self):
        if self.size == 0:
            return None
        
        next_patient = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        self._bubble_down(0)
        return next_patient

    def _bubble_down(self, index):
        while self._has_left_child(index):
            left_idx = self._left_child(index)
            right_idx = self._right_child(index)
            smaller_idx = left_idx

            if self._has_right_child(index) and self.heap[right_idx].triage_level < self.heap[left_idx].triage_level:
                smaller_idx = right_idx

            if self.heap[index].triage_level < self.heap[smaller_idx].triage_level:
                break
                
            self._swap(index, smaller_idx)
            index = smaller_idx

    def peek(self):
        return self.heap[0] if self.size > 0 else None

    def display_queue(self):
        if self.size == 0:
            print("Queue is empty.\n")
            return
            
        print("\nCurrent Triage Queue:")
        for i, patient in enumerate(self.heap):
            print(f"  {i+1}. {patient}")
        print()

def main():
    er_queue = TriageQueue()
    
    print("=== HOSPITAL TRIAGE SYSTEM ===")
    print("Enter patients. Type 'done' for name to finish.\n")
    
    while True:
        name = input("Enter patient's name: ").strip()
        if name.lower() == 'done':
            break
            
        try:
            level = int(input("Enter triage level (1-5): ").strip())
            if level < 1 or level > 5:
                print("Error: Level must be between 1-5.\n")
                continue
                
            time = input("Enter arrival time (e.g., 10:00 AM): ").strip()
            
            er_queue.add_patient(Patient(name, level, time))
            print(f"Added {name} to the queue.\n")
            
        except ValueError:
            print("Error: Please enter a valid number for level.\n")
    
    er_queue.display_queue()
    
    print("Processing patients...\n")
    while er_queue.size > 0:
        next_patient = er_queue.get_next_patient()
        print(f"TREATING: {next_patient}")
        er_queue.display_queue()
        input("Press Enter to treat next patient...")
    
    print("All patients have been treated.")

if __name__ == "__main__":
    main()