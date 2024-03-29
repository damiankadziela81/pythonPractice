# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 3000.12345
price2 = -987.23
price3 = 12.3

print(f"Price 1 is {price1:,.2f}")
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")
