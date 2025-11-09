def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars(book_text):
    
    char_dict = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def to_list(char_dict):
    char_list = []
    for ch, n in char_dict.items():
        char_list.append({"char": ch, "num": n})
    return sorted(char_list, key=lambda x: x["num"], reverse=True)

