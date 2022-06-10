from django.shortcuts import render
from django.contrib.auth import get_user_model
from chats.models import ChatModel
import pickle


#models
model=pickle.load(open('svheart.pkl','rb'))
model1=pickle.load(open('liver.pkl','rb'))
model2=pickle.load(open('diabetes.pkl','rb'))
model3=pickle.load(open('kidney.pkl','rb'))


User = get_user_model()

#homepage
def homepage(request):
    return render(request, 'home.html')
    
#chat Homepage
def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={'users': users})



def diabetes(request):
    return render(request,'diabetes.html')
def options(request):
    return render(request,'options.html')

def appointment(request):
    return render(request,'appointment.html')

def predict2(request):
    p=request.GET['Pregnancies']
    pp=request.GET['Present_Price']
    bp=request.GET['BloodPressure']
    bm=request.GET['BMI']
    dp=request.GET['DiabetesPedigreeFunction']
    ag=request.GET['Age']
    pred=model2.predict([[p,pp,bp,bm,dp,ag]])

    pred=pred[0]
    return render(request,'result2.html',{'pred':pred})


def liver(request):
    return render(request,'liver.html')

def predict1(request):
    age=request.GET['Age']
    sex=request.GET['Sex']
    if sex=='1':
        sex=1
    elif sex=='0':
        sex=0
    tb=request.GET['Total Bilirubin']
    db=request.GET['Direct_Bilirubin']
    ap=request.GET['Alkaline_Phosphotase']
    aa=request.GET['Alamine_Aminotransferase']
    asa=request.GET['Aspartate_Aminotransferase']
    tp=request.GET['Total_Protiens']
    a=request.GET['Albumin']
    ag=request.GET['Albumin_and_Globulin_Ratio']
    pred=model1.predict([[age,sex,tb,db,ap,aa,asa,tp,a,ag]])

    pred=pred[0]
    return render(request,'result1.html',{'pred':pred})
  


def kidney(request):
    return render(request,'kidney.html')

def predict3(request):
    bp=request.GET['bp']
    sg=request.GET['sg']
    al=request.GET['al']
    su=request.GET['su']
    rbc=request.GET['rbc']
    pc=request.GET['pc']
    pcc=request.GET['pcc']
    pred=model3.predict([[bp,sg,al,su,rbc,pc,pcc]])

    pred=pred[0]
    return render(request,'result3.html',{'pred':pred})

def brain(request):
    return render(request,'brain.html')

def heart(request):
    return render(request,'heart.html')

def predict(request):
    age=request.GET['age']
    sex=request.GET['sex']
    if sex=='0':
        sex=0
    elif sex=='1':
        sex=1
    cpt=request.GET['cp']
    if cpt=='0':
        cpt=0
    elif cpt=='1':
        cpt=1
    elif cpt=='2':
        cpt=2
    elif cpt=='3':
        cpt=3
    tps=request.GET['trestbps']
    chol=request.GET['chol']
    fbs=request.GET['fbs']
    if fbs=='0':
        fbs=0
    elif fbs=='1':
        fbs=1
    restecg=request.GET['restecg']
    if restecg=='0':
        restecg=0
    elif restecg=='1':
        restecg==1
    elif restecg=='2':
        restecg=2
    thalach=request.GET['thalach']
    exang=request.GET['exang']
    if exang=='0':
        exang=0
    elif exang=='1':
        exang=1
    oldpeak=request.GET['oldpeak']
    slope=request.GET['oldpeak']
    if oldpeak=='0':
        oldpeak=0
    elif oldpeak=='1':
        oldpeak=1
    elif oldpeak=='2':
        oldpeak=2
    ca=request.GET['ca']
    if ca=='0':
        ca =0
    elif ca=='1':
        ca=1
    elif ca=='2':
        ca=2
    elif ca=='3':
        ca==3
    thal=request.GET['thal']
    if thal=='0':
        thal=0
    elif thal=='1':
        thal=1
    elif thal=='2':
        thal=2
    age_cat=request.GET['age_category']
    if age_cat=='0':
        age_cat=0
    elif age_cat=='1':
        age_cat=1
    elif age_cat=='2':
        age_cat=2

    pred=model.predict([[age,sex,cpt,tps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,age_cat]])
    pred=pred[0]
    print(pred)
    return render(request,'result.html',{'pred':pred})









def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    print(user_obj)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})
