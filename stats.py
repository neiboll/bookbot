def get_count_words(text):
    words = text.split()
    return len(words)

def count_each_char(text):
    each_char = dict()
    lowercase = text.lower()
     
    for char in lowercase:
        if char.isalpha():
            if char in each_char:
                each_char[char] = each_char[char] + 1
            else:
                each_char[char] = 1
    return each_char

def sort_list(text):
    letter_sort = count_each_char(text)
    sorted_dict = dict(sorted(letter_sort.items(), key=lambda item: item[1], reverse=True)) 
    return sorted_dict


