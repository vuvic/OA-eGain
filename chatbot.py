import random
import time

package_status = { # a dictionary with simulated tracking numbers as the key and a string indicating the status as the value
    12345: "In Transit",
    67890: "Out for Delivery",
    11111: "Delivered"
}

def get_tracking_number(): # prompt user for tracking number and verify user input
    tracking_number = input("To track your package delivery status here, please enter your order tracking number: \n") 

    while (not tracking_number.isdigit()): # checks that the user inputted a valid tracking number (assuming that tracking numbers have no set length and contain only numerals)
        tracking_number = input("Invalid tracking number, please try again: \n")
    return tracking_number

def check_status(tracking_number): # retrieves delivery status for the given tracking number
    try:
        print("Let me check the status of your package...")

        time.sleep(3) # Simulate the process of checking the status
        status = package_status.get(int(tracking_number), "Not Found")
        if status == "Not Found":
            raise ValueError()
        return status
    except ValueError as e:
        return None

def get_delivery_duration(tracking_number): # generate fake delivery duration to simulate a real order in transit
    random_days = random.randint(1, 14)
    return random_days

def confirm_delivery(): # confirm that the customer received the package and connect them to a representative otherwise
    lost_check = input("Did you receive your package? (Yes/No): \n").strip().lower()
    if lost_check == "no":
        print("Sorry to hear that! We will connect you with a representative to help you file a report. Please check your email.\n")
    elif lost_check == "yes":
        print("Great! I'm happy to hear that your package has been delivered.\n")
    else: 
        confirm_delivery()

def chatbot():
    tracking_number = get_tracking_number() 
    status = check_status(tracking_number) 

    if status == "In Transit":
        remaining_duration = get_delivery_duration(tracking_number)
        print("Your package is still on the way! Expect it to arrive in " + str(remaining_duration) + " days. \n") # Indicates that the package will arrive in a (randomly generated) number of days
    elif status == "Out for Delivery":
        print("Your package is out for delivery! Expect it to arrive sometime today.\n") 
    elif status == "Delivered":
        print("Your package has been marked as delivered.\n")
        confirm_delivery()
    else:
        print("Tracking number not found in the system.\n")
        chatbot()

def main():
    chatbot()

if __name__ == "__main__":
    main()