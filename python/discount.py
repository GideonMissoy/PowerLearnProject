def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price != original_price:
    print(f"Final Price after {discount_percentage}% discount: {final_price:.2f}")
else:
    print(f"Original Price: {original_price:.2f}")

