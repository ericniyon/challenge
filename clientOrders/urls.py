from django.urls import path
from clientOrders import views

urlpatterns = [
    path('new-order/', views.CreateUserOrderView.as_view(), name='new_create'),
    path('list/', views.UserOrderListView.as_view(), name='list'),
    path('<int:id>', views.OrdersRetrieveUpdateDeleteView.as_view(), name='detail'),
]