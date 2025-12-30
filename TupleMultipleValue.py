def analyze_list(lst):
    return max(lst), min(lst), sum(lst)

num_lst = list(map(int, input("Enter the elements: ").split()))

maxi, mini, total = analyze_list(num_lst)
print("Maximum in the tuple is: ", maxi)
print("Minimum in the tuple is: ", mini)
print("Sum of all elements in the tuple is: ", total)