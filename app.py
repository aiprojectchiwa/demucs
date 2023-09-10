import gradio as gr
import demucs
import torch
import tempfile
import os

# Muat model Demucs
model = demucs.load_model()

# Fungsi untuk memproses audio menggunakan Demucs
def process_audio(audio_file):
    audio = gr.inputs.Audio(audio_file)
    
    # Proses audio menggunakan model Demucs
    separated_audio = model.separate(audio)
    
    return {
        "Vocal": separated_audio["vocals"].to("cpu"),
        "Instrumental": separated_audio["accompaniment"].to("cpu")
    }

# Fungsi untuk menyimpan audio ke file sementara
def save_audio_to_tempfile(audio):
    _, temp_file_path = tempfile.mkstemp(suffix=".wav")
    audio.save(temp_file_path)
    return temp_file_path

# Interface untuk mengunggah dan memproses audio
iface = gr.Interface(
    fn=process_audio,
    inputs=gr.inputs.Audio(label="Unggah Audio"),
    outputs=[
        gr.outputs.Audio(label="Vocal"),
        gr.outputs.Audio(label="Instrumental")
    ],
    live=True,
    title="Demucs Audio Separation",
    description="Unggah audio dan pisahkan vokal dan instrumental dengan Demucs."
)

# Jalankan antarmuka Gradio
if __name__ == "__main__":
    iface.launch()
