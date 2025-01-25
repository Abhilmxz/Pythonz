class Customer:
    def __init__(self, customer_id, quantity, price_per_item):
        self.customer_id = customer_id
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.discount = 0  # Base discount for general customer is 0%

    def generate_bill(self):
        # Calculate the total amount before discount
        total_amount = self.quantity * self.price_per_item
        # Apply the discount
        discount_amount = total_amount * (self.discount / 100)
        final_amount = total_amount - discount_amount
        return final_amount

class SilverCustomer(Customer):
    def __init__(self, customer_id, quantity, price_per_item):
        super().__init__(customer_id, quantity, price_per_item)
        self.discount = 10  # Silver customers get a 10% discount

class GoldCustomer(Customer):
    def __init__(self, customer_id, quantity, price_per_item):
        super().__init__(customer_id, quantity, price_per_item)
        self.discount = 20  # Gold customers get a 20% discount

def get_customer_type():
    while True:
        print("\nSelect your customer type:")
        print("1. Silver Customer (10% Discount)")
        print("2. Gold Customer (20% Discount)")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            return "Silver"
        elif choice == '2':
            return "Gold"
        elif choice == '3':
            return None
        else:
            print("Invalid choice, please choose 1, 2, or 3.")

def main():
    print("Welcome to the Billing System")

    while True:
        # Get customer type
        customer_type = get_customer_type()
        if customer_type is None:
            print("Exiting the program. Goodbye!")
            break

        # Get customer details
        customer_id = input("Enter customer ID: ")
        quantity = int(input("Enter quantity of items: "))
        price_per_item = float(input("Enter price per item: "))

        # Create the correct customer object based on the type
        if customer_type == "Silver":
            customer = SilverCustomer(customer_id, quantity, price_per_item)
        elif customer_type == "Gold":
            customer = GoldCustomer(customer_id, quantity, price_per_item)

        # Generate and display the bill
        final_amount = customer.generate_bill()
        print(f"\nBill for Customer ID {customer.customer_id} ({customer_type} Customer):")
        print(f"Quantity: {customer.quantity}")
        print(f"Price per item: ₹{customer.price_per_item:.2f}")
        print(f"Discount applied: {customer.discount}%")
        print(f"Total amount after discount: ₹{final_amount:.2f}\n")

if __name__ == "__main__":
    main()
