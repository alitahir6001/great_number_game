from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    return render(request, 'index.html')

def inspect(request):
    random_num = random.randint(1,100)
    print('This is the random number',random_num)
    request.session['number'] = request.POST['number']
    input = int(request.session['number'])

    if input > random_num:
        return redirect('/toohigh')
    elif input < random_num:
        return redirect('/toolow')
    else:
        return redirect('/exactly')

def toohigh(request):
    return HttpResponse("it's too high!")

def toolow(request):
    return HttpResponse("it's too low!")

def exactly(request):
    return HttpResponse("You got it!")

# returning a redirect to the respective "too high/too low" page is something i couldn't get to work properly, but returning it as an http response with the given string was the work around i thought of.  Not exactly a great game, but i was able to get the web app to function.