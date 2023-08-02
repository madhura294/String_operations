#some basic operations on strings in Python.
#1. String concatenation.
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)  # Output: "Hello World"

#2. String Length.
string = "Python"
length = len(string)
print(length)  # Output: 6

#3. String Indexing.
string = "Python"
first_character = string[0]
last_character = string[-1]
print(first_character)  # Output: "P"
print(last_character)   # Output: "n"

#4. String Slicing.
string = "Python is fun"
sliced_string = string[7:9]
print(sliced_string)  # Output: "is"

#5. String Upper and Lower Case Conversion.
string = "Python is Fun"
uppercase_string = string.upper()
lowercase_string = string.lower()
print(uppercase_string)  # Output: "PYTHON IS FUN"
print(lowercase_string)  # Output: "python is fun"

#6. String Splitting.
string = "Python is fun"
words = string.split()
print(words)  # Output: ['Python', 'is', 'fun']

#7. String Stripping.
string = "    Hello    "
stripped_string = string.strip()
print(stripped_string)  # Output: "Hello"

#8. string = "Python is fun"
replaced_string = string.replace("fun", "awesome")
print(replaced_string)  # Output: "Python is awesome"

#9. String Formatting.
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: "My name is Alice and I am 30 years old."


