from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Heptities
import math
import random

# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request,"home.html")
def login(request):
    if request.method=="POST":
        first=request.POST['usname']
        password=request.POST['password1']
        User=auth.authenticate(username=first,password=password)
        if User is not None:
            auth.login(request,User)
            return HttpResponseRedirect('form')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    return render(request,"login.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def doctor(request):
    return render(request,"doctor.html")

def register(request):
    if request.method=="POST":
        first=request.POST['Username']
        Password=request.POST['Password']
        Paswrd=request.POST['passe']
        email=request.POST['EmailID']   
        if Password==Paswrd:
            if User.objects.filter(username=first).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exists")
                return render(request,"register.html")
            else:
                 u=User.objects.create_user(username=first,password=Password,email=email)
                 u.save()
                 return HttpResponseRedirect('login')
        else:
            messages.info(request,"Password Not Matching")
            return render(request,"register.html")
    else:
        return render(request,"register.html")   
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def hepatitisdata(request):
    Hepti=Heptities.objects.all()
    return render(request,"Heptities.html",{"Hepti":Hepti})

def form(request):
    if request.method=="POST":
        #n=int(request.POST['Category'])
        p=int(request.POST['Age'])
        q=request.POST['sex']
        r=int(request.POST['ALB'])
        s=int(request.POST['ALP'])
        t=int(request.POST['ALT'])
        u=int(request.POST['AST'])
        v=int(request.POST['BIL'])
        w=int(request.POST['CHE'])
        b=int(request.POST['CHOL'])
        c=int(request.POST['CREA'])
        z=int(request.POST['GGT'])
        a=int(request.POST['PROT'])
        from sklearn.preprocessing import LabelEncoder
        l=LabelEncoder()
        q1=l.fit_transform([q])
        import pandas as pd
        df=pd.read_csv(r"patient/static/dataset/HepatitisCdata.csv")
        print(df.head())
        print(df.isnull().sum())
        print(df.dropna(inplace=True))
        gen=l.fit_transform(df['Sex'])
        df=df.drop('Sex',axis=1)
        df["Sex"]=gen
        import matplotlib.pyplot as plt
        import seaborn as sns
        plt.bar(df["Age"],df["Category"],color="purple")
        plt.show()
        x=df[["Age","Sex","ALB","ALP","ALT","AST","BIL","CHE","CHOL","CREA","GGT","PROT"]]
        print(x.dropna(inplace=True))
        y=df["Category"]
        print(y.dropna(inplace=True))
        from sklearn.linear_model import LogisticRegression
        log=LogisticRegression()
        log.fit(x,y)
        import numpy as np
        X_test=np.array([[p,q1,r,s,t,u,v,w,b,c,z,a]],dtype=object)
        pred_Category=log.predict(X_test)
        print( pred_Category)
        c=Heptities.objects.create(Category=pred_Category,Age=p,Sex=q,ALB=r,ALP=s,ALT=t,AST=u,BIL=v,CHE=w,CHOL=b,CREA=c,GGT=z,PROT=a)
        return render(request,"predict.html",{"Category":pred_Category,"Age":p,"sex":q,"ALB":r,"ALP":s,"ALT":t,"AST":u,"BIL":v,"CHE":w,"CHOL":b,"CREA":c,"GGT":z,"PROT":a})
    return render(request,"form.html")
def predict(request):
    return render(request,"predict.html")


def welcome(request):
    return render(request,"welcome.html")