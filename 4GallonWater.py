"""
4 Gallon Water Bucket Problem

Objective: 
This program solves the classic water measurement problem where two kids need to 
fetch exactly 4 gallons of water from a stream using only two unmarked buckets: 
- One 5-gallon bucket (defined as bucket1 in the code)
- One 3-gallon bucket (defined as bucket2 in the code)

This program uses Breadth-First Search (BFS) to find the optimal solution in 
minimum steps and returns all possible solutions in less than 15 steps.

--code by Dora Jiayue Li

"""

from collections import deque

class FourGallonWaterSolver:
    def __init__(self, bucket1_capacity, bucket2_capacity, target):
        self.bucket1_capacity = bucket1_capacity  # 5-gallon bucket
        self.bucket2_capacity = bucket2_capacity  # 3-gallon bucket
        self.target = target
    
    def get_possible_actions(self, state):
        """Generate all possible actions from current state"""
        bucket1, bucket2 = state  # bucket1 = 5-gallon, bucket2 = 3-gallon
        actions = []
        
        # Fill bucket1 (5-gallon bucket)
        if bucket1 < self.bucket1_capacity:
            actions.append((self.bucket1_capacity, bucket2, f"Fill 5-gallon bucket"))
        
        # Fill bucket2 (3-gallon bucket)
        if bucket2 < self.bucket2_capacity:
            actions.append((bucket1, self.bucket2_capacity, f"Fill 3-gallon bucket"))
        
        # Empty bucket1 (5-gallon bucket)
        if bucket1 > 0:
            actions.append((0, bucket2, f"Empty 5-gallon bucket"))
        
        # Empty bucket2 (3-gallon bucket)
        if bucket2 > 0:
            actions.append((bucket1, 0, f"Empty 3-gallon bucket"))
        
        # Pour from bucket1 to bucket2 (5-gallon to 3-gallon)
        if bucket1 > 0 and bucket2 < self.bucket2_capacity:
            pour_amount = min(bucket1, self.bucket2_capacity - bucket2)
            new_bucket1 = bucket1 - pour_amount
            new_bucket2 = bucket2 + pour_amount
            actions.append((new_bucket1, new_bucket2, f"Pour {pour_amount} gallon(s) from 5-gallon to 3-gallon bucket"))
        
        # Pour from bucket2 to bucket1 (3-gallon to 5-gallon)
        if bucket2 > 0 and bucket1 < self.bucket1_capacity:
            pour_amount = min(bucket2, self.bucket1_capacity - bucket1)
            new_bucket1 = bucket1 + pour_amount
            new_bucket2 = bucket2 - pour_amount
            actions.append((new_bucket1, new_bucket2, f"Pour {pour_amount} gallon(s) from 3-gallon to 5-gallon bucket"))
        
        return actions
    
    def is_goal_state(self, state):
        """Check if current state contains the target amount"""
        bucket1, bucket2 = state  # bucket1 = 5-gallon, bucket2 = 3-gallon
        return bucket1 == self.target or bucket2 == self.target
    
    
    def find_all_solutions(self, max_steps=15):
        """Find all solutions within max_steps limit
            A "state" here is simply the amount of water in each bucket at any given moment, represented as a pair of numbers like (5, 0), 
            meaning the 5-gallon bucket is full and the 3-gallon bucket is empty.
            First starts with initialization of both buckets are empty.
            Then, continues to search out possible actions, and add the actions and states into the queue. Each time pulls a state from the front of the queue.
            It checks if the current state is the goal (Does either bucket have 4 gallons?). 
            If it is, the path taken to reach this state is saved as a solution.
        """
        initial_state = (0, 0)
        queue = deque([(initial_state, [])])
        visited = {}
        solutions = []
        
        while queue: #continue until queue is empty
            current_state, path = queue.popleft()  # Breadth-first search，process from shortest solutions
            
            if self.is_goal_state(current_state):
                solutions.append((path, current_state))
                continue
            
            # Skip if found a shorter path to this state
            if current_state in visited and visited[current_state] <= len(path):
                continue
            visited[current_state] = len(path)
            
            # Skip if path is too long
            if len(path) >= max_steps:
                continue
            
            # Generate all possible next states and add them to queue
            # Each of these new states, along with the action that led to it (e.g., "Fill 5-gallon bucket"), is added to the back of the queue.
            for new_state in self.get_possible_actions(current_state):
                new_bucket1, new_bucket2, action = new_state
                new_state_tuple = (new_bucket1, new_bucket2)
                new_path = path + [action]
                queue.append((new_state_tuple, new_path))
        
        # Sort solutions by length
        solutions.sort(key=lambda x: len(x[0]))
        return solutions
    

def main():
    # Problem parameters
    bucket1_capacity = 5  # 5-gallon bucket
    bucket2_capacity = 3  # 3-gallon bucket
    target = 4            # we want to reach 4 gallons
    
    solver = FourGallonWaterSolver(bucket1_capacity, bucket2_capacity, target)
    
    print("=== 4Gallon Water - Bucket Problem Solver ===")
    print(f"Bucket 1 capacity: {bucket1_capacity} gallons (5-gallon bucket)")
    print(f"Bucket 2 capacity: {bucket2_capacity} gallons (3-gallon bucket)")
    print(f"Target: {target} gallons")
    print(f"Goal: Find solution in less than 15 steps\n")
    
    # Print out all solutions
    all_solutions = solver.find_all_solutions()
    
    if all_solutions:
        print(f"\n✓ Found {len(all_solutions)} different solution(s):")
        
        for i, (path, state) in enumerate(all_solutions, 1):
            target_bucket = "5-gallon bucket" if state[0] == target else "3-gallon bucket"
            print(f"\nSolution {i}: {len(path)} steps (target in {target_bucket})")
            print("Steps:")
            print("  0. Initial state: Both buckets empty (0, 0)")
            for j, step in enumerate(path, 1):
                print(f"  {j}. {step}")
            print(f"  Final state: {state}")
        
        shortest_steps = len(all_solutions[0][0])
        print(f"\n✓ Success! Shortest solution found in {shortest_steps} steps (< 15 steps)")
    else:
        print("No solutions found!")
   
if __name__ == "__main__":
    main()