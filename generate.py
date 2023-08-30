import sys
import tracery
import json
from tracery.modifiers import base_english


def load_json(filename):
    with open(filename) as file:
        json_data = file.read()
    data = json.loads(json_data)
    return data

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <rules_file>')
    sys.exit(1)

rules_file = sys.argv[1]

if len(sys.argv) > 2:
    num_generations = int(sys.argv[2])
else:
    num_generations = 1

rules = load_json(rules_file)

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
for i in range(num_generations):
    print(grammar.flatten("#origin#")) 
    print("")
    print("")

