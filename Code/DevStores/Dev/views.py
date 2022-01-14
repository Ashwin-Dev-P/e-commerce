from django.shortcuts import render
from .models import dress,customer_review
from .models import *
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


dresses = dress.objects.all() 
first_dress = dresses.first()
last_dress = dresses.last()
customer_review_data = customer_review.objects.all()

def home(request):
    if(request.method == "GET"):
 	    return render(request,"index.html",{'title':'Dev Stores'})

def shop(request):
    if(request.method == "GET"):
        dresses = dress.objects.all() 
        return render(request,"shop.html",{'title':'Shop', 'dresses':dresses})
    
    

def view(request,id):
    
    if(request.method == "GET"):
        if(dresses.filter(id=id).exists() ):
            
            dress = dresses.filter(id=id).first()
            
            
            if(dress == first_dress):
                id_left = None
                print("First dress.");
            else:
                #This gets the previous id not the previous object.So change it
                id_left = id-1
                print("Last dress.")
            reviews = customer_review_data.filter(product_id = id)
            
            if(dress == last_dress):
                id_right = None
            else: 
                id_right = id+1          
            
            
            
                
                
            
            return render(request,"view.html",{'title':'view','dresses':dresses,'dress':dress,'reviews':reviews,'id_left':id_left,'id_right':id_right})
            
    elif(request.method == "POST"):
        review = request.POST['customerreview']
        product_id = id
        myform = customer_review(review=review,product_id=product_id)
        myform.save()
        dress = dresses.filter(id=id).first()
        reviews = customer_review_data.filter(product_id = id)
        return render(request,"view.html",{'title':'view','dress':dress,'reviews':reviews})
        
        
        
        
        
def sign_up(request):
    if(request.method == "GET"):
        return render(request,"sign_up.html",{'title':'Sign Up'})
    else:
        return render(request,"sign_up.html",{'title':'Sign Up'})