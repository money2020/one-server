from utils import cat_to_color

token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwicGNrIjoxLCJhbGciOiJkaXIiLCJ0diI6Miwia2lkIjoiYTdxIn0..Q8EPUTo189PyagVaeXKw9XgvYN1pEz5Vgp1bgF4Hj9TE2anFkmGILcf7UX9iO6L0cUTgJQm3blatkUZUyUKc6cHFyyuVPKmtZDIU2zmP6VEhxmroUfeqh8YJnOEw9LRVKU1Pq4fVRuZMsIM1Mf6F2oMOAFL8JTw7AK4CQVUWtti4KHaNBtDX9cHOuwRtDbKhQbmySLP0g5ENzrC9gWMLprmq66hX5bI4TAiF2f7KlgjtT9lvph9pLyDsfBhtOanWj6gVmYMqxcNQlUHcgtsH3nlthX1PsOKQppDtmS09hPELzTxEn2kxk2btJ0KPy2iQFQyDSWfER1xgJnFDASr1sg8MNeQh3Qjmp4vuruQMimu1IFVvb1cIsIDS7cWPCUPa2UFYz9YfW1uXVnUpOyZTCWZ3E28YL70Rn2TbP4Hw030rgBWF5Ok1YD51e7BWJXXCq1lIWUG85WmjWZ5Il4nVNZBxBFDPR7lQMG2Gw36ibffzfTDwwHfWhlpkmbqtRLawKEVtYNDcpIvocujQJFHlwCRJ9uex5BXJzQQ6Mrp1cvxp3sp65mU5EPSU4J1OK0Iuj8Yv.I3YRuEIDtnqtHjjjrb9OK0A'


ICONS = {
    'fa-birthay-cake': '&#xf1fd;',
    'fa-camera': '&#xf030;',
    'fa-coffee': '&#xf0f4;',
    'fa-credit-card': '&#xf09d;',
    'fa-heart': '&#xf004;',
    'fa-hotel': '&#xf236;',
    'fa-tree': '&#xf1bb;',
    'fa-twitter': '&#xf099;',
}

SCAFFOLDING_OFFERS = [
    # {
    #     'id': 1,
    #     'title': 'Happy Birthday, Nick! ***EXCLUSIVE***',
    #     'icon': ICONS['fa-birthday-cake'],
    #     'text': '$20 off Italianos, pay with pts',
    #     'category': 'Food & Dining',
    #     'subcategory': 'Restaurant',
    #     'color': cat_to_color('Food & Dining'),
    #     'target': 'nick'
    # },

    # Lucas Offers
    {
        'id': 2,
        'title': 'Early Holiday Escape.',
        'icon': ICONS['fa-hotel'],
        'text': '25% bonus pts at Hilton.',
        'expiration': '11/25/2017',
        'category': 'Travel',
        'subcategory': 'Hotels',
        'color': cat_to_color('Travel'),
        'target': 'nick'
    },
    {
        'id': 3,
        'title': 'Refill your prescription.',
        'icon': ICONS['fa-heart'],
        'text': '+200 pts at CVS.',
        'expiration': '10/31/2017',
        'category': 'Health & Fitness',
        'subcategory': 'Health',
        'color': cat_to_color('Health & Fitness'),
        'target': 'nick'
    },
    {
        'id': 4,
        'title': 'Fall Coffee is Here.',
        'icon': ICONS['fa-coffee'],
        'text': 'FREE Pumpkin Spice at Starbucks.',
        'expiration': '11/11/2017',
        'category': 'Food & Dining',
        'subcategory': 'Coffee Shop',
        'color': cat_to_color('Food & Dining'),
        'target': 'nick'
    },
    {
        'id': 5,
        'title': 'Gear up your camera for Christmas!',
        'icon': ICONS['fa-camera'],
        'text': '+1,000 pts, free shipping from B&H Photo.',
        'expiration': '12/1/2017',
        'category': 'Shopping',
        'subcategory': 'Electronics',
        'color': cat_to_color('Shopping'),
        'target': 'nick'
    },

    # Tatiana Offers
    {
        'id': 6,
        'title': 'Beach time!',
        'icon': ICONS['fa-hotel'],
        'text': '25% bonus pts at Cubana.',
        'expiration': '11/25/2017',
        'category': 'Travel',
        'subcategory': 'Hotels',
        'color': cat_to_color('Travel'),
        'target': 'cathy'
    },
    {
        'id': 7,
        'title': 'Turkey Time?',
        'icon': ICONS['fa-twitter'],
        'text': '+500 pts at Wholefoods.',
        'expiration': '11/30/2017',
        'category': 'Shopping',
        'subcategory': 'Grocery',
        'color': cat_to_color('Shopping'),
        'target': 'cathy'
    },
    {
        'id': 8,
        'title': 'Let\'s Get Moving',
        'icon': ICONS['fa-tree'],
        'text': 'Stream Spotify hiking playlist.',
        'expiration': 'Fun never expires.',
        'category': 'Travel',
        'subcategory': 'Activities',
        'color': cat_to_color('Travel'),
        'target': 'cathy'
    },
]