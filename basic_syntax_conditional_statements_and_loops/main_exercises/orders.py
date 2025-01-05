number_of_orders = int(input())

total_price = 0
for _ in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    needed_capsules = int(input())
    if capsule_price >= 0.01 and capsule_price <= 100:
        if days >= 1 and days <= 31:
            if needed_capsules >= 1 and needed_capsules <= 2000:
                price_per_coffee = capsule_price * needed_capsules * days
                total_price += price_per_coffee
                print(f"The price for the coffee is: ${price_per_coffee:.2f}")
    else:
        continue

print(f"Total: ${total_price:.2f}")