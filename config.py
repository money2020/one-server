from utils import cat_to_color

token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwicGNrIjoxLCJhbGciOiJkaXIiLCJ0diI6Miwia2lkIjoiYTdxIn0..Q8EPUTo189PyagVaeXKw9XgvYN1pEz5Vgp1bgF4Hj9TE2anFkmGILcf7UX9iO6L0cUTgJQm3blatkUZUyUKc6cHFyyuVPKmtZDIU2zmP6VEhxmroUfeqh8YJnOEw9LRVKU1Pq4fVRuZMsIM1Mf6F2oMOAFL8JTw7AK4CQVUWtti4KHaNBtDX9cHOuwRtDbKhQbmySLP0g5ENzrC9gWMLprmq66hX5bI4TAiF2f7KlgjtT9lvph9pLyDsfBhtOanWj6gVmYMqxcNQlUHcgtsH3nlthX1PsOKQppDtmS09hPELzTxEn2kxk2btJ0KPy2iQFQyDSWfER1xgJnFDASr1sg8MNeQh3Qjmp4vuruQMimu1IFVvb1cIsIDS7cWPCUPa2UFYz9YfW1uXVnUpOyZTCWZ3E28YL70Rn2TbP4Hw030rgBWF5Ok1YD51e7BWJXXCq1lIWUG85WmjWZ5Il4nVNZBxBFDPR7lQMG2Gw36ibffzfTDwwHfWhlpkmbqtRLawKEVtYNDcpIvocujQJFHlwCRJ9uex5BXJzQQ6Mrp1cvxp3sp65mU5EPSU4J1OK0Iuj8Yv.I3YRuEIDtnqtHjjjrb9OK0A'


ICONS = {
    'fa-credit-card': '&#xf09d;',
}

SCAFFOLDING_OFFERS = [
    # {
    #     'id': 1,
    #     'title': 'Happy Birthday, Lucas! ***EXCLUSIVE***',
    #     'icon': '&#xf1fd;',
    #     'text': '$20 off Italianos, pay with pts',
    #     'category': 'Food & Dining',
    #     'subcategory': 'Restaurant',
    #     'color': cat_to_color('Food & Dining'),
    #     'target': 'lucas'
    # },

    # Lucas Offers
    {
        'id': 2,
        'title': 'Early Holiday Escape.',
        'icon': '&#xf236;',
        'text': '25% bonus pts at Hilton.',
        'expiration': '11/25/2017',
        'category': 'Travel',
        'subcategory': 'Hotels',
        'color': cat_to_color('Travel'),
        'target': 'lucas'
    },
    {
        'id': 3,
        'title': 'Refill your prescription.',
        'icon': '&#xf004;',
        'text': '+200 pts at CVS.',
        'expiration': '10/31/2017',
        'category': 'Health & Fitness',
        'subcategory': 'Health',
        'color': cat_to_color('Health & Fitness'),
        'target': 'lucas'
    },
    {
        'id': 4,
        'title': 'Fall Coffee is Here.',
        'icon': '&#xf0f4;',
        'text': 'FREE Pumpkin Spice at Starbucks.',
        'expiration': '11/11/2017',
        'category': 'Food & Dining',
        'subcategory': 'Coffee Shop',
        'color': cat_to_color('Food & Dining'),
        'target': 'lucas'
    },
    {
        'id': 5,
        'title': 'Gear up your camera for Christmas!',
        'icon': '&#xf030;',
        'text': '+1,000 pts, free shipping from B&H Photo.',
        'expiration': '12/1/2017',
        'category': 'Shopping',
        'subcategory': 'Electronics',
        'color': cat_to_color('Shopping'),
        'target': 'lucas'
    },

    # Tatiana Offers
    {
        'id': 6,
        'title': 'Beach time!',
        'icon': '&#xf236;',
        'text': '25% bonus pts at Cubana.',
        'expiration': '11/25/2017',
        'category': 'Travel',
        'subcategory': 'Hotels',
        'color': cat_to_color('Travel'),
        'target': 'tatiana'
    },
    {
        'id': 7,
        'title': 'Turkey Time?',
        'icon': '&#xf099;',
        'text': '+500 pts at Wholefoods.',
        'expiration': '11/30/2017',
        'category': 'Shopping',
        'subcategory': 'Groceries',
        'color': cat_to_color('Shopping'),
        'target': 'tatiana'
    },
    {
        'id': 8,
        'title': 'Let\'s Get Moving',
        'icon': '&#xf1bb;',
        'text': 'Stream Spotify hiking playlist.',
        'expiration': 'Fun never expires.',
        'category': 'Travel',
        'subcategory': 'Activities',
        'color': cat_to_color('Travel'),
        'target': 'tatiana'
    },
]