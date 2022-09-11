numbers = list(map(int, input().split(", ")))

group_of_10 = []
group_of_20 = []
group_of_30 = []
group_of_40 = []
group_of_50 = []

for number in numbers:
    if number <= 10:
        group_of_10.append(number)
    elif number <= 20 and number > 10:
        group_of_20.append(number)
    elif number <= 30 and number > 20:
        group_of_30.append(number)
    elif number <= 40 and number > 30:
        group_of_40.append(number)
    elif number <= 50 and number > 40:
        group_of_50.append(number)

print(f"Group of 10's: {group_of_10}")
print(f"Group of 20's: {group_of_20}")
print(f"Group of 30's: {group_of_30}")
print(f"Group of 40's: {group_of_40}")
print(f"Group of 50's: {group_of_50}")