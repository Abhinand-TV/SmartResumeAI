def final_score(similarity, skill_score):
    return round(0.5 * similarity + 0.5 * skill_score, 2)