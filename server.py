import tomli
import tracery_plot
from plot_image import PlotImage
import llm_plot
import gradio as gr

styles = [
        'horror',
        'zombie',
        'vampire',
        'space opera',
        'spaghetti western',
        'dystopian',
        'post-apocalyptic',
        'time travel',
        'psychological thriller',
        'buddy cop',
        'suspense',
        'film noir',
        'science fiction'
]

def generate_tracery():
    return tracery.generate()

def generate_llm(tracery_output,temperature,style):
    if isinstance(style, list) and len(style) == 0:
        style = None
    return llm.generate(tracery_output, top_k = 100, temperature = temperature, style = style)

def generate_image(llm_output):
    return plot_image.render(llm_output) 

with gr.Blocks() as server:
    # name = gr.Textbox(label="Name")
    tracery_output = gr.Textbox(label="Tracery Output",interactive=True)
    generate_tracery_btn = gr.Button("Generate Tracery Plot")
    generate_tracery_btn.click(fn=generate_tracery, outputs=tracery_output, api_name="generate_tracery")
    llm_temperature = gr.Slider(0, 10.0, value = 1.1, step = 0.01, label = "Temperature")
    llm_style = gr.Dropdown(styles,label="Style")
    llm_output = gr.Textbox(label="LLM Output",interactive=True)
    generate_llm_btn = gr.Button("Generate LLM Plot")
    generate_llm_btn.click(fn=generate_llm, inputs=[tracery_output, llm_temperature, llm_style], outputs=llm_output, api_name="generate_llm")
    image_output = gr.Image(label="Image",height=300)
    generate_image_btn = gr.Button("Generate Image")
    generate_image_btn.click(fn=generate_image, inputs=llm_output, outputs=image_output, api_name="generate_image")
                           

with open("config.toml", mode="rb") as fp:
    config = tomli.load(fp)

#MODEL_FILE = "/home/llanphar/src/text-generation-webui/models/Wizard-Vicuna-30B-Uncensored.ggmlv3.q4_K_M.bin"
MODEL_FILE = "/home/llanphar/src/text-generation-webui/models/wizardlm-30b-uncensored.ggmlv3.q4_K_M.bin"

tracery = tracery_plot.TraceryPlot(config['tracery']['grammar'])
plot_image = PlotImage() 
llm = llm_plot.LLMPlot(
        config['llm']['model'],
        n_gpu_layers = config['llm']['n_gpu_layers'],
        prompt_pre = config['llm']['prompt_pre'],
        prompt_post = config['llm']['prompt_post']
)

print("Starting server")
server.launch(server_name="0.0.0.0")


