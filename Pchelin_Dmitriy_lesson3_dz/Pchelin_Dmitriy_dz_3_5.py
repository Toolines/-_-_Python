from random import choice
def get_jokes(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = ''
    for i in range(n):
        word1, word2, word3 = choice(nouns), choice(adverbs), choice(adjectives)
        joke = word1 + ' ' + word2 + ' ' + word3
        print(joke)

get_jokes(4)