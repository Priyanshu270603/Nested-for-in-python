def find_max(L1):
    max = L1[0]

    for num in L1:
        if num > max:
            max = num

    return max

n = int(input("Enter the elements of the list: "))

L1 = []

for i in range(n):

    value = int(input(f"Enter elements {i + 1}: "))

    L1.append(value)

print("Max value is:", find_max(L1))