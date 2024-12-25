''' Elevator Scheduling with Bubble Sort
# Problem Statement:
# You're tasked with designing a simplified elevator system for a small building. The elevator serves multiple floors and needs to efficiently handle passenger requests.
# Task:
#  * Initialize: Set the elevator's starting floor and the total number of floors in the building.Done
#  * Receive Requests: Create a list to store floor requests (both pick-up and drop-off).Done
#  * Optimize Movement: Use bubble sort to arrange the floor requests in ascending or descending order based on the elevator's current position. This will help determine the most efficient route for the elevator.
#  * Simulate Movement: Simulate the elevator's movement by iterating through the sorted floor requests. The elevator should travel to each requested floor, pick up or drop off passengers as needed, and then  to the next move requested floor.'''
totalfloor=7
startfloor=3
floor=[5,2,4,1,6]
numb=len(floor)
for r in range(numb-1):
    for l in range(numb-1):
        if floor[l]>floor[l+1]:
            r=floor[l]
            floor[l]=floor[l+1]
            floor[l+1]=r
print(floor)
# 2,1,4,5,6
