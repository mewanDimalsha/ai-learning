# from sentence_transformers import SentenceTransformer, util

# model = SentenceTransformer("all-MiniLM-L6-v2")

# sentences = [
#     "The cat sits outside",
#     "A man is playing guitar",
#     "The feline is resting outdoors",
# ]

# embeddings = model.encode(sentences)

# # print(f"Embedding for Sentence A (first 10 numbers): \n{embeddings[0][:10]}...")
# # print(f"Total dimensions: {len(embeddings[0])}\n")

# # (This measures the angle between vectors: 1.0 is identical, 0 is unrelated)
# sim_A_C = util.cos_sim(embeddings[0], embeddings[2])
# sim_A_B = util.cos_sim(embeddings[0], embeddings[1])

# print(f"Similarity between 'Cat' and 'Feline': {sim_A_C.item():.4f}")
# print(f"Similarity between 'Cat' and 'Guitar': {sim_A_B.item():.4f}")

document = """
RAG stands for Retrieval Augmented Generation.
It solves the problem of LLMs not knowing recent information.
First you chunk your documents into smaller pieces.
Then you embed each chunk into a vector.
Then you store vectors in a vector database.
When a user asks a question you embed the question too.
You find the closest chunks to the question.
You send those chunks to the LLM as context.
The LLM answers using only that context.
"""


def chunk_text(text, chunk_size=2):
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    chunks = []
    # YOUR job: group sentences into pairs using range()
    # Hint: range(0, len(sentences), chunk_size)
    for x in range(0, len(sentences), chunk_size):
        chunk = ". ".join(sentences[x : x + chunk_size]) + "."
        chunks.append(chunk)
    return chunks


print(chunk_text(document))
