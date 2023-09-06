# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # Changed 'dictionary[k]' to 'dictionary[key]'


# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!",  # Enclosed 'd'oh!' within double quotes
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases,['lisa','bart','homer']) #reduced number of inputs to the function by enclosing keys in square brackets [] 

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''