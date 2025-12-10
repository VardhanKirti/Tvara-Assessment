from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/e5-small-v2")

sentences = [
    "That is a happy person",
    "That is a happy dog",
    "That is a very happy person",
    "Today is a sunny day",
    "I am a very happy person but sometimes I get sad"

]
embeddings = model.encode(sentences)

similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [4, 4]