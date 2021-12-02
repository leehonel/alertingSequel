from name_function import get_formatted_name

print("Enter 'q' at any point to quit.")
while True:
    first = input("\nPlease enter the first name: ")
    if first == 'q':
        break
    last = input("\nPlease enter the last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: "+formatted_name+".")
    