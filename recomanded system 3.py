import pandas as pd

data = {
    'Destination': ['Maldives', 'Swiss Alps', 'Paris', 'Bali', 'New York', 'Himalayas'],
    'Category': ['Beach', 'Mountain', 'City', 'Beach', 'City', 'Mountain']
}

df = pd.DataFrame(data)

def cosine_similarity(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    words1, words2 = set(str1.split()), set(str2.split())
    
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    
    return intersection / union if union != 0 else 0

def recommend_destinations(user_input, df):
    print(f"Your input category: {user_input}")
    
    sim_scores = []
    
   
    for idx, category in df['Category'].items():
        score = cosine_similarity(user_input, category)
        sim_scores.append((idx, score))
    
    sim_scores.sort(key=lambda x: x[1], reverse=True)
    
   
    recommended_indices = [score[0] for score in sim_scores if df['Category'][score[0]] != user_input]
    
    print("\nDestinations recommended for you:")
    for idx in recommended_indices[:2]:  
        print(f"- {df['Destination'][idx]} ({df['Category'][idx]})")

user_input = input("enter your preffed destination category (e.g., 'Beach','Mountain','city'): ")
recommend_destinations(user_input, df)
