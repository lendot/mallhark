import tracery_plot
from plot_image import PlotImage

import gradio as gr

def generate_tracery():
    return tracery.generate()

def generate_llm(tracery_output):
    return "BOT OUTPUT: "+tracery_output 

def generate_image(llm_output):
    return plot_image.render(llm_output) 

with gr.Blocks() as server:
    # name = gr.Textbox(label="Name")
    tracery_output = gr.Textbox(label="Tracery Output",interactive=True)
    generate_tracery_btn = gr.Button("Generate Tracery Plot")
    generate_tracery_btn.click(fn=generate_tracery, outputs=tracery_output, api_name="generate_tracery")
    llm_output = gr.Textbox(label="LLM Output",interactive=True)
    generate_llm_btn = gr.Button("Generate LLM Plot")
    generate_llm_btn.click(fn=generate_llm, inputs=tracery_output, outputs=llm_output, api_name="generate_llm")
    image_output = gr.Image(label="Image",height=500)
    generate_image_btn = gr.Button("Generate Image")
    generate_image_btn.click(fn=generate_image, inputs=llm_output, outputs=image_output, api_name="generate_image")
                           

tracery = tracery_plot.TraceryPlot("mallhark.json")
plot_image = PlotImage() 

server.launch(server_name="0.0.0.0")


