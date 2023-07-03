from datasets import load_dataset
from transformers import AutoTokenizer

dataset = load_dataset("yelp_review_full")
dataset["train"][100]

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")


def tokenize_function(demos):
    return tokenizer(demos["text"], padding="max_length", truncation=True, )


tokenized_datasets = dataset.map(tokenize_function, batched=True)
