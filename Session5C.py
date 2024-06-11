product_prices = [1200, 500, 7650, 800, 3500, 1700]
salaries = [35000, 61500, 1800, 13500, 21700]
team_points = [12, 8, 4, 10, 2]

# Goal : find maximum out of these three

max = product_prices[0] # 1200
for idx in range(1, len(product_prices)): # 1, 2, 3, 4, 5
    if product_prices[idx] > max:
        max = product_prices[idx]

print("max is:", max)

max = salaries[0] # 35000
for idx in range(1, len(salaries)): # 1, 2, 3, 4, 5
    if salaries[idx] > max:
        max = salaries[idx]

print("max is:", max)

max = team_points[0] # 12
for idx in range(1, len(salaries)): # 1, 2, 3, 4, 5
    if team_points[idx] > max:
        max = team_points[idx]

print("max is:", max)