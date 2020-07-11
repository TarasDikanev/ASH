import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

import string
import pymorphy2
morph = pymorphy2.MorphAnalyzer()


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
    'лол': 'лол', 'белой': 'белый', 'ху¤се': 'ху¤се', 'джинса': 'джинса', 'гент': 'гент', 'ал': 'ал', 
    'але': 'але', 'алах': 'аллах', 'усы': 'усы', 'усе': 'усе', 'штоле': 'штоле', 'чето': 'чето', 'че': 'че', 
    'неее': 'неее', 'чтоле': 'чтоле', 'боков': 'бок', 'кароч': 'кароч', 'нете': 'нет_(сеть)', 'парней': 'парень',
    'охуевша¤': 'охуевший', 'охуевшей': 'охуевший', 'охуевшие': 'охуевший', 'охуевший': 'охуевший', 
    'охуевшим': 'охуевший', 'охуевшими': 'охуевший', 'охуевших': 'охуевший', 'ахуевшими': 'ахуевший', 
    'охуел': 'охуеть', 'охуела': 'охуеть', 'охуели': 'охуеть', 'спиздили': 'спиздить', 'долбоеб': 'долбоеб', 
    'долбоЄб': 'долбоеб', 'хуею': 'хуеть', 'ебло': 'ебло', 'ебли': 'ебать'
}

postprocessing = {
    'убунт': 'убунту', 'гент': 'генту', 'дебиана': 'дебиан', 'ктулха': 'ктулху', 'вист': 'виста', 
    'винд': 'винда', 'ютуба': 'ютуб', 'фич': 'фича', 'смайла': 'смайл', 'свича': 'свич', 'хабра': 'хабр', 
    'хабрахабра': 'хабрахабр', 'одмина': 'одмин', 'линуха': 'линух', 'хаба': 'хаб', 'пинга': 'пинг', 
    'конфига': 'конфиг', 'козлы': 'козЄл', 'нихуй': 'ниху¤', 'хуйн': 'хуйн¤', 'пидора': 'пидор', 
    'пидоров': 'пидор', 'пиздюл¤' : 'пиздюли', 'пидором': 'пидор', 'мудаки': 'мудак', 'мудаками': 'мудак', 
    'мудаком': 'мудак', 'мудака': 'мудак', 'заебал': 'заебать', 'съебал': 'съебать', 'доебал': 'доебать',
    'проебали': 'проебать', 'проебал': 'проебать', 'разъебал': 'разъебать', 'заебали': 'заебать', 
    'ебали': 'ебать', 'уебали': 'уебать', 'ебал': 'ебать', 'выебал': 'выебать', 'наебал': 'наебать', 
    'сук': 'сука', 'херовин': 'херовина', 'херачил': 'херачить', 'херачили': 'херачить', 'захерачил': 'захерачить', 
    'отхерачил': 'отхерачить', 'херней': 'херн¤', 'дохер': 'дохера', 'отпиздим': 'отпиздить', 
    'спиздил': 'спиздить', 'насрало': 'насрать', 'дибить': 'дибил', 'ахуесть': 'ахуеть', 'пиздюл¤': 'пиздюли',
    'ебета': 'ебать', 'ебут': 'ебать', 'серЄг': 'серЄга', 'матана': 'матан', 'игнора': 'игнор', '¤м': '¤ма', 
    'джинса': 'джинсы', 'коты': 'кот', 'вейдЄр': 'вейдер', 'побежалый': 'побежать', 'похуделый': 'похудеть', 
    'комаров': 'комар', 'маркета': 'маркет', 'трусик': 'трусики', 'медведа': 'медвед', 'охренель': 'охренеть',
    'дот': 'дота', 'капЄс': 'капс', 'винампа': 'винамп', 'ир': 'ира', 'анастасий': 'анастаси¤', 'марин': 'марина', 
    'дим': 'дима', 'димона': 'димон', 'красных': 'красный', 'поверь': 'поверить', 'живить': 'жить',
    'печенек': 'печенька', 'тапка': 'тапок', 'игнора': 'игнор', 'донцов': 'донцова', 'скинхэда': 'скинхэд', 
    'скарлетта': 'скарлетт', 'боков': 'боковой', 'друган': 'друган', 'друганом': 'друган', 'другана': 'друган', 
    'мазд': 'мазда', 'каптать': 'капча', 'лежалый': 'лежать', 'оливь¤': 'оливье', 'парка': 'парк',
    'орало': 'орать', 'охренела': 'охренеть', 'основный': 'основной', 'боев': 'боевой', 'тимлида': 'тимлид', 
    'млина': 'млин', 'вырасти': 'вырастать', 'фот': 'фота', 'другать': 'друган', 'фейспалма': 'фейспалм', 
    'погуглила': 'погуглить', 'погуголь': 'погугли', 'семейник': 'семейники', 'донестись': 'доноситьс¤', 
    'тибить': 'тиб¤', 'уползти': 'уползать', 'смутитьс¤': 'смущатьс¤'
}

def lemmatize(token):
    if token in exceptions:
        lemma = exceptions[token]
    else:
        lemma = morph.parse(token)[0].normal_form
        if lemma in postprocessing:
            lemma = postprocessing[lemma]
    return lemma

