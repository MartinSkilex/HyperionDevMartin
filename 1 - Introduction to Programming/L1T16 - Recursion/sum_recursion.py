def adding_up_to(num_list,index):
    # Base case: If the index is 0, return the value at the first position of the num_list.
    # This is the stopping condition for the recursion.
    if index == 0:
        return num_list[0]
    # Recursive case: If the index is not 0, add the value at the current index to the sum of
    # values from previous indices.
    else:
        return  num_list[index] + adding_up_to(num_list,index-1)
   
# Test the 'adding_up_to' function with a sample list [1, 4, 5, 3, 12, 16] and index 4.
# The function should return the sum of values up to index 4, which is 1 + 4 + 5 + 3 + 12 = 25.
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))