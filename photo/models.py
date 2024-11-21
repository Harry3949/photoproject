from django.db import models
#accountsアプリのmodelsモジュールからCustomUserインポート
from accounts.models import CustomUser

class Category(models.Model):
    #カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )
    def __str__(self):
        return self.title

class PhotoPost(models.Model):
    #CustomUserが親でPhotoPostがこの関係
    user = models.ForeignKey(
        CustomUser,
        #フィールドタイトル
        verbose_name='ユーザー',
        #ユーザーを消去する場合、ユーザーの投稿データもすべて消去
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリー',
        on_delete=models.PROTECT
    )
    #タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    #コメント用
    comment = models.TextField(
        verbose_name='コメント',
    )
    #イメージ１用
    #データベースに画像読み込ますため。
    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to='photos'
    )
    #イメージ２用
    image2 = models.ImageField(
        verbose_name='イメージ２',
        upload_to='photos',
        blank=True,
        null=True)
    #投稿日時フィールド
    posted_at = models.DateField(
        verbose_name='投稿日時',
        auto_now_add=True,
    )
    
    def __str__(self):
        return self.title