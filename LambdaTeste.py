import pandas as pd
pd.set_option('display.max_colwidth', -1)

def word_count(review, word):
    cont = 0
    review = review.lower()
    if word in review.lower():
        return review.count(word)
    else:
        return 0

dt = pd.DataFrame([['Atendimento excelente, chega de coisa ruim no mercado','positivo'],
                   ['Gostei muito do atendimento, estão de parabéns!!,recomendo muito!!','positivo'],
                   ['É uma pena não ter estacionamento, isso prejudica demais!','negativo'],
                   ['Achei que tinha estacionamento, isso quebrou minhas pernas','negativo'],
                   ['Achei o preço salgado!.','negativo'],
                   ['Comida muito boa, preço bom!!','positivo'],
                   ['Preço bom e lugar aconchegante.','positivo']]
                   , columns=['review','sentiment'])

dt['atendimento'] = dt['review'].apply(lambda x: word_count(x, 'atendimento'))
dt['estacionamento'] = dt['review'].apply(lambda x: word_count(x, 'estacionamento'))
dt['preço'] = dt['review'].apply(lambda x: word_count(x, 'preço'))
dt['comida'] = dt['review'].apply(lambda x: word_count(x, 'comida'))
