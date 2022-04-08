from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from first_app.models import Book
from rested.serializers import BookSerializer


class IndexAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'message': f'Hello {request.user}'}, status=200)


class BookAPI(APIView):
    def get(self, request, book_pk):
        book = get_object_or_404(klass=Book, pk=book_pk)
        book_serializer = BookSerializer(instance=book)
        return Response(book_serializer.data)

    def put(self, request, book_pk):
        book = get_object_or_404(klass=Book, pk=book_pk)
        book_serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response({'message': 'Successfully changed book', 'book': book_serializer.data})
        else:
            return Response({'message': 'There was an error', 'book': book_serializer.errors})
