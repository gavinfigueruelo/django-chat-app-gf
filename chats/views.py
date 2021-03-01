from django.shortcuts import render

# Create your views here.
class ChatAppListView(generics.ListAPIView):
    queryset = ChatApp.objects.all()
    serializer_class = ChatAppSerializer

class ChatAppDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser | IsOwnerOrReadOnly,)
    queryset = ChatApp.objects.all()
    serializer_class = ChatAppSerializer

class ChatAppCreateView(generics.CreateAPIView):
    queryset = ChatApp.objects.all()
    serializer_class = ChatAppSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ChatAppUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAdminUser | IsOwnerOrReadOnly,)
    queryset = ChatApp.objects.all()
    serializer_class = ChatAppSerializer

class ChatAppDestroyView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAdminUser | IsOwnerOrReadOnly,)
    queryset = ChatApp.objects.all()
    serializer_class = ChatAppSerializer

class RoomView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser | IsOwnerOrReadOnly,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
