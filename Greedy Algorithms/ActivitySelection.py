
def activitySelector(s, f):
    n = len(s)
    
    # Initialize selected activity array
    A = [0]
    
    for i in range(1, n):
        
        # Select activity that has start time greater or equal to finish time of previous activity
        if s[i] >= f[A[-1]]:
            A.append(i)
            
    return A
            
        
# Driver code

if __name__ == '__main__':
    
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    
    # Function call
    selected_activities = activitySelector(s, f)
    
    # Print outcome
    for i in selected_activities:
        print(f"Activity {i + 1} ({s[i]},{f[i]})")
        

       
'''
def activitySelector(s, f):
    n = len(s)
    
    # Sort activities based on finsih time
    activity = list(zip(s, f))
    activity.sort(key=lambda x: x[1])
    
    
    # Initialize selected activity array
    A = [0]
    
    for i in range(1, n):
        
        # Select activity that has start time greater or equal to finish time of previous activity
        if activity[i][0] >= activity[A[-1]][1]:
            A.append(i)
            
    # Print outcome
    for i in A:
        print(f"Activity {i + 1} ({activity[i][0]}, {activity[i][1]})")
    
    
            
        
# Driver code

if __name__ == '__main__':
    
    s = [1, 3, 8, 5, 0, 5]
    f = [2, 4, 9, 7, 6, 9]
    
    # Function call
    activitySelector(s, f)
'''        
