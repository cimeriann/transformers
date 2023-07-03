from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
batch_sentences = [
    "But what about breakfast?",
    "Don't think he knows about second breakfast, Pip.",
    "What about elevensies?",
]

encoded_input_for_pt = tokenizer(batch_sentences, truncation=True,
                                 padding=True, return_tensors="pt")

encoded_input_for_tf = tokenizer(
    batch_sentences, truncation=True, padding=True, return_tensors="tf")

print(encoded_input_for_tf)
print(encoded_input_for_pt)
