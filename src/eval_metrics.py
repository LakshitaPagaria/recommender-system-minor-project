
def precision_at_k(recommended, relevant, k):
    """
    recommended: list of item ids (ranked)
    relevant: set of relevant item ids
    """
    recommended_k = recommended[:k]
    return len([r for r in recommended_k if r in relevant]) / k

def recall_at_k(recommended, relevant, k):
    recommended_k = recommended[:k]
    return len([r for r in recommended_k if r in relevant]) / max(1, len(relevant))
