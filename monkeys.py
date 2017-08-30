import random as r
import copy as c
import csv

# This is a list of english words I found online.
with open('wordsEn.txt') as words_file:
    words = set(word.strip().lower() for word in words_file)

class Monkey():
    '''Represents a "monkey" or random string generator. Each instance will have its own set of letter frequencies that are altered for each generation.'''
    avgwords = 0

    def __init__(self,  chars = None):
        if chars is None: # Initialize letter frequencies.
            chars = [['a',5],['b',5],['c',5],['d',5],['e',5],['f',5],['g',5],['h',5],['i',5],['j',5],['k',5],['l',5],['m',5],['n',5],['o',5],['p',5],['q',5],['r',5],['s',5],['t',5],['u',5],['v',5],['w',5],['x',5],['y',5],['z',5]]
        self.wchars = chars

# Copy-pasted from:
# http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
def weighted_choice(choices):
    '''Chooses randomly based on a weight/frequency for each choice.'''
    total= sum(w for c, w in choices)
    x = r.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= x:
            return c
        upto += w

def lavg(list): #lavg = list average
    '''Returns the average of a list of numbers.'''
    tot = sum(list)
    return tot/len(list)

def chk(word):
    '''Checks that given word is, in fact, a word (based on words file above).'''
    return word.lower() in words

def wrand_string(n,chars):
    '''Returns a random string based on the weighted or nonweighted letter choices provided in "chars".'''
    string = " "
    for i in range(n):
        x = r.randrange(100)
        #20% chance of a space, but spaces cannot be consecutive
        if x < 20 and string[-1] != ' ':
            string += " "
        #80% chance of a letter
        else:
            string += weighted_choice(chars)
    return string

def monkeys(n,chars):
    '''Produces random strings and then checks them for words of length 3 letters to 7 letters.'''
    total = wrand_string(n,chars)
    words = []
    for q in range(2,7):
        for a in range(len(total)-q):
            s = total[a:a+q]
            if chk(s) == True and len(s) > 2:
                words.append(s)
    return words

def monkeysaverage(numchars,chars,smooth,wordlen):
    '''Runs the monkey function a bunch of times ('smooth' times) with numchars of characters and the weighted or nonweighted letters in chars and returns the average number of wordlen words found.'''
    results = []
    for i in range(smooth):
        words = monkeys(numchars,chars)
        foo = len([x for x in words if len(x) == wordlen])
        results.append(foo)
    return lavg(results)

def evolve(members, generations):
    '''Iterates through virtual generations of Monkey objects. Monkey's that produce more words have a better chance to pass on their frequency to the next generation. Each generation, the latest base frequencies are randomly modified by a small amount.'''
    with open('{0}{1}.csv'.format(members,generations), 'w') as csvfile:
        mywriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        mems = []
        for m in range(members-1): # Seed the first generation of monkeys.
            mems.append(Monkey())
        for n in range(generations):
            for i in range(members-1):
                ran = r.randrange(0,26)
                mems[i].wchars[ran][1] += r.uniform(-0.1,0.1)
                # How many words will the monkey make with those frequencies?
                mems[i].avgwords = average(500,mems[i].wchars,10,3)
            best = (max(mems,key=lambda x:x.avgwords))
            mywriter.writerow([n,best.avgwords,best.wchars])
            parentgen = c.deepcopy(mems)
            for i in range(members-1):
                # Choose a random (weighted) parent; more words found means higher chance of heredity.
                parent = weighted_choice([(m,m.avgwords) for m in parentgen])
                mems[i].avgwords = 0 # Reset the monkeys.
                mems[i].wchars = c.deepcopy(parent.wchars) # Each monkey of the next generation starts with the frequencies of the best monkey from this generation.
    # Return the frequencies from the monkey who found the most words in the final generation.
    return (max(mems,key=lambda x:x.avgwords)).wchars
