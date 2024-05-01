def read_text(path_to_text:str):
    full_text = None

    with open("./books/frankenstein.txt") as f:
        text = f.read()
        full_text = text

    return full_text


def main():
    book = "./books/frankenstein.txt"
    
    print(read_text(book))


main()
