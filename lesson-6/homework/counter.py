def count_word_frequency():
    try:
        with open("sample.txt", "r") as file:
            content = file.read().lower()  

        for char in ".,!?;:":
            content = content.replace(char, "")
        words = content.split()

        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1