from django.shortcuts import render 

def index(requests):
    return render(requests, 'index.html')


def second(requests):
    username = requests.GET['usertext']
    age =  requests.GET['age']
    email = requests.GET['email']
    return render(requests, 'second.html', {'username': username, 'age': age, 'email': email})
