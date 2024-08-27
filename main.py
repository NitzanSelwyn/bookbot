
def generate_report(char_array,total_words):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{total_words} words found in the document')
    for char in char_array:
        print(f"The '{char['name']}' character was found {char['num']} times")
    print('--- End report ---')    

def sort_on(dict):
    return dict["num"]

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = len(words)
        total_chars = {}
        chars_lst = []
        for word in words:
            w = word.lower()
            for c in w:
                if c in total_chars:
                    total_chars[c] = total_chars[c] + 1                
                else:
                    total_chars[c] = 1

        for char in total_chars:
            chars_lst.append({'name':char,'num':total_chars[char]})

        chars_lst.sort(reverse=True,key=sort_on)
        generate_report(chars_lst,total_words)        

main()    