base_fair = 50
distance_fair = 10

trips = list(map(int,input("Enter the Distance in Kilometers for each trip separated by spaces: ").split()))

total_fair = sum(base_fair + distance * distance_fair for distance in trips)

print(f"Total Fair: {total_fair}$")