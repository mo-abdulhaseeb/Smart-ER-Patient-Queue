*Hospital ER Triage System:*
This project models an emergency room waiting list using a priority queue. It ensures patients are seen based on how urgent their condition is, not just when they arrived.

*The Problem:*
Standard waiting lines work on a first-come-first-served basis. In a hospital ER, this could mean someone with a minor issue gets treated before someone having a heart attack just because they arrived earlier. This isn't just inefficient - it's dangerous.

*How This Solution Works:*
Instead of a regular queue, this system uses a max-heap structure to prioritize patients. Each patient gets a triage level from 1 (most critical) to 5 (least critical). The system automatically keeps the most urgent patient at the front.

Key features:
-Patients are sorted by medical urgency
-Adding or removing patients takes O(log n) time
-The most critical patient is always next in line
-Works like real hospital triage systems

*Why This Matters:*
This approach demonstrates how the right data structure can solve real-world problems. In an ER, proper prioritization saves lives. This system shows how computer science concepts can directly impact critical healthcare decisions.

