from sentence_transformers import SentenceTransformer
import umap
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import seaborn as sns


formulas = []
with open("formulas.csv", "r") as f:
    for row in list(f)[1:10]:
        formulas.append(row.strip())

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(formulas)
print("Formulas encoded")


sns.set(context="paper", style="white")

fig, ax = plt.subplots(figsize=(1, 1))
plt.scatter(embeddings[:, 0], embeddings[:, 1], cmap="Spectral", s=1)
plt.setp(ax, xticks=[], yticks=[])

plt.show()
