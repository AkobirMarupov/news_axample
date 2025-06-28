from django.contrib import admin
from news.models import Category, News, MediaFile, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  

    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'is_published', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'category', 'created_at')
    search_fields = ('title', 'content', 'author__email', 'category__name')
    prepopulated_fields = {'slug': ('title',)} 
    raw_id_fields = ('author', 'category') 



@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_type', 'file')
    search_fields = ('file_type',)
    filter_horizontal = ('news',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    filter_horizontal = ('news',)

