from django.urls import path, include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter
'''
ViewSet не подключается как обычный класс-представление через метод .as_view()
для подключения viewset понадобится специальный роутер, он импортируется из rest_framework.routers
'''
router = DefaultRouter()
router.register('', ProductViewSet)
urlpatterns = [
    path('product/', include(router.urls))
    # path('products-list/', get_products) ,# Если вы пишете представление на функциях, вызывать их не нужно
    # path('products-cbv/', ProductListView.as_view()), # Если вы используете классовые представления, нужно обязательно вызвать метод as_view()
    # path('product-delete/<int:pk>/', ProductDeleteView.as_view()),
    # path('product-create/', ProductCreateView.as_view()),
    # path('product-partial-update/<int:pk>/', ProductUpdateView.as_view())
   ]
