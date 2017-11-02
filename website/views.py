from django.shortcuts import render
def homepage(request):
      return render(request, "website/Homepage.html")
      #return HttpResponse("<h1>Welcome to the page user!</h1>")
