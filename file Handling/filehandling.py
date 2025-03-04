'''
File handling in Python refers to the process of working with files on your computer. This includes creating, reading, updating, and deleting files. Python provides built-in functions and methods to perform these operations.

1. Opening a File

    Common Modes:
"r": Read mode (default). Opens the file for reading.

"w": Write mode. Opens the file for writing (creates a new file or truncates an existing file).

"a": Append mode. Opens the file for appending data (does not truncate the file).

"b": Binary mode. Used for binary files (e.g., images).

"+": Update mode. Opens the file for both reading and writing.


2. Reading from a File
You can read the contents of a file using methods like read(), readline(), or readlines().

3. Writing to a File
You can write to a file using the write() or writelines() methods

4. Appending to a File
If you want to add content to an existing file without overwriting it, use the append mode ("a").

5. Closing a File
Always close a file after you’re done with it using the close() method. This frees up system resources.

6. Using with Statement (Recommended)
The with statement is the best way to handle files because it automatically closes the file, even if an exception occurs.

7. Handling Binary Files
To work with binary files (e.g., images), use the "b" mode.

'''

#1. Opening a File

# # Syntax: open(file_name, mode)
# file = open("example.txt", "r")  # Opens the file in read mode

# #2. Reading from a File

# # Example: Reading a file
# file = open("example.txt", "r")  # Open the file in read mode

# # Read the entire file content
# content = file.read()
# print("File Content:\n", content)

# # Read one line at a time
# file.seek(0)  # Reset the file pointer to the beginning
# line = file.readline()
# print("First Line:", line)

# # Read all lines into a list
# file.seek(0)  # Reset the file pointer to the beginning
# lines = file.readlines()
# print("All Lines:", lines)

# file.close()  # Always close the file after use

# 3. Writing to a File

# # Example: Writing to a file
# file = open("example.txt", "w")  # Open the file in write mode

# # Write a string to the file
# file.write("Hello, World!\n")
# file.write("This is a new line.\n")

# # Write a list of strings to the file
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# file.writelines(lines)

# file.close()  # Close the file


# # 4. Appending to a File

# # Example: Appending to a file
# file = open("example.txt", "a")  # Open the file in append mode

# file.write("This line is appended.\n")

# file.close()  # Close the file

# # 5. Closing a File

# file = open("example.txt", "r")
# # Perform file operations
# file.close()  # Close the file

# # 6. Using with Statement (Recommended)

# # Example: Using 'with' statement
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)
# # No need to explicitly close the file; it's done automatically


# # 7. Handling Binary Files

# # Example: Reading a binary file
# with open("image.png", "rb") as file:
#     binary_data = file.read()
#     # Process binary data here

# # Reading and Writing a File

# # Writing to a file
# with open("example.txt", "w") as file:
#     file.write("Hello, Python!\n")
#     file.write("File handling is easy.\n")

# # Reading from a file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print("File Content:\n", content)