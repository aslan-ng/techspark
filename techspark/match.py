from techspark.fuzzy_search import fuzzy_similarity
from techspark.cosine_similarity import cosine_similarity


def match_items(input, items: list, threshold, num_results=None):
    """
    Match an input (string or embedding) against a list of items.

    Returns a list of dicts with `index`, `item`, and `score`, sorted by score
    (descending), filtered by the provided threshold, and capped at
    `num_results` (or all results if `num_results` is None).
    """
    if isinstance(input, str):
        score_function = fuzzy_similarity
    elif isinstance(input, list) or \
        isinstance(input, tuple):
        score_function = cosine_similarity
    else:
        raise ValueError("Input must be a string or a list/tuple of numbers.")
    

    scored_items = []
    for idx, item in enumerate(items):
        score = score_function(input, item)
        if score >= threshold:
            scored_items.append({
                "index": idx,
                "item": item,
                "score": score,
            })

    scored_items.sort(key=lambda x: x["score"], reverse=True)
    if num_results is None:
        return scored_items
    return scored_items[:num_results]


if __name__ == "__main__":
    items = ["apple", "banana", "grape", "pineapple"]
    input_str = "appl"
    matches = match_items(input_str, items, threshold=0.6)
    print(matches)
