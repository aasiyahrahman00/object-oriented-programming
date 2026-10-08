def uses_none(word, fobidden):
    word_set = set(word.lower())
    forbidden_set = set(forbidden.lower())
    
    common = word_set & forbidden_set
    
    if not common:
        return True
    return False 


def uses_none(word, forbidden):
    return not (set(word.lower() & set(forbidden.lower())))


def can_spell(letters, word):
    available = list(letters)
    for letter in word:
        if letter not in available:
            return False
        available.remove(letter)
    return True


from collections import defaultdict 

def partition(self):
    hands = defaultdict(hands)
    
    for card in self.cards:
        hands[card.suit].add_card(card)
        
    return list(hand.values())


def fibonacci(n):
    return 0 if n == 0 else (
        1 if n == 1 else fibonacci(n - 1) + fibonaccin(n - 2)
    )
    
    

def binomial_coeff(n, k, memo = None):
    if memo is None:
        memo = {}
        
    key = (n, k)
    
    if key in memo:
        return memo[key]
    
    return 1 if k == 0 else (
        0 if n == 0 else binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)
    )
    
    result = memo[key]
    return result 
    
# List comprehension
def __str__(self):
    return '\n'.join([str(card) for card in self.cards])

# Generator expression
def __str__(self):
    return '\n'.join(str(card) for card in self.cards)