from django import forms
from .models import Profile

class ProfilePost(forms.ModelForm):
    class Meta:
        model = Profile # 어떤 모델을 기반으로 한 입력공간이니?
        fields = ['title','body','image']

    def __init__(self,*args,**kwargs): 
        #*args : 복수의 인자를 받고자 할 때, *뒤 변수명을 적으면 된다. 
        #**kwargs : 여러 키워드 파라미터를 받을 수 있다(ex- x=10 과 같은!).   
        super().__init__(*args,**kwargs)
        #super()을 이용해 부모클래스의 내용을 가지고 올 수 있다.=> 오버라이딩 즉 Blogapp 내용에 접근!
        self.fields['title'].label="제목"
        self.fields['body'].label="본문"
        self.fields['image'].lable="사진"
        self.fields['title'].widget.attrs.update({
            'class' : 'title_class',
            'placeholder':'제목을 입력하세요',
        })