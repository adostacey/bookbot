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

def main():
    book = "./books/frankenstein.txt"
    text = read_text(book)
    word_count = count_words(text)
    char_count = count_characters(text)
    
    print(text)
    print(word_count)
    print(char_count)

main()
