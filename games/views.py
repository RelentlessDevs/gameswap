from django.shortcuts import render

# Create your views here.
games = [
    {
        'id': 1, 'name': 'Halo 3', 'price': 20,
        'description': 'An adrenaline inducing space adventure to save humans.'
    },
    {
        'id':2, 'name': 'PUBG', 'price': 15,
        'description': 'The original battle royale'
    },
    {
        'id': 3, 'name': 'Minecraft', 'price': 24,
        'description': ' The most popular sandbox survival game.'
    },
    {
        'id': 4, 'name': 'Arkam Asylum', 'price': 10,
        'description': 'Play as the Dark Knight himself in this thrilling epic'
    },
]
def index(request):
    return render(request, "games/index.html")
    template_data = {}
    template_data['title'] = 'Games'
    template_data['games'] = 'games'
    return render(request, 'games/index.html',
    {'template_data': template_data})