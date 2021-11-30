# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello world !")


from django.shortcuts import render
 
def hello(request):
    context = {}
    context['hello'] = 'Hello World2!'
    return render(request, 'testHello.html', context)
