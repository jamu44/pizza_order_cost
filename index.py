# Purpose:Calculate the total cost of a pizza order (size+toppings+delivery).
#
# ------------ Psuedo Code ------------
# 1. ask for the user input: size
# 2. base cost (small = $8 or large = $12) if
# 3. toppings $1
# 4. delivery fee (if)
# 5. total = base_cost + toppings + delivery_fee
# 6. print the receipt/output
#

# ----------- Prices -----------
#
SMALL_PRICE = 8
LARGE_PRICE = 12
TOPPING_PRICE = 1
BASE_DELVERY_FEE = 2
BASE_DELVERY_MILES = 5
EXTRA_MILE_FEE = 1

# ------ input --------
size = input("Kindly indicate among `small` or `large`: ").strip().lower()
topping = int(input("How many number of topping?: "))
radius_in_miles = int(input("How far off do you live in miles?: "))
# ------- BASE COST -------
#
if size == "small":
    base_cost = SMALL_PRICE
elif size == "large":
    base_cost = LARGE_PRICE
else:
    print("chose among the two in lower case")
    raise SystemExit


# ------------ toppings -------------
#
toppings_cost = topping * TOPPING_PRICE


# ------------- miles --------------
#
if radius_in_miles == 0:
    delivery_fee = 0
elif radius_in_miles <= BASE_DELVERY_MILES:
    delivery_fee = BASE_DELVERY_FEE
else:
    extra_miles = radius_in_miles - BASE_DELVERY_MILES
    delivery_fee = BASE_DELVERY_MILES + extra_miles * EXTRA_MILE_FEE


# -----------TOTAL --------------
#
total_cost = base_cost + toppings_cost + delivery_fee


print(f"the final cost if ${total_cost}")
