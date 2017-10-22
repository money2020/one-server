categories = {
    'Bills': 'rgb(252, 45, 121)',
    'Shopping': 'rgb(252, 182, 53)',
    'Travel': 'rgb(193, 193, 193)',
    'Food & Dining': 'rgb(74, 144, 226)',
    'Health & Fitness': 'rgb(17, 205, 197)',
    'Services': 'rgb(252, 182, 53)',
    'Unknown': 'rgb(17, 205, 197)'
}

def cat_to_color(category):
    return categories.get(category, categories['Unknown'])
