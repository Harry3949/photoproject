from django.contrib import admin
#CustomUserをインポート
from .models import Category, PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    #レコード一覧にidとtitleを表示
    list_display = ('id','title')
    #表示するカラムにリンク設定
    list_display_links = ('id','title')
    
class PhotoPostAdmin(admin.ModelAdmin):
    #レコード一覧にidとtitleを表示
    list_display = ('id','title')
    #表示するカラムにリンクを設定
    list_display_links = ('id','title')
#Django管理サイトにCategory,CategoryAdminを登録
admin.site.register(Category, CategoryAdmin)
#Django管理サイトにPhotoPost、PhotoPostAdminを登録
admin.site.register(PhotoPost, PhotoPostAdmin)