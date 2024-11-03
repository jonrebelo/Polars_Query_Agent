from transformers import T5ForConditionalGeneration, AutoTokenizer
import torch

# Path to the local model directory
model_path = "F:/00_Github/Polars_Query_Agent/Model"  # Replace with the actual path

# Load the tokenizer and model from the local path
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path).to("cuda")

# Function to generate text using mixed precision
def generate_text(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    
    with torch.cuda.amp.autocast():  # Enable mixed precision
        outputs = model.generate(inputs["input_ids"], max_length=max_length)
        
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example prompt
prompt = "Write a Polars DataFrame query to filter rows where the column 'age' is greater than 30:"
generated_code = generate_text(prompt)

print("Generated Code:\n", generated_code)