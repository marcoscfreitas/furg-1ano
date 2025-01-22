# Python Tutorial: Manipulation of Strings, Lists, and Files

# -----------------------------
# String Manipulations
# -----------------------------

print("\n--- String Manipulations ---\n")

# 1. Changing Case
text = "Hello World"
print("Original Text:", text)
print("Upper Case:", text.upper())  # Converts all letters to uppercase
print("Lower Case:", text.lower())  # Converts all letters to lowercase
print("Title Case:", text.title())  # Converts the first character of each word to uppercase

# 2. Stripping and Replacing
messy_text = "   Python is great!   "
print("\nMessy Text:", messy_text)
print("Stripped Text:", messy_text.strip())  # Removes leading and trailing spaces
print("Replaced Text:", messy_text.replace("great", "awesome"))  # Replaces words

# 3. Splitting and Joining
sentence = "This is a sample sentence."
words = sentence.split()  # Splits a string into a list of words
print("\nSplit Sentence into Words:", words)
joined_sentence = "-".join(words)  # Joins a list of words into a string with "-"
print("Joined Words:", joined_sentence)

# 4. Finding and Checking
print("\nDoes 'Python' exist in the text?", "Python" in messy_text)
print("Starts with 'Hello'?", text.startswith("Hello"))  # Checks if string starts with "Hello"
print("Ends with 'World'?", text.endswith("World"))  # Checks if string ends with "World"


# -----------------------------
# List Manipulations
# -----------------------------

print("\n--- List Manipulations ---\n")

# 1. Creating and Accessing
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)
print("First Item:", fruits[0])  # Accessing the first item
print("Last Item:", fruits[-1])  # Accessing the last item

# 2. Modifying
fruits.append("date")  # Adding an item to the end
print("\nAfter Append:", fruits)
fruits.insert(1, "blueberry")  # Inserting an item at index 1
print("After Insert:", fruits)

# 3. Removing
fruits.remove("banana")  # Removes the first occurrence of "banana"
print("\nAfter Remove:", fruits)
popped_item = fruits.pop()  # Removes and returns the last item
print("After Pop:", fruits, ", Popped Item:", popped_item)

# 4. Sorting and Reversing
numbers = [4, 2, 9, 1, 5]
print("\nOriginal Numbers:", numbers)
numbers.sort()  # Sorts the list in ascending order
print("Sorted Numbers:", numbers)
numbers.reverse()  # Reverses the order of the list
print("Reversed Numbers:", numbers)


# -----------------------------
# Functions Within Brackets
# -----------------------------

print("\n--- Functions Within Brackets ---\n")

# 1. Indexing
my_list = [10, 20, 30, 40]
print("Original List:", my_list)
print("Element at index 2:", my_list[2])

# 2. Negative Indexing
print("Last Element:", my_list[-1])  # Access the last element

# 3. Slicing
print("Slice from index 1 to 3:", my_list[1:3])
print("Slice with step 2:", my_list[::2])
print("Reversed List:", my_list[::-1])

# 4. Multidimensional Access
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
print("Element at row 2, column 3:", matrix[1][2])

# 5. Dynamic Slicing
start, end = 1, 3
print("Dynamic Slice:", my_list[start:end])


# -----------------------------
# Working with Matrices
# -----------------------------

print("\n--- Working with Matrices ---\n")

# Creating a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:")
for row in matrix:
    print(row)

# Accessing elements
print("\nElement at row 2, column 3:", matrix[1][2])  # Indexing starts at 0

# Modifying elements
matrix[0][0] = 10  # Change the top-left element
print("\nModified Matrix:")
for row in matrix:
    print(row)

# Adding rows or columns
new_row = [10, 11, 12]
matrix.append(new_row)  # Add a new row
print("\nMatrix after adding a row:")
for row in matrix:
    print(row)

# Iterating through the matrix
print("\nElements of the matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Transposing a matrix
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("\nTransposed Matrix:")
for row in transpose:
    print(row)


# -----------------------------
# File Manipulations
# -----------------------------

print("\n--- File Manipulations ---\n")

# Writing to a file
file_name = "example.txt"
with open(file_name, "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("Python makes file handling easy!\n")
print(f"Written to {file_name}.")

# Reading from a file
with open(file_name, "r") as file:
    print("\nFile Contents:")
    for line in file:
        print(line.strip())  # Strips the newline character

# Appending to a file
with open(file_name, "a") as file:
    file.write("Appending a new line to the file.\n")
print(f"Appended new content to {file_name}.")

# Checking updated file contents
with open(file_name, "r") as file:
    print("\nUpdated File Contents:")
    print(file.read())
