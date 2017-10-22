categories = {
    'Bills': {'r': 252, 'g': 45, 'b': 121},
    'Shopping': {'r': 252, 'g': 182, 'b': 53},
    'Food & Dining': {'r': 17, 'g': 205, 'b': 197},
    'Travel': {'r': 74, 'g': 144, 'b': 226},
    'Health & Fitness': {'r': 17, 'g': 205, 'b': 197},
    'Unknown': {'r': 193, 'g': 193, 'b': 193}
}

def cat_to_color(category):
    return categories.get(category, categories['Unknown'])
