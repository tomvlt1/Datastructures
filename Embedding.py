from transformers import AutoTokenizer, AutoModel
import torch

def TakeFields(person1, person2):
    #we want to verify that the input is a string
    if all(isinstance(x, str) for x in person1) and all(isinstance(x, str) for x in person2):
        return Embedding(person1, person2)
    else:
        return "Please enter valid strings"


def Embedding(person1, person2):
    # we are going to do text embeddings for the two persons to see how close they in terms of "interest"
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    # we are importing the model and tokenizer from the huggingface library
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
    return (sum(interest)/len(interest)) #we are averaging out the cosine similarity of the two persons for sorting later



