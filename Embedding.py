from transformers import AutoTokenizer, AutoModel
import torch

def TakeFields(person1, person2):
    
    if all(isinstance(x, str) for x in person1) and all(isinstance(x, str) for x in person2):
        return Embedding(person1, person2)
    else:
        return "Please enter valid strings"


def Embedding(person1, person2):
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    interest = []
    for i in person1:
        for j in person2:
            inputs1 = tokenizer(i, return_tensors="pt")
            inputs2 = tokenizer(j, return_tensors="pt")

            with torch.no_grad():
                outputs1 = model(**inputs1).last_hidden_state.mean(dim=1) 
                outputs2 = model(**inputs2).last_hidden_state.mean(dim=1)
            cos_sim = torch.nn.functional.cosine_similarity(outputs1, outputs2)
            interest.append(cos_sim.item())
    return (sum(interest)/len(interest))





