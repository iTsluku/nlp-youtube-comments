''' module exports static content '''

from nltk.corpus import stopwords
# nltk.download('stopwords')

stop_words_add = [
    "mal",
    "mehr",
    "ja",
    "schon",
    "gibt",
    "geht",
    "hast",
    "einfach",
    "ganz",
    "macht",
    "immer",
    "tun",
    "viele",
    "wer",
    "sagen",
    "wäre",
    "genau",
    "dafür",
    "natürlich",
    "seit",
    "wurde",
    "eigentlich",
    "kommt",
    "gesagt",
    "sagt",
    "nie",
    "sehen",
    "deren",
    "versuchen",
    "empfehlen",
    "müssen",
    "kurz",
    "wenig",
    "erste",
    "klare",
    "gar",
    "grad",
    "wohl",
    "oft",
    "ha",
    "schaffen",
    "daher",
    "schreibt",
    "ständig",
    "völlig",
    "verdient",
    "worden",
    "solange",
    "könnt",
    "mann",
    "zeigt",
    "später",
    "erste",
    "iwelche",
    "wen",
    "eigenem",
]

def get_stop_words_add():
    ''' return stop_words_add list'''
    return stop_words_add

def get_stop_words_nltk():
    ''' return german nltk stopwords set'''
    return set(stopwords.words("german"))

def get_stop_words():
    ''' return german stopwords set -- union of german nltk stopwords and stop_words_add'''
    return set(list(set(stopwords.words("german"))) + list(set(get_stop_words_add())))
