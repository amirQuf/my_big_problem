EN_TO_FA = {
    "q": "ض",
    "w": "ص",
    "e": "ث",
    "r": "ق",
    "t": "ف",
    "y": "غ",
    "u": "ع",
    "i": "ه",
    "o": "خ",
    "p": "ح",
    "[": "ج",
    "]": "چ",
    "a": "ش",
    "s": "س",
    "d": "ی",
    "f": "ب",
    "g": "ل",
    "h": "ا",
    "j": "ت",
    "k": "ن",
    "l": "م",
    ";": "ک",
    "'": "گ",
    "z": "ظ",
    "x": "ط",
    "c": "ز",
    "v": "ر",
    "b": "ذ",
    "n": "د",
    "m": "پ",
    ",": "و",
    ".": ".",
    "/": "/",
    "`": "\u200c",  # zero-width non-joiner placeholder (not exact); optional
}


FA_TO_EN = {v: k for k, v in EN_TO_FA.items()}


EXTRA_FA_TO_EN = {
    "؛": ";",
    "،": ",",
    "؟": "?",
    "«": "<",
    "»": ">",
    "‌": "",  # zero-width non-joiner
}
FA_TO_EN.update(EXTRA_FA_TO_EN)

import re


def inverter_EN_TO_FA(s):
    """
    Changing Gibberish English words to persian
    """
    result = ""
    for ch in s:
        if ch in EN_TO_FA:
            result += EN_TO_FA[ch]
        else:
            result += " "
    return result


def inverter_FA_TO_EN(s):
    """
    Changing Gibberish persian words to English
    """
    result = ""
    for ch in s:
        if ch in FA_TO_EN:
            result += FA_TO_EN[ch]
        else:
            result += " "
    return result


if __name__ == "__main__":
    s = "Amir"

    result = inverter_EN_TO_FA(s.lower())
    print(result)

    s1 = "حاح"  # php
    result = inverter_FA_TO_EN(s1.lower())
    print(result)
