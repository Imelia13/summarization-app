import torch
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "imelia13/t5-indosum-summarizer"

device = torch.device("cpu")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
model.to(device)
model.eval()


def clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def summarize_text(text: str) -> str:
    text = clean_text(text)

    inputs = tokenizer(
        "ringkas: " + text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=128,
            num_beams=4,
            early_stopping=True
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
