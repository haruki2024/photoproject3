from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    
    class Meta:
        
        # 連携するUserモデルを設定
        model = PhotoPost
        # フォームで使用するフィールドを設定
        # ユーザー名、メールアドレス、パスワード、パスワード(確認用)
        fields = ['category', 'title', 'comment', 'image1','image2']