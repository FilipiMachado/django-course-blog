from django.shortcuts import render

# Create your views here.


def index(request):
    meetups = [
        {
          'title': 'First Meetup',
          'location': 'New York',
          'slug': 'first-meetup'
        },
        {
          'title': 'Second Meetup',
          'location': 'Paris',
          'slug': 'second-meetup'
        },
    ]

    return render(request, 'meetups/index.html', {
        'meetups': meetups,
        'show_meetups': True
    })

def meetup_details(request, meetup_slug):
    selected_meetup = {'title': 'First Meetup', 'description': 'This is the first meetup'}
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })