import random
import time


package_status = { # a dictionary with simulated tracking numbers as the key and a string indicating the status as the value
    12345: "In Transit",
    67890: "Out for Delivery",
    11111: "Delivered"
}

def get_tracking_number():  # prompt user for tracking number and verify user input
    while True:
        tracking_number = input("To track your package delivery status here, please enter your order tracking number: \n")

        try:
            # Check if the input is a valid number
            if not tracking_number.isdigit():  # checks that the user inputted a valid tracking number
                raise ValueError("Invalid tracking number, please try again. \n")
            return tracking_number
        except ValueError as e:
            print(f"{e}") # user is prompted again

def check_status(tracking_number):
    print("Let me check the status of your package...\n")
    time.sleep(3)  # simulate the process of checking the status
    status = package_status.get(int(tracking_number), None)
    
    if status is None:
        raise KeyError("Tracking number not found in the system.\n")
    return status

def get_delivery_duration(tracking_number): # generate fake delivery duration to simulate a real order in transit
    random_days = random.randint(1, 14)
    return random_days

def confirm_delivery(): # ensures that users received their package; otherwise, connects them to a representative (not really)
    while True:
        try:
            lost_check = input("Did you receive your package? (Yes/No): \n").strip().lower()
            if lost_check == "no":
                print("Sorry to hear that! We will connect you with a representative to help you file a report. Please check your email.\n") 
                break
            elif lost_check == "yes":
                print("Great! I'm happy to hear that your package has been delivered.\n")
                break
            else:
                raise ValueError("Invalid response. Please answer with 'Yes' or 'No'.\n")
        except ValueError as e:
            print(f"{e}")


def chatbot():
    try:
        tracking_number = get_tracking_number() 
        status = check_status(tracking_number)

        if status == "In Transit":
            remaining_duration = get_delivery_duration(tracking_number)
            print("Your package is still on the way! Expect it to arrive in " + str(remaining_duration) + " days. \n")
        elif status == "Out for Delivery":
            print("Your package is out for delivery! Expect it to arrive sometime today.\n") 
        elif status == "Delivered":
            print("Your package has been marked as delivered.\n")
            confirm_delivery()
        else:
            print("a")

    except KeyError as e:
        print(f"{e}")
        print("Please try again with a valid tracking number.\n")
        chatbot()  # Restart the process to allow the user to input a valid number


def main():
    chatbot()

if __name__ == "__main__":
    main()