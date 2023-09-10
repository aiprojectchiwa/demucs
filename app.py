import os
import gradio as gr
from scipy.io.wavfile import write


def inference(audio):
  os.makedirs("out", exist_ok=True)
  write('test.wav', audio[0], audio[1])
  os.system("python3 -m demucs.separate -n mdx_extra_q -d cpu test.wav -o out")
  return "./out/mdx_extra_q/test/vocals.wav","./out/mdx_extra_q/test/bass.wav",\
"./out/mdx_extra_q/test/drums.wav","./out/mdx_extra_q/test/other.wav"

parser = argparse.ArgumentParser()
parser.add_argument('--api', action="store_true", default=False)
parser.add_argument("--share", action="store_true", default=False, help="share gradio app")
  
title = "Demucs"
description = "Gradio demo for Demucs: Music Source Separation in the Waveform Domain. To use it, simply upload your audio, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/1911.13254' target='_blank'>Music Source Separation in the Waveform Domain</a> | <a href='https://github.com/facebookresearch/demucs' target='_blank'>Github Repo</a></p>"

examples=[['test.mp3']]
gr.Interface(
    inference, 
    gr.inputs.Audio(type="numpy", label="Input"), 
    [gr.outputs.Audio(type="filepath", label="Vocals"),gr.outputs.Audio(type="filepath", label="Bass"),gr.outputs.Audio(type="filepath", label="Drums"),gr.outputs.Audio(type="filepath", label="Other")],
    title=title,
    description=description,
    article=article,
    examples=examples
    ).launch(enable_queue=True)
