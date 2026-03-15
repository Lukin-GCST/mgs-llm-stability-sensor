import numpy as np
from sentence_transformers import SentenceTransformer

ANCHOR_POINTS = [
    "logic", "order", "consistency", "structure", "truth", "stability"
]

class MGSSensor:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.anchor_embeddings = self.model.encode(ANCHOR_POINTS, convert_to_tensor=True)

    def analyze(self, text):
        embedding = self.model.encode([text], convert_to_tensor=True)
        resonances = np.dot(embedding, self.anchor_embeddings.T).flatten()
        mean_res = np.mean(resonances)
        std_res = np.std(resonances)
        epsilon = 1e-6
        g_index = mean_res / (std_res + epsilon)
        
        if g_index < 0.8:
            status = "CHAOS"
        elif 0.8 <= g_index <= 1.2:
            status = "STABLE"
        else:
            status = "DOGMA"
        
        return {
            "text": text,
            "g_index": round(float(g_index), 4),
            "status": status
        }
