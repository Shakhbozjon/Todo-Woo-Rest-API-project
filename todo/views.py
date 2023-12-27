from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer


class TodoListApi(ListAPIView):
    # queryset = Todo.objects.filter(completed=False)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(status='current')


class TodoListCompletedApi(ListAPIView):
    # queryset = Todo.objects.filter(completed=True)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(status='completed')


class TodoDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_update(self, serializer):
        status = self.request.data.get('status', None)
        if status and status in ['completed', 'current']:
            serializer.save(status=status)
        else:
            serializer.save()


class TodoDeleteApi(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreateApi(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
