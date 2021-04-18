from collections import Counter


def generate_frequency_string(text: str) -> str:
    arr = list(Counter(text.lower()).items())
    arr.sort(key=lambda x: x[1], reverse=True)
    return ''.join([x[0] for x in arr if x[0].isalpha()])


def generate_transform_dict(text: str, alphabet: str) -> dict:
    return dict(zip(text, alphabet))


def break_caesar(text: str) -> str:
    eng = "etainroshdlcfumgpwbyvkqxjz"
    transform = generate_transform_dict(generate_frequency_string(text), eng)
    out = ""
    for letter in text.lower():
        if letter.isalpha():
            out += transform[letter]
        else:
            out += letter
    return out
