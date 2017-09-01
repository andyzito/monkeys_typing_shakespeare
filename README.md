# Monkeys Typing Shakespeare

This is an academic project (from course Programming for Science, Hampshire College Fall 2016 - see http://diviiportfolio.andycodesthings.com/#programming-science).

This Python script attempts to 'evolve' English letter frequences via a relatively small scale evolutionary simulation. It runs a set number of generations (iterations) using a set number of members (Monkey objects).

Each Monkey has:
  1. A dictionary which maps the letters of the English alphabet to a number representing the frequency or weight of that letter.
  2. A number representing the average number of English words found when random strings of a set length are generated via random, weighted choice from the Monkey's own alphabet-weight dictionary (the letter frequencies).

The Monkeys each start with an evenly weighted alphabet. In each generation:
  1. The word counter is reset on every Monkey.
  2. The letter frequencies (the values of each key in the alphabet-weight dictionary) are randomly modified by a small amount (simulating mutation)
  3. Each Monkey generates a set number of strings via random, weighted selection from its own alphabet-weight dictionary.
  4. Each Monkey stores the average number of words found in each of its generated string.
  5. A Monkey is selected as the "seed" of the next generation. Monkeys with more average words (and a "better" letter frequency dictionary) have a higher chance of being selected.
  6. The letter frequencies of the selected "seed" Monkey are stored, all Monkeys are reset.
  7. All Monkeys are updated with the stored frequencies from the "seed" Monkey.
  
After all generations have been simulated, the program will return the most "successful" letter frequency set (the Monkey from the last generation that generated the most average words).

# Results
