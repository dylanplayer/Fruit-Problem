# Import random library
import random as Random

# Create function that takes in a parameter for the fruits array and the number of fruits requested
def pick_fruits(fruits, num_fruits=3):
    # Set the value of the fruits array to the value returned by the get avalible fruits functtion
    fruits = get_avalible_fruits(fruits)
    # Create an empty array
    picked_fruits = []
    # Check if there are more fruits in the array than the requested amount
    if len(fruits) > num_fruits:
        # If so:
        # Create a while loop that runs while the length of the picked_fruits array is less than the number of fruits requested
        while len(picked_fruits) < num_fruits:
            # Chose a random fruit from the fruit array
            fruit_choice = Random.choice(fruits)
            # Remove the chosen fruit from the array
            fruits.remove(fruit_choice)
            # Append the picked_fruits array with the new chosen fruit
            picked_fruits.append(fruit_choice)
        # Return the picked fruits array
        return picked_fruits
    else:
        return fruits
    
# Create function that takes in an array of fruits called get_avalible_fruits
def get_avalible_fruits(fruits):
    # Create an empty array to store the avalible fruits
    avalible_fruits = []
    # Create a for loop that iterates through all of the fruits
    for fruit in fruits:
        # If the fruit does not start with a vowel:
        if fruit[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
            # Append the avalible fruits array with the fruit
            avalible_fruits.append(fruit)
    # Return the avalible fruits array
    return avalible_fruits

fruits = ["Banana", "Apple", "Mango", "Orange", "Pineapple", "Honeydew"]
print(pick_fruits(fruits, 3))