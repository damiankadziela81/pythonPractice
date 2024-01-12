# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

card_number = input("Enter credit card number: ")
# 1
card_number = card_number.replace(" ","").replace("-","")
# reverse the numbers
card_number = card_number[::-1]
# 3
even_sum = 0
for x in range(1,16,2):
    # double every digit
    doubled_even_digit = int(card_number[x]) * 2
    print(f"current value: {doubled_even_digit}")
    # if digit doubled has 2 digits, add them together
    if doubled_even_digit > 9:
        doubled_even_digit = int(str(doubled_even_digit)[1]) + int(str(doubled_even_digit)[0])
    # add the calculated value to the sum
    even_sum += doubled_even_digit
print(even_sum)
# 2
odd_sum = 0
for x in range(0,15,2):
    odd_sum += int(card_number[x])
print(odd_sum)

total_sum = even_sum + odd_sum
print(f"Total sum / 10 reminder: {total_sum % 10}")
if total_sum % 10 == 0:
    print("Card number is valid.")
else:
    print("Card number is invalid")

