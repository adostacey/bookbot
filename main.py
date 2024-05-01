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


def main():
    book = "./books/frankenstein.txt"
    text = read_text(book)
    word_count = count_words(text)

    print(text)
    print(word_count)


main()
