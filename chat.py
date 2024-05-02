import time

def greet():
    return "🍕 Welcome to Pizza Palace! How can I assist you today?"

def show_menu():
    menu = "Our menu:\n1. Margherita Pizza\n2. Pepperoni Pizza\n3. Vegetarian Pizza\n4. Hawaiian Pizza"
    return menu

def take_order():
    return "What would you like to order? Please specify by number."

def confirm_order(order):
    return f"You ordered {order}. Is that correct?"

def get_address():
    return "Great! Could you please provide your delivery address?"

def confirm_address(address):
    return f"Thank you! We'll deliver your order to {address}. Enjoy your meal!"

def add_special_request():
    return "Do you have any special instructions for your order?"

def track_order(order_number):
    return f"Your order {order_number} is out for delivery. It should arrive shortly."



def goodbye():
    return "Thank you for choosing Pizza Palace! Have a great day! 🍕"

def chat():
    print(greet())
    time.sleep(1)
    
    print(show_menu())
    time.sleep(1)
    
    order = input(take_order())
    time.sleep(1)
    
    confirmation = input(confirm_order(order))
    time.sleep(1)
    
    if confirmation.lower() in ['yes', 'y']:
        address = input(get_address())
        time.sleep(1)
        
        print(confirm_address(address))
        time.sleep(1)
        
        add_special_request = input(add_special_request())
        time.sleep(1)
        
        order_number = "#1234"  # Mock order number
        print(f"Your order has been placed. Order number: {order_number}")
        print(track_order(order_number))
        time.sleep(1)
        
      
        
        print(goodbye())
    else:
        print("I'm sorry, could you please repeat your order?")
        chat()  # Restart the conversation

# Start the conversation
chat()
