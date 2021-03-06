#!/usr/bin/python3

import json
import re

GRAMMAR_START = "normalPlot"

with open("mallhark.json","r") as grammar_file:
    grammar = json.load(grammar_file)

pattern = re.compile("\#[a-zA-Z0-9_\.]+\#")

touched_nodes = {}

def walk_grammar(grammar_node):
    global touched_nodes

#    print ("analyzing "+grammar_node)
    
    if grammar_node not in grammar:
#        print("missing node "+grammar_node)
        return

    if grammar_node in touched_nodes:
#        print("already analyzed "+grammar_node)
        return

    touched_nodes[grammar_node] = True

    tokens=[]
        
    for token in grammar[grammar_node]:
        if token in tokens:
            print("duplicate token in "+grammar_node+": "+token)
        else:
            tokens.append(token)
            
        nodes = pattern.findall(token)
        for node in nodes:
            node=node.replace('#',"")
            node=node.replace(".a","")
            node=node.replace(".capitalize","")
            walk_grammar(node)

walk_grammar(GRAMMAR_START)

for k in grammar.keys():
    if k not in touched_nodes.keys():
        print("Unused token: "+k)
