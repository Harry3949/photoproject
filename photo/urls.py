from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

# URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
    #写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    #投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    #カテゴリ一覧ページ
    #photos/<Categorysテーブルのid値>にマッチング
    #<int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name = 'photos_cat'),
    #ユーザーの投稿一覧ページ
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'
         ),
    #詳細ページ
    path('photo-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'photo_detail'
         ),
    path('mypage/',
         views.MypageView.as_view(),
         name='mypage'),
    #写真の削除
    path('photo/<int:pk>/delete',
         views.PhotoDeleteView.as_view(),
         name = 'photo_delete'),
]