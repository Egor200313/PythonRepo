from collections import Counter


class CaesarBreaker:
    def __init__(self, train_text=""):
        if not train_text:
            self.freqstr = "etainroshdlcfumgpwbyvkqxjz"
        else:
            self.freqstr = self.generate_frequency_string(train_text)

    @staticmethod
    def generate_frequency_string(text: str) -> str:
        arr = list(Counter(text.lower()).items())
        arr.sort(key=lambda x: x[1], reverse=True)
        return ''.join([x[0] for x in arr if x[0].isalpha()])

    @staticmethod
    def generate_transform_dict(text: str, alphabet: str) -> dict:
        return dict(zip(text, alphabet))

    def break_caesar(self, text: str) -> str:
        transform = self.generate_transform_dict(self.generate_frequency_string(text), self.freqstr)
        out = ""
        for letter in text.lower():
            if letter.isalpha():
                out += transform[letter]
            else:
                out += letter
        return out
