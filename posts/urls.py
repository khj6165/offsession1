from django.urls import path
from .views import main, new, create, show

app_name = "posts"
urlpatterns = [
    path('', main, name="main"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('/show/<int:id>', show, name="show"),
]
#id라는 이름으로, 타입 integer로 주소로 전달
#id를 views에서 받아야함