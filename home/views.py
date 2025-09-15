from django.shortcuts import render


def index(request):
    template_data = {}
    template_data['title'] = 'Game Swap'
    return render(request, 'home/index.html',{'template_data': template_data})
def about(request):
    return render(request, 'home/about.html')