""" import numpy as np

def rgb_to_grayscale_average(rgb_image):
    # Convert the RGB image to grayscale using the average method
    return np.mean(rgb_image, axis=2)

def apply_threshold(grayscale_image, threshold=128):
    # Apply binary thresholding
    binary_image = np.where(grayscale_image > threshold, 255, 0)
    return binary_image

def print_menu():
    print("1. Display RGB Image")
    print("2. Convert RGB Image to Grayscale (Average Method)")
    print("3. Apply Threshold to Grayscale Image")
    print("4. Exit")

def get_valid_rgb_value(channel_name):
    # Function to get valid input for an RGB channel
    while True:
        try:
            value = int(input(f"Enter value for {channel_name} (0-255): "))
            if 0 <= value <= 255:
                return value
            else:
                print("Error: Please enter a value between 0 and 255.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def main():
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Accept user input for a 3D RGB image
    rgb_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    print("\nEnter RGB values (0-255) for each pixel:")
    for i in range(height):
        for j in range(width):
            r = get_valid_rgb_value(f"Pixel ({i}, {j}) - Red")
            g = get_valid_rgb_value(f"Pixel ({i}, {j}) - Green")
            b = get_valid_rgb_value(f"Pixel ({i}, {j}) - Blue")
            rgb_image[i, j] = [r, g, b]
    
    grayscale_image = None
    binary_image = None

    while True:
        print_menu()
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            # Display the RGB image
            print("\nRGB Image:")
            print(rgb_image)
        
        elif choice == 2:
            # Convert to grayscale using average method
            grayscale_image = rgb_to_grayscale_average(rgb_image)
            print("\nGrayscale image (Average method):")
            print(grayscale_image)
        
        elif choice == 3:
            if grayscale_image is None:
                print("Please convert the image to grayscale first!")
            else:
                threshold = int(input("Enter the threshold (0-255): "))
                binary_image = apply_threshold(grayscale_image, threshold)
                print("\nBinary image after applying threshold:")
                print(binary_image)
        
        elif choice == 4:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

main() """


import numpy as np
import matplotlib.pyplot as plt

def rgb_to_grayscale_average(rgb_image):
    # Convert the RGB image to grayscale using the average method
    return np.mean(rgb_image, axis=2)

def apply_threshold(grayscale_image, threshold=128):
    # Apply binary thresholding
    binary_image = np.where(grayscale_image > threshold, 255, 0)
    return binary_image

def print_menu():
    print("1. Display RGB Image")
    print("2. Convert RGB Image to Grayscale (Average Method)")
    print("3. Apply Threshold to Grayscale Image")
    print("4. Exit")

def get_valid_rgb_value(channel_name):
    # Function to get valid input for an RGB channel
    while True:
        try:
            value = int(input(f"Enter value for {channel_name} (0-255): "))
            if 0 <= value <= 255:
                return value
            else:
                print("Error: Please enter a value between 0 and 255.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def display_image(image, title):
    # Function to display an image
    plt.imshow(image, cmap='gray' if len(image.shape) == 2 else None)
    plt.title(title)
    plt.axis('off')  # Hide axis
    plt.show()

def main():
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Accept user input for a 3D RGB image
    rgb_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    print("\nEnter RGB values (0-255) for each pixel:")
    for i in range(height):
        for j in range(width):
            r = get_valid_rgb_value(f"Pixel ({i}, {j}) - Red")
            g = get_valid_rgb_value(f"Pixel ({i}, {j}) - Green")
            b = get_valid_rgb_value(f"Pixel ({i}, {j}) - Blue")
            rgb_image[i, j] = [r, g, b]
    
    grayscale_image = None
    binary_image = None

    while True:
        print_menu()
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            # Display the RGB image
            display_image(rgb_image, "RGB Image")
        
        elif choice == 2:
            # Convert to grayscale using average method
            grayscale_image = rgb_to_grayscale_average(rgb_image).astype(np.uint8)
            display_image(grayscale_image, "Grayscale Image (Average Method)")
        
        elif choice == 3:
            if grayscale_image is None:
                print("Please convert the image to grayscale first!")
            else:
                threshold = int(input("Enter the threshold (0-255): "))
                binary_image = apply_threshold(grayscale_image, threshold).astype(np.uint8)
                display_image(binary_image, "Binary Image after Applying Threshold")
        
        elif choice == 4:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

main()
