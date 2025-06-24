from .views import ThreadListView, ThreadDetailView, ThreadCreateView

urlpatterns = [
    path('', ThreadListView.as_view(), name='index'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    path('create/', ThreadCreateView.as_view(), name='create_thread'),
]