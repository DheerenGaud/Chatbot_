from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

bot=ChatBot('chatbot',read_only=False,logic_adapters=['chatterbot.logic.BestMatch',
                                                      'chatterbot.logic.MathematicalEvaluation',
                                                      'chatterbot.logic.TimeLogicAdapter'])

list_to_train =[
    "hi",
    "hi,Mathew",
    "What's your name?",
    "I'm just a chatbot",
]

# list_trainer=ListTrainer(bot)
# list_trainer.train(list_to_train)
# Create your views here.
def home(req):
     return  render(req,'blog/index.html')
def article(req,article_id):
     return render(req,'blog/index.html',{"article_id":article_id});
def getResponse(request):
     print(list_to_train)
     userMessage= request.GET.get("userMessage")
     # if(userMessage=="ganesh"):
          #     return HttpResponse(chatResponse)
     #       list_to_train.append("rollNo")
     #       list_to_train.append("5021115")
     #       list_to_train.append("name")
     #       list_to_train.append("Dheeren Gaud")
     #       list_to_train.append("collage")
     #       list_to_train.append("Fcrit")
     # list_trainer.train(list_to_train)
     chatResponse= str(bot.get_response(userMessage))
     return HttpResponse(chatResponse)

def SpecialQuery(request):
     print("hellow")
     Query= request.GET.get("specialQuery")
     print(Query)
     return  HttpResponse(Query)