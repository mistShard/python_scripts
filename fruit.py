def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        # Reverse and print the list named fruit_list.
        fruit_list.reverse()
        print(f"Reversed: {fruit_list}")

        # Append Orange to the end of the list
        # print the list.
        fruit_list.append("orange")
        print(fruit_list)

        # Find apple in the list and put  cherry
        # before it.
        i = fruit_list.index("apple")
        fruit_list.insert(i, "cherry")
        print(fruit_list)

        # Delete banana from list and print list
        fruit_list.remove("banana")
        print(fruit_list)

        # Pop and print last item from fruit_list
        item = fruit_list.pop()
        print(item)

        # Sort and print fruit_list
        sorted_list = sorted(fruit_list)
        print(sorted_list)

        # Clear and print list
        fruit_list.clear()
        print(fruit_list)
        
    except (IndexError, ValueError) as err:
        print(type(err).__name__, err, sep=": ")

if __name__ == "__main__":
    main()