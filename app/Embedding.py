from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2") #we found these on hugging face (if i remember correctly)
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")#we found these on hugging face (if i remember correctly)

def TakeFields(person_data, target_data):
    
    if isinstance(person_data, str): #verifies if the input is a string
        person_data = [person_data]
    if isinstance(target_data, str):
        target_data = [target_data]

    
    if not person_data or not target_data: #the rating will be 0 if the data is empty
        return 0.0
    if not all(isinstance(x, str) for x in person_data + target_data):
        return 0.0

    
    return Embedding(person_data, target_data)

def Embedding(person_data, target_data):
    
    inputs1 = tokenizer(person_data, padding=True, truncation=True, return_tensors="pt") #tokenize each imput
    inputs2 = tokenizer(target_data, padding=True, truncation=True, return_tensors="pt")

    
    with torch.no_grad():
        outputs1 = model(**inputs1).last_hidden_state.mean(dim=1)
        outputs2 = model(**inputs2).last_hidden_state.mean(dim=1)

    
    similarity_scores = [] #we will store the similarity scores here
    for emb1 in outputs1: #we will compare each output to each other
        for emb2 in outputs2:
            cos_sim = torch.nn.functional.cosine_similarity(emb1.unsqueeze(0), emb2.unsqueeze(0))
            similarity_scores.append(cos_sim.item())

    
    return sum(similarity_scores) / len(similarity_scores) if similarity_scores else 0.0 #return the average of the similarity scores


if __name__ == "__main__":
    print(TakeFields(["Computer Science"], ["Data Science", "Computer Science", "Machine Learning"]))