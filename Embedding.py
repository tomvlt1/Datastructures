from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Tokenize and encode inputs
keywords = [
    "Bachelors in Business Management", "Data Science", "International Relations", 
    "Masters Business Management and Data Science", "Computer Science", 
    "Biochemical Engineering", "Law", "Medicine", "Economics", "Applied Maths"
]
for i in keywords:
    for j in keywords:
        inputs1 = tokenizer(i, return_tensors="pt")
        inputs2 = tokenizer(j, return_tensors="pt")

        # Generate embeddings
        with torch.no_grad():
            outputs1 = model(**inputs1).last_hidden_state.mean(dim=1)  # Pooling
            outputs2 = model(**inputs2).last_hidden_state.mean(dim=1)
        cos_sim = torch.nn.functional.cosine_similarity(outputs1, outputs2)
        print(f"Similarity:  between {i} - {j} {cos_sim.item()}")

inputs1 = tokenizer("entrepreneurship", return_tensors="pt")
inputs2 = tokenizer("literature", return_tensors="pt")

# Generate embeddings


# Compute cosine similarity

