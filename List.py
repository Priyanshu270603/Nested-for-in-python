try:
    L1 = ["Apple", "Banana", "Cherry", "Date", "ElderBerry"]

    index = int(input("Please enter your choice: "))
    print(L1[index])

except IndexError:
    print("Index you entered is out of range")

finally:
    print("Operation Completed")