# import text processor
from transformers import AutoTokenizer

# instantiate a tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

# pass text to tokenizer
encoded_input = tokenizer("Do not meddle in the affairs of wizards, for they are subtle and quick to anger.")

print(encoded_input)

# print original text
print(tokenizer.decode(encoded_input["input_ids"]))