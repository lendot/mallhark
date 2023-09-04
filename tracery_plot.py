import sys
import tracery
import json
from tracery.modifiers import base_english

class TraceryPlot: 
    """ Tracery plot generator """

    def __init__(self, grammar_file):

        self.grammar_file = grammar_file


    def _load_json(self,filename):
        with open(filename) as file:
            json_data = file.read()
        data = json.loads(json_data)
        return data

    def generate(self, start_token = "#origin#"):
        grammar_rules = self._load_json(self.grammar_file)
        self.grammar =  tracery.Grammar(grammar_rules)
        self.grammar.add_modifiers(base_english)

        plot = self.grammar.flatten(start_token)
        return plot

