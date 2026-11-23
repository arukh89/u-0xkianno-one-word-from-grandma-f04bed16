"""
One Word From Grandma — make.fun entry.

The word a grandma would text about AI: "Chatgipity".

It is how a grandma pronounces ChatGPT when she tries to say it out
loud — "chat-gipity" — and then texts it exactly that way. Warm, a
little baffled, funny on its own, and tied to AI itself: it is the
name of the AI she means, as she hears it. Not the obvious robot word,
not a generic gadget word — her own version of it.
"""

import os

WORD = "Chatgipity"


def main():
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip(), "word must not be only white space"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert WORD.isalpha(), "entry must be a plain word, no punctuation tricks"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
