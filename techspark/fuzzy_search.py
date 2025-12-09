from rapidfuzz import fuzz


def fuzzy_similarity(s1: str, s2: str):
    """
    Token-based fuzzy similarity using RapidFuzz.
    Returns float in [0, 1].
    """
    # token_set_ratio gives excellent performance on messy text
    score = fuzz.token_set_ratio(s1, s2)
    return score / 100.0


if __name__ == "__main__":
    s1 = "Waterjet Cutter"
    s2 = "Laser Cutter"
    similarity = fuzzy_similarity(s1, s2)
    print(similarity)