# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello world !")


from django.shortcuts import render
 
def hello(request):
    context = {}
    context['hello'] = 'Hello World2!'
    return render(request, 'testHello.html', context)


def testEcharts1(request):
    return render(request, 'testEcharts1.html')

def test_axis_arrow(request):
    return render(request, 'test_axis_arrow.html')
