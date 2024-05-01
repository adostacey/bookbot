def read_text(path_to_text:str):
    full_text = None

    with open("./books/frankenstein.txt") as f:
        text = f.read()
        full_text = text

    return full_text

def count_words(text:str):
    words = text.split()
    count = len(words)
    
    return count

def count_characters(text:str):
    chars = text.lower()
    char_count = {}
    
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(dict:dict):
    return list(dict.values())[0]


def report_characters(char_count:dict):

    char_list = [{c:char_count[c]} for c in char_count if c.isalpha()]
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list


def main():
    book = "./books/frankenstein.txt"
    text = read_text(book)
    word_count = count_words(text)
    char_count = count_characters(text)
    char_report = report_characters(char_count)

    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document6")
    print("\n")
    
    for char in char_report:
        for (k, v) in char.items():
            print(f"The '{k}' character was found {v} times")

    print("--- End Report ---")

main()
