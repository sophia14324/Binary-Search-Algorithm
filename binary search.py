def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1
    
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2 
        midpoint_value = sequence[midpoint]
        
        if midpoint_value == item: 
            return midpoint
        elif item < midpoint_value: 
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1 
    
    return None 
            
sequence = [2,3,4,5,6,7,8,9,10,11,12,14,15,16]

# returns the position of the number 12 --> ANS: 10
item = 12
 
print(binary_search(sequence, item))