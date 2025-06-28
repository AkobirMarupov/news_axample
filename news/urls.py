from django.urls import path


from news.api_endpoinds.Category.List.views import CategoryListGetAPIView, CategoryRetrieveAPIView


app_name = 'news'
urlpatterns = [
    path("category/list/", CategoryListGetAPIView.as_view(), name="category-list"),
    path("category/<int:pk>/", CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
]