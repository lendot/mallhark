import tracery_plot
from plot_image import PlotImage
import llm_plot
import gradio as gr

def generate_tracery():
    return tracery.generate()

def generate_llm(tracery_output,temperature):
    return llm.generate(tracery_output, top_k = 100, temperature = temperature)

def generate_image(llm_output):
    return plot_image.render(llm_output) 

with gr.Blocks() as server:
    # name = gr.Textbox(label="Name")
    tracery_output = gr.Textbox(label="Tracery Output",interactive=True)
    generate_tracery_btn = gr.Button("Generate Tracery Plot")
    generate_tracery_btn.click(fn=generate_tracery, outputs=tracery_output, api_name="generate_tracery")
    llm_temperature = gr.Slider(0, 10.0, value = 1.1, step = 0.01, label = "Temperature")
    llm_output = gr.Textbox(label="LLM Output",interactive=True)
    generate_llm_btn = gr.Button("Generate LLM Plot")
    generate_llm_btn.click(fn=generate_llm, inputs=[tracery_output, llm_temperature], outputs=llm_output, api_name="generate_llm")
    image_output = gr.Image(label="Image",height=300)
    generate_image_btn = gr.Button("Generate Image")
    generate_image_btn.click(fn=generate_image, inputs=llm_output, outputs=image_output, api_name="generate_image")
                           

MODEL_FILE = "/home/llanphar/src/oobabooga_linux/text-generation-webui/models/Wizard-Vicuna-30B-Uncensored.ggmlv3.q4_K_M.bin"

tracery = tracery_plot.TraceryPlot("mallhark.json")
plot_image = PlotImage() 
llm = llm_plot.LLMPlot(MODEL_FILE,n_gpu_layers=100)

server.launch(server_name="0.0.0.0")


