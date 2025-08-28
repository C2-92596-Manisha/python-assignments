# Function to check if two lists have common elements
def overlapping(list1, list2):
    for item in list1:          
        if item in list2:      
            return True       
    return False              

print(overlapping([11, 12, 13], [14, 15, 12]))  
print(overlapping(['a', 'c'], ['n', 'p'])) 
