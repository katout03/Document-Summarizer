import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if not text or text.strip() == "":
        return "Please enter some text to summarize."
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, label="Paste your text here..."),
    outputs=gr.Textbox(label="Generated Summary"),
    title="Intelligent Document Summarizer",
    description="A tool powered by Hugging Face to automatically summarize long articles into concise paragraphs."
)

if __name__ == "__main__":
    interface.launch()
