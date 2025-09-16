from django.shortcuts import render

games = [
    {
        'id': 1, 'name': 'Battlefield 2042', 'price': 1,
        'description': 'Literally the worst FPS ever.'
    },
    {
        'id': 2, 'name': 'PUBG', 'price': 25,
        'description': 'Battle royale and
        the battle for resources.'
    },
    {
        'id': 3, 'name': 'The Dark Knight', 'price': 14,
        'description': 'Gothams vigilante faces the Joker.'
    },
    {
        'id': 4, 'name': 'Halo 3', 'price': 11,
        'description': 'Masterchief saves humanity once again.',
    },
]
def index(request):
    template_data = {}
    template_data['title'] = 'Games'
    template_data['movies'] = games
    return render(request, 'games/index.html',
                  {'template_data': template_data})









]