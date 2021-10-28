import os
import openai
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import statistics
from secrets import API_Token
sk_en = "Slovak: Dobré ráno!\nEnglish: Good morning!\n###\Slovak: Ako sa máš?\nEnglish: How are you?\n###\nSlovak: Odkiaľ si?\nEnglish: Where are you from?\n###\nSlovak: "

sk_sentences = ['Dnes si môžeme ísť kúpiť oblečenie do nákupného centra, ale nebudeme sa tam môcť najesť', 
                'O druhej poobede budem doma na obed',
                "Môžete mi poslať e-mail s dátumom a časom stretnutia?",
                "Keď sa skončí hokej, mali by sme ísť hrať hokej",
                "Kúpim chladničku za sto dolárov",
                "Musím sa učiť na test z biológie",
                "Poďme do parku a zahrajme si futbal",
                'Môžeme mať na večeru kuracie mäso?',
                "Tento víkend som išiel do domu svojich priateľov a hral videohry",
                "Veľmi sa teším, keď ich zajtra uvidím hrať na koncerte"
                ]

en_sentences = ['Today we can go to the mall to buy clothes, but we will not be able to eat there',
                "I will be home for lunch at two in the afternoon",
                "Can you send me an email with the date and time of the meeting?",
                "When hockey is over, we should go play hockey",
                "I'll buy a refrigerator for a hundred dollars",
                "I have to study for a biology test",
                "Let's go to the park and play football",
                "Can we have chicken for dinner?",
                "This weekend I went to my friends' house and played video games",
                "I'm very happy to see them play at the concert tomorrow"
                ]

openai.api_key = API_Token

en_tranlations = []
for sentence in sk_sentences:
    response = openai.Completion.create(
        engine="davinci",
        prompt=sk_en + sentence + "\nEnglish: ",
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
    )
    
    res = response["choices"][0]["text"]
    en_tranlations.append(res)

# print(en_tranlations)
smoothie = SmoothingFunction().method4
bleu_scores = []
for index in range(len(en_tranlations)):
    reference = en_sentences[index].split()
    candidate = en_tranlations[index].split()
    
    for cand in range(len(candidate)):
        candidate[cand].replace(u'\xa0', u'')
        candidate[cand].replace(u'\n', u'')
    
    print('ref', reference)
    print('cand', candidate)
    print('\n')
    
    BLEUscore = sentence_bleu([reference], candidate, smoothing_function=smoothie)
    bleu_scores.append(BLEUscore)
    
print(bleu_scores)
print(statistics.mean(bleu_scores))
    
