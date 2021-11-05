from django.shortcuts import render
from django.http.response import Http404
from .serializers import BookSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
# Create your views here.


class ProjectList(APIView):


    def get(self, request):
        project_list = []
        docs = db.collection(u'Projects').stream()
        for doc in docs:
            project_list.append(doc.to_dict())
        serializer = ProjectSerializer(project_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            db.collection('Projects').document(request.data.get("name")).set(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Project(APIView):


    def get(self, request, ProjectId):
        doc_ref = db.collection(u'Projects').document(ProjectId)

        doc = doc_ref.get()
        if doc.exists:
            serializer = ProjectSerializer(doc.to_dict())
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, ProjectId):
        doc_ref = db.collection(u'Projects').document(ProjectId)
        doc_ref.update(request.data)

        doc = doc_ref.get()
        if doc.exists:
            serializer = ProjectSerializer(doc.to_dict())
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class BookList(APIView):
    
    
    def get(self, request, ProjectId):
        book_list = []
        docs = db.collection(u'Projects').document(ProjectId).collection(
                u'Books').stream()

        for doc in docs:
            book_list.append(doc.to_dict())
        serializer = BookSerializer(book_list, many=True)
        return Response(serializer.data)

    def post(self, request, ProjectId):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            db.collection('Projects').document(ProjectId).collection(
                'Books').document(request.data.get("title")).set(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class Book(APIView):


    def get(self, request, ProjectId, BookId):
        doc_ref = db.collection(u'Projects').document(ProjectId).collection(
            u'Books').document(BookId)


        doc = doc_ref.get()
        if doc.exists:
            serializer = BookSerializer(doc.to_dict())
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, ProjectId, BookId):
        doc_ref = db.collection(u'Projects').document(ProjectId).collection(
            u'Books').document(BookId)
        doc_ref.update(request.data)

        doc = doc_ref.get()
        if doc.exists:
            serializer = BookSerializer(doc.to_dict())
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)