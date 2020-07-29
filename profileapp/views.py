from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfilePost
from django.utils import timezone



def upload(request):
    return render(request,'upload.html')

def upload_create(request):
    form=Profile()
    form.title=request.POST['title']
    form.body=request.POST['body']
    try:
        form.image=request.FILES['image']
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
    return redirect('/profileapp/profile/')

def profile(request):
    profile=Profile.objects.all()
    return render(request,'profile.html',{'profile':profile})



def upload_form(request):
    if request.method =='POST': #POST방식으로 요청이 들어왔을 때 - form에 입력받은 데이터를 저장하기
        form = ProfilePost(request.POST,request.FILES) #입력된 내용들을 form이라는 변수에 저장
        if form.is_valid(): #form이 유효하다면(=models.py에 정의한 필드에 맞다면)
            post = form.save(commit=False) #form 데이터를 가져온다.-> 날짜랑 사용자를 넣어줘야 하니까!
            post.pub_date=timezone.now()
            post.save()
            return redirect('/profileapp/profile/')
    else:
        forms = ProfilePost()
        return render(request,'upload_form.html',{'form':forms})
