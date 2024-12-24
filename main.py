def words_counter(text):
    words_list = text.split()
    words_in_text = len(words_list)
    return words_in_text

def character_counter(text):
    text_lower = text.lower()
    words_list = text_lower.split()
    characters_total = {}
    is_a_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for word in words_list:
        characters = list(word)
        for character in characters:
            if character in characters_total and character in is_a_letter:
                characters_total[character] += 1
            elif character not in characters_total and character in is_a_letter:
                characters_total[character] = 0
            else:
                pass
    return characters_total

def main():
    with open("books/frankenstein.txt") as f:   
        file_contents = f.read()
        words_counted = words_counter(file_contents)
        characters_counted = character_counter(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words_counted}  words found in the document")
        print("\n")
        for i in characters_counted:
            print(f"The {i} character was found {characters_counted[i]} times")
        print("--- End report ---")

main()