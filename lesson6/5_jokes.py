import random

n = int(input("insert n: "))


def get_joke():
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    get_word = lambda words: random.choice(words)

    result = []
    for word in nouns, adverbs, adjectives:
        result.append(get_word(word))

    return ' '.join(result)


def get_jokes(how_many: int) -> enumerate[str]:
    jokes = []
    for _ in range(n):
        jokes.append(get_joke())
    return jokes


print(get_jokes(n))
