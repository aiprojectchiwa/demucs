import gradio as gr
import demucs

# Fungsi untuk memproses audio menggunakan Demucs
def process_audio(audio_file):
    # Muat model Demucs
    model = demucs.load_model()

    # Baca audio dari file yang diunggah
    audio = gr.inputs.Audio(type="numpy", label="Input")

    # Proses audio menggunakan model Demucs
    separated_audio = model.separate(audio)

    return separated_audio

# Membuat antarmuka Gradio
iface = gr.Interface(
    fn=process_audio,
    inputs="audio",
    outputs=gr.outputs.Audio(label="Audio Terpisah"),
    live=True,
    title="Demucs Audio Separation",
    description="Pisahkan sumber audio dengan Demucs."
)

# Jalankan antarmuka Gradio
if __name__ == "__main__":
    iface.launch()
