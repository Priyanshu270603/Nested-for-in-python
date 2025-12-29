def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])

tuple_lst = int(input("Enter the number of tuples: "))
data = []

for i in range(tuple_lst):
    ele1 = input("Enter the first element: ")
    ele2 = int(input("Enter the second element: "))
    data.append((ele1, ele2))

srt_lst = sort_by_second_element(data)

print("Sorted list: ", srt_lst)