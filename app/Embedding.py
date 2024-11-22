from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def TakeFields(person_data, target_data):
    
    if isinstance(person_data, str):
        person_data = [person_data]  
    if isinstance(target_data, str):
        target_data = [target_data]  

    if all(isinstance(x, str) for x in person_data) and all(isinstance(x, str) for x in target_data):
        return Embedding(person_data, target_data)
    else:
        return 0.0

def Embedding(person_data, target_data):
    
    similarity_scores = []

    for person_item in person_data:
        for target_item in target_data:
            inputs1 = tokenizer(person_item, return_tensors="pt")
            inputs2 = tokenizer(target_item, return_tensors="pt")

            with torch.no_grad():
                outputs1 = model(**inputs1).last_hidden_state.mean(dim=1)
                outputs2 = model(**inputs2).last_hidden_state.mean(dim=1)

            cos_sim = torch.nn.functional.cosine_similarity(outputs1, outputs2)
            similarity_scores.append(cos_sim.item())

    if len(similarity_scores) == 0:
        return 0
    return sum(similarity_scores) / len(similarity_scores)