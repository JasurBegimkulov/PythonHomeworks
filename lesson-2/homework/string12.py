words = input("write words:").split()
separator = input("Write a seperator (e.g., - or ,): ")
result = separator.join(words)

print("Single string:", result)