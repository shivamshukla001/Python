# format specifiers = {value:flags} format specifiers allow you to format values in a string by
# specifying how the value should be presented. The flags can include alignment, width, precision,  
# and type of formatting (e.g., integer, float, string).
# Example usage:

price1 = 4775885.9870998
price2 = 1.2556
price3 = 1234.564564

print(f"the price is {price1:+,.2f}")
print(f"the price is {price2:+.3f}")