import json
import random


def json_convertor():
    with open('C:\\Users\murea\\Desktop\\Python\\Proiecte Python\\Hangman '
              'Project\\dictionary_of_words.json') as json_file:
        data_from_json = json.load(json_file)
        categories = data_from_json['categories']

    return categories


def list_extractor(given_category: str, type_of_extraction: int):
    categories = json_convertor()
    list_of_words_with_hints = []
    list_of_words_without_hints = []

    for category in categories:
        if category['category'] == given_category:
            for word in category['words']:
                list_of_words_with_hints.append([word['value'], word['hint']])
                list_of_words_without_hints.append(word['value'])

    if type_of_extraction == 1:
        return list_of_words_with_hints
    else:
        return list_of_words_without_hints


def random_word_extractor(given_category: str):
    categories = json_convertor()
    list_of_words = []

    for category in categories:
        if category['category'] == given_category:
            for word in category['words']:
                list_of_words.append(word['value'])

    return random.choice(list_of_words)