from transformers import AutoTokenizer, AutoModel
import torch
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def TakeFields(person1, person2):
    if isinstance(person1, str) and isinstance(person2, str):
        return Embedding([person1], [person2])
    else:
        return "Please enter valid strings"



def Embedding(person1, person2):
    interest = []
    for i in person1:
        for j in person2:
            inputs1 = tokenizer(i, return_tensors="pt")
            inputs2 = tokenizer(j, return_tensors="pt")

            with torch.no_grad():
                outputs1 = model(**inputs1).last_hidden_state.mean(dim=1)
                outputs2 = model(**inputs2).last_hidden_state.mean(dim=1)
            cos_sim = torch.nn.functional.cosine_similarity(outputs1, outputs2)
            #print(f"Cosine similarity between '{i}' and '{j}': {cos_sim.item()}")
            interest.append(cos_sim.item())
    
    if len(interest) == 0:
        return 0
    return sum(interest) / len(interest) #we are averaging out the cosine similarity of the two persons for sorting later



