def calculate_trip_cost(days, price_per_day, discount):
    total = days * price_per_day
    discount_amount = total * (discount / 100)
    return total - discount_amount
