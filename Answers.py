def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage (as a number between 0 and 1).

  Returns:
    The final price after applying the discount.
  """

  if discount_percent >= 0.2:
    final_price = price - (price * discount_percent)
  else:
    final_price = price

  return final_price


# Example usage:
price = 100
discount_percent = 0.2
final_price = calculate_discount(price, discount_percent)
print(final_price)  # Output: 80.0




#Question
def calculate_discount(original_price, discount_percentage):
  """Calculates the final price of an item after applying a discount.

  Args:
    original_price: The original price of the item in dollars.
    discount_percentage: The discount percentage as a decimal.

  Returns:
    The final price of the item after applying the discount in dollars.
  """

  if discount_percentage > 0:
    discount_amount = original_price * discount_percentage
    final_price = original_price - discount_amount
  else:
    final_price = original_price

  return final_price


def main():
  """Gets the original price and discount percentage from the user and prints the final price."""

  original_price = float(input("Enter the original price of the item in dollars: "))
  discount_percentage = float(input("Enter the discount percentage as a decimal (0 for no discount): "))

  final_price = calculate_discount(original_price, discount_percentage)
  print(f"The final price of the item is ${final_price:.2f}")


if __name__ == "__main__":
  main()







  def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount = float(input("Enter the discount percentage: "))

    # Use the calculate_discount function
    final_price = calculate_discount(original_price, discount)

    # Display the result
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"The final price after a {discount}% discount is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
