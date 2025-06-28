from modeltranslation.translator import register, TranslationOptions
from .models import Category, News, Tag


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)
