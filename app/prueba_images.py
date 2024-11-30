import random
import pandas as pd

def add_random_image_column_to_file(file_name):
    # List of possible image names
    image_names = ["milei.jpeg", "person1.png", "person2.png", "person3.png", "person4.png", "biden.jpeg", "trump.jpeg"]
    
    # Load the dataset from the CSV file
    dataset = pd.read_csv(file_name)
    
    # Add a new column "Image" with random selection from image_names
    dataset['Image'] = [random.choice(image_names) for _ in range(len(dataset))]
    
    # Save the updated dataset back to the same file
    dataset.to_csv(file_name, index=False)

# Example usage
file_name = "generated_database.csv"
add_random_image_column_to_file(file_name)
print(f"The file '{file_name}' has been updated with a random 'Image' column.")


