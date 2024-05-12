import gradio as gr

from transformers import pipeline

pipe = pipeline("translation", model="google-t5/t5-base")


def translate(text):
    return pipe(text)[0]["translation_text"]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            english = gr.Textbox(label="Englsih Text")
            translate_btn = gr.Button(value="Translate")

        with gr.Column():
            german = gr.Textbox(label="German Text")

    translate_btn.click(translate, inputs=english, outputs=german)
    examples = gr.Examples(examples=["I went to the supermaket yesterday.", "Hellen is good at swimming."],
                           inputs=[english])

demo.launch(share=True)