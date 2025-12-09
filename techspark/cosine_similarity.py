import numpy as np


def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)

    if v1.shape != v2.shape:
        raise ValueError("Vectors must have the same shape")

    dot = np.dot(v1, v2)
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)

    if mag1 == 0 or mag2 == 0:
        return 0.0

    similarity = dot / (mag1 * mag2)
    similarity_normalized = (similarity + 1) / 2
    return similarity_normalized


if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [-4, -5, -6]
    similarity = cosine_similarity(v1, v2)
    print(similarity)