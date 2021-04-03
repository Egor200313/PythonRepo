from collections import Counter

def generate_frequency_dict(text):
    arr = list(Counter(text.lower()).items())
    arr.sort(key=lambda x: x[1], reverse=True)
    #print(arr)
    return ''.join([x[0] for x in arr if x[0].isalpha()])

def generate_transform_dict(text, alphabet):
    print(dict(zip(text, alphabet)))
    return dict(zip(text, alphabet))

def break_caesar(text):
    eng = "etainroshdlcfumgpwbyvkqxjz"
    transform = generate_transform_dict(generate_frequency_dict(text), eng)
    out = ""
    for letter in text.lower():
        if letter.isalpha():
            out += transform[letter]
        else:
            out += letter
    return out
