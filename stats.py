def get_word_count(book_string):
    return len(book_string.split())

def get_character_count(book_string):
    character_count = {}

    for word in book_string.split():
        for character in word:
            character = character.lower()
            if character not in character_count:
                character_count[character] = 1
            else:
                character_count[character] += 1 

    return character_count

def sort_on(items):
    return items["num"] 

def sort_character_count(character_count):
    characters = []

    for character in character_count:
        characters.append({"char": character, "num": character_count[character]})

    characters.sort(reverse=True, key=sort_on)

    return characters
