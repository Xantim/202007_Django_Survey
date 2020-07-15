from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request,"index.html")

def create_user(request):
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['message'] = request.POST['message']
    
    context = {
    	"name_on_template" : request.session['name'],
    	"email_on_template" : request.session['email'], 
        'language_on_template' : request.session['language'],
        'location_on_template' : request.session['location'],
        'message_on_template' : request.session['message'],
    }
   
    return redirect('/result')   

def result(request):
    #this is the success route
    return render(request,'result.html') 
      