from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
batch_sentences = [
    "But what about breakfast?",
    "Don't think he knows about second breakfast, Pip.",
    "What about elevensies?",
]

encoded_input = tokenizer(batch_sentences, truncation=True,
                          padding=True, return_tensors="pt")

print(encoded_input)
