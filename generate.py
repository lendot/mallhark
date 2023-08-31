import sys
import tracery
import json
from tracery.modifiers import base_english
from llama_cpp import Llama


def load_json(filename):
    with open(filename) as file:
        json_data = file.read()
    data = json.loads(json_data)
    return data

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <rules_file>')
    sys.exit(1)

MODEL_FILE = "/home/llanphar/src/oobabooga_linux/text-generation-webui/models/Wizard-Vicuna-30B-Uncensored.ggmlv3.q4_0.bin"

print(f'loading {MODEL_FILE}...')
llama = Llama(model_path = MODEL_FILE,n_ctx = 1024, n_gpu_layers=32)
print("Done.")

llama.reset()

rules_file = sys.argv[1]

#if len(sys.argv) > 2:
#    num_generations = int(sys.argv[2])
#else:
#    num_generations = 1

rules = load_json(rules_file)

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

plot_preamble = "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\n\n"

plot_instructions = plot_preamble + "### Human: Write a description in 100 words or less for the following Hallmark Movie. " + grammar.flatten("#origin#") + "\n### Assistant: " 

print(plot_instructions) 

"""
plot_instructions_bytes = plot_instructions.encode(encoding = 'UTF-8')
plot_tokens = llama.tokenize(plot_instructions_bytes)

llm_plot=""
"""

completion_chunks = llama.create_completion(
        plot_instructions,
        top_k = 40,
        top_p = 0.9,
        temperature = 0.3,
        max_tokens = 300,
        stream=True
)

output = ""

for completion_chunk in completion_chunks:
    print('',end='',flush=True)
    text = completion_chunk['choices'][0]['text']
    output += text
    print(text,end='',flush=True)

