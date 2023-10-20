import random

nouns = ["fossil","horse", "aardvark", "judge", "chef","mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes","curdles"]
adjectives = ["furry","balding", "incredulous", "fragrant","exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in","like", "over", "within"]
adverbs = [ "curiously", "extravagantly", "tantalizingly", "furiously","sensuously"]

def make_poem():
    # Nouns
    n1 = random.choice(nouns)
    n2 = random.choice(nouns)
    n3 = random.choice(nouns)
    # Verbs
    v1 = random.choice(verbs)
    v2 = random.choice(verbs)
    v3 = random.choice(verbs)
    # Adjectives
    a1 = random.choice(adjectives)
    a2 = random.choice(adjectives)
    a3 = random.choice(adjectives)
    # Prepositions
    p1 = random.choice(prepositions)
    p2 = random.choice(prepositions)
    # Adverbs
    a = random.choice(adverbs)

    if "aeiou".find(a[0]) != -1: 
        article = "An"
    else:
        article = "A"

    poem = f'''{article} {a1} {n1}
{article} {a1} {n1} {v1} {p1} the {a2} {n2}
{a}, the {n1} {v2}
the {n2} {v3} {p2} a {a3} {n2}
    '''
    return poem

print(make_poem())
