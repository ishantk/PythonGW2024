product_prices = [1200, 500, 7650, 800, 3500, 1700]
salaries = [35000, 61500, 1800, 13500, 21700]
team_points = [12, 8, 4, 10, 2]

# Goal : find maximum out of all three

def find_max(data):
    max = data[0]
    for idx in range(1, len(data)):
        if data[idx] > max:
            max = data[idx]
    
    print("Max is:", max)

find_max(product_prices)
find_max(salaries)
find_max(team_points)
