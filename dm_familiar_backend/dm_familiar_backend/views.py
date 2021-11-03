from django.shortcuts import render
import pyrebase
from .local_settings import FIREBASE_CONFIG


firebase=pyrebase.initialize_app(FIREBASE_CONFIG)
authe = firebase.auth()
database=firebase.database()
 
def home(request):
    day = database.child('Test').child('Day').get().val()
    id = database.child('Test').child('Id').get().val()
    projectname = database.child('Test').child('ProjectName').get().val()
    return render(request,"home.html",{"day":day,"id":id,"projectname":projectname })