from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
from joblib import load
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#initializations
vanalyzer = SentimentIntensityAnalyzer()
clf = load('model19.joblib')
clf2 = load('agg.joblib')
vec = load('vec.joblib')
before1=[]
after1= []
name1 = ''
text1 = ''
emotions1 = ''
# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'home.html',{})
    #return HttpResponse('hello')
@csrf_exempt
def before(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'before.html', {})
@csrf_exempt
def index4(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index4.html', {})

@csrf_exempt
def index5(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index5.html', {})

@csrf_exempt
def privacy(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'privacy.html', {})

@csrf_exempt
def thankyou(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'thankyou.html', {})

@csrf_exempt
def add_to_db(request):
    global before1, after1, name1, text1, emotions1
    prolific = ''
    json_stuff= json.dumps({'start':'start db'})
    if request.POST.get('q_1','')!='':
        p1 =  request.POST.get('prolific', '')
        prolific = p1
        q1b = request.POST.get('q_1','')
        q2b = request.POST.get('q_2','')
        q3b = request.POST.get('q_3','')
        q4b = request.POST.get('q_4','')
        q5b = request.POST.get('q_5','')
        q6b = request.POST.get('q_6','')
        q7b = request.POST.get('q_7','')
        q8b = request.POST.get('q_8','')
        q9b = request.POST.get('q_9','')
        q10b = request.POST.get('q_10','')
        before1 = [p1,q1b,q2b,q3b,q4b,q5b,q6b,q7b,q8b,q9b,q10b]
        return redirect("/index4")
    if request.POST.get('name', False)!=False:
         name1 = request.POST.get('name', False)
         text1 = request.POST.get('text', False)
         emotions1 = request.POST.get('emotions', False)
         return redirect("/index5")
    if request.POST.get('question_9','')!='':#=="1":
         q1a = request.POST.get('question_1','')
         q2a = request.POST.get('question_2','')
         q3a = request.POST.get('question_3','')
         q4a = request.POST.get('question_4','')
         q5a = request.POST.get('question_5','')
         q6a = request.POST.get('question_6','')
         q7a = request.POST.get('question_7','')
         q8a = request.POST.get('question_8','')
         q10a = request.POST.get('question_10','')
         q11a = request.POST.get('question_11','')
         q12a = request.POST.get('question_12','')
         q13a = request.POST.get('question_13','')
         q14a = request.POST.get('question_14','')
         q15a = request.POST.get('question_15','')
         q16a = request.POST.get('question_16','')
         q17a = request.POST.get('question_17','')
         after1 = [q1a,q2a,q3a,q4a,q5a,q6a,q7a,q8a,q10a,q11a,q12a,q13a,q14a,q15a,q16a,q17a]
         #print(name1 + p1 + emotions1)
         user = User(name=name1, prolific = prolific, text=text1, emotions=emotions1, before=before1, after=after1)
         user.save()
         json_stuff = json.dumps({name1: [text1,emotions1]})
         return redirect("thankyou")
    return redirect("/#")
#logic
@csrf_exempt
def predict_aggression1(text,countvector,model):
    return model.predict(countvector.transform([text]))[0]

@csrf_exempt
def get_text(request):
    text = request.POST.get('text', False)
    emotion = 'get_text emotion'#text_emotion(text)
    aggression = 'get_text aggression' #agg_detection(text)
    emotion = extract_emotion(text)
    aggression = agg_detection(text)
    json_stuff = json.dumps({"list": ['no voice',emotion, aggression]})
    return HttpResponse(json_stuff, content_type="application/json")
@csrf_exempt
def agg_detection(text):
    prediction = predict_aggression1(text,vec,clf2)
    return prediction

@csrf_exempt
def vader_tone(text):
    vs = vanalyzer.polarity_scores(text)
    tone_name = "neutral"
    nuscore = vs['neu']
    negscore = vs['neg']
    posscore = vs['pos']
    score = vs['compound']
    if negscore > posscore and negscore > nuscore:
        tone_name = "negative"
    else:
        if posscore > negscore and posscore > nuscore:
            tone_name = "positive"
    return tone_name,score

@csrf_exempt
def extract_emotion(text):
    tone_name, score = vader_tone(text)
    return tone_name
