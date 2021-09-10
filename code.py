from flask import Flask
import requests
app = Flask(_name_)
@app.route('alerts/create/', methods=['GET', 'POST'])
def createAlert(request):
    if(request.method=='POST'):
        coinToAlert=request.json['name']
        alertPrice=request.json['alertPrice']
        try:
            with open("coins.txt",'a',encoding = 'utf-8') as f:
                f.write(str(coinToAlert))
        except Exception as e:
            return e
    return "Alert Created"
@app.route('alerts/delete/', methods=['GET', 'POST'])
def deleteAlert():
    if(request.method=='POST'):
        coinToAlert=request.json['name']
        try:
            f=open('coins.txt','r')
            s=f.readlines()
            s=[i for i in s if(i==coinToAlert)]
            with open("coins.txt",'w',encoding = 'utf-8') as f:
                for i in s:
                    f.write(i)
        except Exception as e:
            return e
    return "Alert Deleted"

@app.route('alerts/delete/', methods=['GET', 'POST'])
def listAlert():
    l=''
    if(request.method=='GET'):
        try:
            f=open('coins.txt','r')
            s=f.readlines()
            l="\n".join(s)
        except Exception as e:
            return e
    return
