import torch
from transformers import pipeline
 
# Load model
model_id = "meta-llama/Llama-3.2-1B-Instruct"
 
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
 
# Initialize conversation history
messages = [
    {
        "role": "system",
        "content": "You are a professional chatbot who always responds in helpful and responsive manner!"
    }
]
 
print("AdvitChatBot-llama (type 'exit' to quit)\n")
 
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
 
    # Add user message
    messages.append({"role": "user", "content": user_input})
 
    # Generate response
    outputs = pipe(
        messages,
        max_new_tokens=256,
    )
 
    # Extract assistant reply
    reply = outputs[0]["generated_text"][-1]["content"]
 
    # Print and store response
    print(f"Pirate: {reply}\n")
 
    messages.append({"role": "assistant", "content": reply})