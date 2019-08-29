# https://www.codewars.com/kata/your-order-please/train/python

def order(sentence):
    sentence_dict = {}
    for item in sentence.split():
        for b in item:
            if b.isdigit():
                sentence_dict[b] = item
    return " ".join([x[1] for x in sorted(sentence_dict.items())])