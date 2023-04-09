from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from chatbot.models import Newevent
from chatbot.models import Collageinfo
from chatbot.models import Deparment
from django.shortcuts import redirect
from asgiref.sync import sync_to_async
import json



from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

bot=ChatBot('chatbot',read_only=False,logic_adapters=[ "chatterbot.logic.BestMatch",
                                                      'chatterbot.logic.MathematicalEvaluation',
                                                      'chatterbot.logic.TimeLogicAdapter'
                                                                        ])
# bot.storage.drop()
list_to_train= [
    "hi",
    "hi,Mathew",
    "What's your name?",
    "I'm just a chatbot",
]



list_trainer=ListTrainer(bot)

def restart():
      # event
       global list_to_train
       print(list_to_train)
       list_to_train=[];
       list_to_train=["hi","hi,Mathew","What's your name?","I'm just a chatbot"] 
       bot.storage.drop()
       data = list(Newevent.objects.values())
       p=[];
       for i in data:
            p.append(i['event'])  
       item={"type":'event',"button":p}
       list_to_train.append("event") 
       list_to_train.append(json.dumps(item)) 
       data = list(Newevent.objects.values())
       for x in data:
        list_to_train.append(x['event']) 
        a={"type":"Event","h2":x['event'],"p":x['discription'],"a":str(x['eventurl']),"h3":[{"Start at":str(x['eventstart']),"End at":str(x['eventend'])}]}
        list_to_train.append(json.dumps(a))
        
        
        
       #   collage
       col = list(Collageinfo.objects.values())
       b={"type":"Collage info","h1":col[0]['collagename'],"h3" :col[0]['achivment'],"p":col[0]['detail'],'a':col[0]['collageurl']}
       list_to_train.append('fcrit') 
       list_to_train.append(json.dumps(b))
       #  print(json.dumps(b)) 
      
      
      
      
       #department
       D = list(Deparment.objects.values())
       p=[];
       for i in D:
            p.append(i['department_name'])  
       item={"type":'Department info',"button":p}
       list_to_train.append('department') 
       list_to_train.append(json.dumps(item)) 
             
       for x in D:
        b={"type":"Department info","h1":x["department_name"],"h2":[{"HOD":x["department_hod_name"],"Fees":str(x["department_fees"])}],"h3":[{"Teaching Staff":str(x['department_teachingstaff']),"Non-Teaching Staff":str(x['department_nonteachingstaff'])}]}
        list_to_train.append(x['department_name']) 
        list_to_train.append(json.dumps(b))
      #  print(json.dumps(b))
      
      
      
      #training start
       list_trainer.train(list_to_train) 
       list_trainer.train(list_to_train) 
       list_trainer.train(list_to_train) 
       list_trainer.train(list_to_train) 
       list_trainer.train(list_to_train) 
       print(list_to_train)
       
         
       
# restart()       

def home(req):
     return  render(req,'blog/index.html')
def article(req,article_id):
     return render(req,'blog/index.html',{"article_id":article_id});
def getResponse(request):
     userMessage= request.GET.get("userMessage")
     if(userMessage=="event"):
      x= str(bot.get_response("event")) 
     elif(userMessage=="fcrit" or userMessage=="Collage info"):
      x= str(bot.get_response("fcrit")) 
     else:      
      x= str(bot.get_response(userMessage))
      print(userMessage)
      print(x)
     return HttpResponse(x)

def SpecialQuery(request):
     Query= request.GET.get("specialQuery")
     x= str(bot.get_response(Query))
     if(Query=="event"):
      x= str(bot.get_response("event")) 
     elif(Query=="fcrit" or Query=="Collage info"):
      x= str(bot.get_response("fcrit")) 
     print(x)
     return HttpResponse(x)


def Dashbord(request):
      return render(request,'blog/dashbord.html')


def Addevent(request):

      return render(request,'blog/addevent.html')

def Department(request):
      if(request.method=="POST"):
    
       department_name=request.POST.get("department_name")
       hod_name=request.POST.get("hod_name")
       teachingstaff=request.POST.get("teachingstaff")
       nonteachingstaff=request.POST.get("nonteachingstaff")
       fees=request.POST.get("fees")
       
       D = list(Deparment.objects.values())
       print(D)
       b={"type":"Department info","h1":D[0]["department_name"],"h2":[{"HOD":D[0]["department_hod_name"],"Fees":str(D[0]["department_fees"])}],"h3":[{"Teaching Staff":str(D[0]['department_teachingstaff']),"Non-Teaching Staff":str(D[0]['department_nonteachingstaff'])}]}
       list_to_train.append(D[0]['department_name']) 
       list_to_train.append(json.dumps(b))
       print(json.dumps(b))
       list_trainer.train(list_to_train) 
      
       depart,created = Deparment.objects.get_or_create(department_name=department_name)
       if created:
          created.department_name=department_name
          created.department_hod_name=hod_name
          created.department_teachingstaff=teachingstaff
          created.department_nonteachingstaff=nonteachingstaff
          created.department_fees=fees
          created.save();
       else:
          depart.department_name=department_name
          depart.department_hod_name=hod_name
          depart.department_teachingstaff=teachingstaff
          depart.department_nonteachingstaff=nonteachingstaff
          depart.department_fees=fees
          depart.save();
       restart()
       return render(request,'blog/department.html')
      return render(request,'blog/department.html')


def Collage(request):
      mathew = Collageinfo.objects.filter()[:1].get()
      return render(request,'blog/collageinfo.html',{'mathew':mathew})


def addCollageinfo(request):
      Collageinfo.objects.all().delete()
      if(request.method=="POST"):
         collagename=request.POST.get("collagename")
         achivment=request.POST.get("achivment")
         collageurl=request.POST.get("url")
         detail=request.POST.get("detail")
         x=Collageinfo(collagename=collagename,achivment=achivment,collageurl=collageurl,detail=detail,)
         x.save()  
      restart()
      return  HttpResponse("hellow colage info in  is added")




def Addmission(request):
      return render(request,'blog/admission.html')

def Scholership(request):
      return render(request,'blog/scholership.html')



def Allevent(request):
      events=Newevent.objects.values()
      return render(request,'blog/allevent.html',{'events':events})

def AlleventActionEdit(request,x_id):
         events= Newevent.objects.get(id=x_id)
         if(request.method=="POST"):
             events.event=request.POST.get("event")
             events.eventurl=request.POST.get("eventurl")
             events.eventstart=request.POST.get("eventstart")
             events.discription=request.POST.get("discription")
             events.eventend=request.POST.get("eventend")
             events.eventlogo=request.POST.get("eventlogo")
             events.save();
             restart();
             x=Newevent.objects.values()
             return render(request,'blog/allevent.html',{'events':x})
         return render(request,'blog/addevent.html',{'events':events})
            
def AlleventActionDelete(request,x_id):
            
            Newevent.objects.get(id=x_id).delete()
            sync_to_async(restart())
            events=Newevent.objects.values()
            return render(request,'blog/allevent.html',{'events':events})
      
      
def newEvent(request):
       if(request.method=="POST"):
         event=request.POST.get("event")
         eventurl=request.POST.get("eventurl")
         eventstart=request.POST.get("eventstart")
         discription=request.POST.get("discription")
         eventend=request.POST.get("eventend")
         eventlogo=request.POST.get("eventlogo")
         x=Newevent(event=event,eventurl=eventurl,eventstart=eventstart,discription=discription,eventend=eventend,eventlogo=eventlogo)
         sync_to_async(x.save())
         sync_to_async(restart())
       events=Newevent.objects.values()
       
       return render(request,'blog/allevent.html',{'events':events})




