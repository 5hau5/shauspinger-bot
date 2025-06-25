import pytesseract
import pyautogui
from PIL import Image
import time

# Path to Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Counter to keep track of the accumulated number for "Book of Orgain"
book_of_orgain_counter = 0

# Function to capture the main part of the screen and perform OCR logic
def monitor_and_act():
    while True:
        # Capture the region for the first task (numbers separated by "/")
        screenshot = pyautogui.screenshot(region=(100, 200, 300, 150))  # Adjust to your region
        
        # Convert the image to grayscale for better OCR accuracy
        grayscale_image = screenshot.convert('L')
        
        # Perform OCR to extract the text
        text = pytesseract.image_to_string(grayscale_image)
        
        try:
            # Split the text by '/' to get the left and right numbers
            left_num, right_num = text.strip().split('/')
            
            # Convert the extracted numbers to integers
            left_num = int(left_num.strip())
            right_num = int(right_num.strip())
            
            # Check if left number is 10% or less than the right number
            if left_num <= 0.1 * right_num:
                print("Left number is 10% or less than the right number, performing action 1")
                perform_button_combination_1()
            else:
                print("Left number is more than 10% of the right number, performing action 2")
                perform_button_combination_2()
        except Exception as e:
            print(f"Error occurred: {e}. Retrying...")
        
        # Call the function to monitor "Book of Orgain"
        monitor_book_of_orgain()

        # Pause before next check (adjust the delay as needed)
        time.sleep(5)

# Function for specific button combination when condition is met (left <= 10%)
def perform_button_combination_1():
    pyautogui.hotkey('ctrl', 'shift', 'a')
    time.sleep(1)

# Function for another button combination when condition is not met (left > 10%)
def perform_button_combination_2():
    pyautogui.hotkey('alt', 'x')
    time.sleep(1)

# Function for button combination when the "Book of Orgain" counter reaches 90
def perform_button_combination_3():
    pyautogui.hotkey('ctrl', 'alt', 'b')
    time.sleep(1)

# Function to monitor "Book of Orgain" and accumulate the associated number
def monitor_book_of_orgain():
    global book_of_orgain_counter

    # Capture the region where "Book of Orgain" appears
    screenshot = pyautogui.screenshot(region=(400, 300, 300, 150))  # Adjust to the region for "Book of Orgain"
    
    # Convert to grayscale for better OCR accuracy
    grayscale_image = screenshot.convert('L')

    # Perform OCR to extract the text
    text = pytesseract.image_to_string(grayscale_image)

    try:
        # Look for the phrase "Book of Orgain" and the following number
        if "Book of Orgain" in text:
            print(f"Found 'Book of Orgain' in text: {text}")
            # Extract the number after "Book of Orgain" (assuming it's right after the phrase)
            # Example: "Book of Orgain 30" -> number = 30
            number_str = text.split("Book of Orgain")[-1].strip()
            number = int(number_str)
            
            # Add this number to the counter
            book_of_orgain_counter += number
            print(f"Added {number}. New 'Book of Orgain' counter: {book_of_orgain_counter}")
            
            # Check if the counter has reached or exceeded 90
            if book_of_orgain_counter >= 90:
                print("Counter reached 90, performing action 3")
                perform_button_combination_3()
                book_of_orgain_counter = 0  # Reset the counter after performing the action
        else:
            print("'Book of Orgain' not found")
    except Exception as e:
        print(f"Error occurred in 'Book of Orgain' monitoring: {e}")

# Run the bot
monitor_and_act()