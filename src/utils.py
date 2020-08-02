import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

import string
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

import json

import jupyter_beeper


# Tokenization
to_list = ['когда-то', 'тогда-то', 'куда-то', 'откуда-то', 'туда-то', 'где-то', 'чей-то', 'какой-то', 'такой-то', 'который-то', 
           'как-то', 'так-то', 'зачем-то', 'всего-то', 'чего-то', 'отчего-то', 'сколько-то', 'то-то', 'кто-то', 'что-то', 'тот-то', 
           'тут-то', 'почему-то']

def tokenize(text):
    tokens = word_tokenize(text.lower(), language = 'russian')
    tokens = [t for t in tokens if t not in (string.punctuation + "''``Ђї")]
    tokens2 = []
    for t in tokens:
        if t[-3:] == '-то' and t not in to_list:
            tokens2 += [t[:-3], '-то']
        else:
            tokens2 += [t]
    return tokens2


# Lemmatization
exceptions = {
    'лол': 'лол', 'белой': 'белый', 'хуясе': 'хуясе', 'джинса': 'джинса', 'гент': 'гент', 'ал': 'ал', 
    'але': 'але', 'алах': 'аллах', 'усы': 'усы', 'усе': 'усе', 'штоле': 'штоле', 'чето': 'чето', 'че': 'че', 
    'неее': 'неее', 'чтоле': 'чтоле', 'боков': 'бок', 'кароч': 'кароч', 'нете': 'нет_(сеть)', 'парней': 'парень',
    'охуевшая': 'охуевший', 'охуевшей': 'охуевший', 'охуевшие': 'охуевший', 'охуевший': 'охуевший', 
    'охуевшим': 'охуевший', 'охуевшими': 'охуевший', 'охуевших': 'охуевший', 'ахуевшими': 'ахуевший', 
    'охуел': 'охуеть', 'охуела': 'охуеть', 'охуели': 'охуеть', 'спиздили': 'спиздить', 'долбоеб': 'долбоеб', 
    'долбоёб': 'долбоеб', 'хуею': 'хуеть', 'ебло': 'ебло', 'ебли': 'ебать', 'пpизывник': 'призывник',
    'падруга' : 'падруга', 'y': 'у'
}

postprocessing = {
    'убунт': 'убунту', 'гент': 'генту', 'дебиана': 'дебиан', 'ктулха': 'ктулху', 'вист': 'виста', 
    'винд': 'винда', 'ютуба': 'ютуб', 'фич': 'фича', 'смайла': 'смайл', 'свича': 'свич', 'хабра': 'хабр', 
    'хабрахабра': 'хабрахабр', 'одмина': 'одмин', 'линуха': 'линух', 'хаба': 'хаб', 'пинга': 'пинг', 
    'конфига': 'конфиг', 'козлы': 'козёл', 'нихуй': 'нихуя', 'хуйн': 'хуйня', 'пидора': 'пидор', 
    'пидоров': 'пидор', 'пиздюля' : 'пиздюли', 'пидором': 'пидор', 'мудаки': 'мудак', 'мудаками': 'мудак', 
    'мудаком': 'мудак', 'мудака': 'мудак', 'заебал': 'заебать', 'съебал': 'съебать', 'доебал': 'доебать',
    'проебали': 'проебать', 'проебал': 'проебать', 'разъебал': 'разъебать', 'заебали': 'заебать', 
    'ебали': 'ебать', 'уебали': 'уебать', 'ебал': 'ебать', 'выебал': 'выебать', 'наебал': 'наебать', 
    'сук': 'сука', 'херовин': 'херовина', 'херачил': 'херачить', 'херачили': 'херачить', 'захерачил': 'захерачить', 
    'отхерачил': 'отхерачить', 'херней': 'херня', 'дохер': 'дохера', 'отпиздим': 'отпиздить', 
    'спиздил': 'спиздить', 'насрало': 'насрать', 'дибить': 'дибил', 'ахуесть': 'ахуеть', 'пиздюля': 'пиздюли',
    'ебета': 'ебать', 'ебут': 'ебать', 'серёг': 'серёга', 'матана': 'матан', 'игнора': 'игнор', 'ям': 'яма', 
    'джинса': 'джинсы', 'коты': 'кот', 'вейдёр': 'вейдер', 'побежалый': 'побежать', 'похуделый': 'похудеть', 
    'комаров': 'комар', 'маркета': 'маркет', 'трусик': 'трусики', 'медведа': 'медвед', 'охренель': 'охренеть',
    'дот': 'дота', 'капёс': 'капс', 'винампа': 'винамп', 'ир': 'ира', 'анастасий': 'анастасия', 'марин': 'марина', 
    'дим': 'дима', 'димона': 'димон', 'красных': 'красный', 'поверь': 'поверить', 'живить': 'жить',
    'печенек': 'печенька', 'тапка': 'тапок', 'игнора': 'игнор', 'донцов': 'донцова', 'скинхэда': 'скинхэд', 
    'скарлетта': 'скарлетт', 'боков': 'боковой', 'друган': 'друган', 'друганом': 'друган', 'другана': 'друган', 
    'мазд': 'мазда', 'каптать': 'капча', 'лежалый': 'лежать', 'оливья': 'оливье', 'парка': 'парк',
    'орало': 'орать', 'охренела': 'охренеть', 'основный': 'основной', 'боев': 'боевой', 'тимлида': 'тимлид', 
    'млина': 'млин', 'вырасти': 'вырастать', 'фот': 'фота', 'другать': 'друган', 'фейспалма': 'фейспалм', 
    'погуглила': 'погуглить', 'погуголь': 'погугли', 'семейник': 'семейники', 'донестись': 'доноситься', 
    'тибить': 'тибя', 'уползти': 'уползать', 'смутиться': 'смущаться', 'мyж': 'муж'
}

# Replace latin symbol with same looking cirillic in russian words
def replace_latin(word, lat, cyr):
    if (lat in word) and any([c in word for c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']):
        word = word.replace(lat, cyr)
    return word

def lemmatize(token):
    if token in exceptions:
        lemma = exceptions[token]
    else:
        if token[0] == '-':
            token = token[1:]
        token = replace_latin(token, 'y', 'у')
        token = replace_latin(token, 'p', 'р')
        lemma = morph.parse(token)[0].normal_form
        if lemma in postprocessing:
            lemma = postprocessing[lemma]
    return lemma


def LoadIndices():
    an_jokes_direct = json.loads(open('..\\data\\interim\\an_jokes_direct.json', 'r', encoding = 'utf-8').read())
    an_jokes_inverted = json.loads(open('..\\data\\interim\\an_jokes_inverted.json', 'r', encoding = 'utf-8').read())
    bash_jokes_direct = json.loads(open('..\\data\\interim\\bash_jokes_direct.json', 'r', encoding = 'utf-8').read())
    bash_jokes_inverted = json.loads(open('..\\data\\interim\\bash_jokes_inverted.json', 'r', encoding = 'utf-8').read())
    return an_jokes_direct, an_jokes_inverted, bash_jokes_direct, bash_jokes_inverted

def LoadDatasets():
    an_jokes   = json.loads(open('..\\data\\processed\\an_jokes_eq.json', 'r', encoding = 'utf-8').read())
    bash_jokes = json.loads(open('..\\data\\processed\\bash_jokes_eq.json', 'r', encoding = 'utf-8').read())
    return an_jokes, bash_jokes

# Train and test samples indices
def TrainTestIdx(jokes, train_share = 0.75):
    #N = len(jokes)
    sss = StratifiedShuffleSplit(1, train_size = train_share)
    y = [joke[-1] for joke in jokes]
    return list(sss.split(np.zeros(len(jokes)), y))[0]


def Beep():
    b = jupyter_beeper.Beeper()
    b.beep(frequency=530, secs=0.8, blocking=True)


