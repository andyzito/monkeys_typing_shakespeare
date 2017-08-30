# Monkeys Typing Shakespeare

This Python script is sort of an attempt to simulate the Infinite Monkey Theorem. The Infinite Monkey Theorem is the thought experiment where you have an infinite number of monkeys banging away on typewriters, and eventually they produce the works of Shakespeare through pure random chance.

My script runs with this idea, and attempts to 'evolve' English letter frequences via a relatively small scale evolutionary simulation. In brief, it runs through a bunch of virtual generations. Each generation has a bunch of Monkey objects which generate random strings based on individual weighted alphabets. Each generation seeds the next generation with the most successful letter frequencies from itself, most successful being defined by how many words were generated using random choice from the weighted alphabet (letter frequencies).

# Results
