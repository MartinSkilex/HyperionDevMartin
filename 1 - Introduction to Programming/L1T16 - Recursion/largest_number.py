def largest_number(num_list):
     #Base case:If there is only one element in the list, it is the largest number.
     if len(num_list) == 1:
        return num_list[0]
     # Recursive case: If the list has more than one element, find the largest number recursively.
     else:

        # Get the first element of the list.
        first_num = num_list[0]

        # Recursively find the largest number in the rest of the list (excluding the first element).
        largest = largest_number(num_list[1:])

        # Compare the first element with the largest number in the rest of the list.
        if first_num > largest:
            return first_num
        else:
            return largest

# Test the 'largest_number' function with a sample list [1, 8, 5, 10].
# The function should return the largest number, which is 10.    
print(largest_number([1, 8, 5, 10]))

