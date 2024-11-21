from django.db.models.query import QuerySet
from django.shortcuts import render
# django.views.genericからTemplateView,ListViewをインポート
from django.views.generic import TemplateView,ListView
# CreateViewをインポート
from django.views.generic import CreateView
#reverse_lazyをインポート
from django.urls import reverse_lazy
#PhotoPostFormをインポート
from .forms import PhotoPostForm
#method_decoratorをインポート
from django.utils.decorators import method_decorator
#login_requiredをインポート
from django.contrib.auth.decorators import login_required
#PhotoPostをインポート
from .models import PhotoPost
#DetailViewをインポート
from django.views.generic import DetailView
#DeleteViewをインポート
from django.views.generic import DeleteView

class IndexView(ListView):
    # index.htmlをレンダリングする
    template_name ='index.html'
    #投稿日時の降順で並べ替え
    queryset = PhotoPost.objects.order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 9

#デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される。
#ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクト
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    #forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    #レンダリングするテンプレート
    template_name = "post_photo.html"
    #フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_done')
    
    def form_valid(self, form):
        #commit=Falseに対し、Postされたデータを取得
        postdata = form.save(commit=False)
        #投稿ユーザーのidを取得し、モデルのuserフィールドに格納
        postdata.user = self.request.user
        #投稿データをデータベースに登録
        postdata.save()
        #戻り値はスーパークラスのform_valid()の戻り値
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    #idex.htmlをレンダリング
    template_name = 'post_success.html'
    
class CategoryView(ListView):
    #index.htmlをレンダリング
    template_name='index.html'
    #1ページに表示するレコードの件数
    paginate_by = 9
    
    def get_queryset(self):
        #self.kwargsでキーワードの辞書を取得し、Categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category']
        #filterで絞り込む
        categories = PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        #クエリによって取得されたレコード返す
        return categories
class UserView(ListView):
    #index.htmlをレンダリング
    template_name='index.html'
    #1ページに表示するレコードの件数
    paginate_by = 9
    
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        #クエリによって取得されたレコード返す
        return user_list
    
class DetailView(DetailView):
    #post.htmlをレンダリングする
    template_name = 'detail.html'
    #クラス変数modelにモデルBlogPostを設定
    model = PhotoPost
    
class MypageView(ListView):
    #mypage.htmlをレンダリング
    template_name = 'mypage.html'
    #1ページに表示するレコードの件数
    pagenate_by = 9
    
    def get_queryset(self):
        #filter(userフィールド=userオブジェクトで絞り込み)
        queryset = PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class PhotoDeleteView(DeleteView):
    #操作の対象はPhotoPostモデル
    model = PhotoPost
    #photo_delete.htmlをレンダリングする
    template_name = 'photo_delete.html'
    #処理終了後にマイページにリダイレクト
    success_url = reverse_lazy('photo:mypage')
    
    def delete(self,request,*args,**kwargs):
        #スーパークラスのdelete()を実行
        return super().delete(request, *args,**kwargs)