from sentence_transformers import SentenceTransformer
import chromadb
model=SentenceTransformer("all-MiniLM-L6-V2")
with open("ai_sample.text","r") as file:
    text = file.read()
#print(text)
#text = file.readlines(),file.readline()
#print("No.of characters :",len(text))
chunks = []
chunk_size = 25
chunk_overlap = 10
step = chunk_size - chunk_overlap
for i in range(0,len(text),step):
    chunk = text[i:i+chunk_size] #(0,265,10) 
    chunks.append(chunk) #text[10:20]
#print("No.of chunks :",len(chunks))
#for i in range(0,len(chunks)):
    #print("chunk -" ,i,":",chunks[i])
    #print(f"Chunk{i}->{chunks[i]}")
#Embedding
embeddings=model.encode(chunks)
#print("embeddings created successfully")
print(embeddings.shape)

#chroma db

client=chromadb.Client()
collection=client.create_collection(name="my_documents")
print("collection creeated successfully")
ids=[]
for i in range(len(chunks)):
    ids.append(str(i))
collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist()

)
print("no of items collections:",collection.count())
results=collection.get()
for i in range(len(results["ids"])):
    print(f"ID:{results['ids'][i]}->chunk:{results['documents'][i]}")

chunk1=collection.get(ids=['0',])
print("chunk 1:",chunk1)