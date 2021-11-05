from django.shortcuts import render
from django.http.response import Http404
from .serializers import BookSerializer, ChapterSerializer, ProjectSerializer, StaticAssetSerializer
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


    # Get All Projects
    def get(self, request):
        project_list = []
        docs = db.collection(u'Projects').stream()

        for doc in docs:
            project_list.append(doc.to_dict())
        serializer = ProjectSerializer(project_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create New Project
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            db.collection('Projects').document(request.data.get("name")).set(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Project(APIView):


    # Get Selected Project
    def get(self, request, ProjectId):
        doc_ref = db.collection(u'Projects').document(ProjectId)

        doc = doc_ref.get()
        if doc.exists:
            serializer = ProjectSerializer(doc.to_dict())
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    #Edit Project
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
    
    
    # Get All Books
    def get(self, request, ProjectId):
        book_list = []
        docs = db.collection(u'Projects').document(ProjectId).collection(
                u'Books').stream()

        for doc in docs:
            book_list.append(doc.to_dict())
        serializer = BookSerializer(book_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create Book
    def post(self, request, ProjectId):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            db.collection('Projects').document(ProjectId).collection(
                'Books').document(request.data.get("title")).set(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class Book(APIView):


    # Get Selected Book
    def get(self, request, ProjectId, BookId):
        doc_ref = db.collection(u'Projects').document(ProjectId).collection(
            u'Books').document(BookId)

        doc = doc_ref.get()
        if doc.exists:
            serializer = BookSerializer(doc.to_dict())
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Edit Book
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


class ChapterList(APIView):


    # Get All Chapters for that Book
    def get(self, request, ProjectId, BookId):
        chapter_list = []
        docs = db.collection(u'Projects').document(ProjectId).collection(
            u'Books').document(BookId).collection(u'Chapters').stream()

        for doc in docs:
            chapter_list.append(doc.to_dict())
        serializer = ChapterSerializer(chapter_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create New Chapter for that Book
    def post(self, request, ProjectId, BookId):
        serializer = ChapterSerializer(data=request.data)
        if serializer.is_valid():
            db.collection('Projects').document(ProjectId).collection(
                'Books').document(BookId).collection('Chapters').document(request.data.get("title")).set(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Chapter(APIView):


    # Get selected chapter of Book
    def get(self, request, ProjectId, BookId, ChapterId):
        doc_ref = db.collection(u'Projects').document(ProjectId).collection(
            u'Books').document(BookId).collection('Chapters').document(ChapterId)

        doc = doc_ref.get()
        if doc.exists:
            serializer = ChapterSerializer(doc.to_dict())
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Edit Chapter
    def patch(self, request, ProjectId, BookId, ChapterId):
        doc_ref = db.collection(u'Projects').document(ProjectId).collection(
            u'Books').document(BookId).collection('Chapters').document(ChapterId)
        doc_ref.update(request.data)

        doc = doc_ref.get()
        if doc.exists:
            serializer = ChapterSerializer(doc.to_dict())
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class StaticAssetList(APIView):


    # Get All Static Assets
    def get(self, request, ProjectId):
        static_list = []
        docs = db.collection(u'Projects').document(ProjectId).collection(u'StaticAssets').stream()

        for doc in docs:
            static_list.append(doc.to_dict())
        serializer = StaticAssetSerializer(static_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create New Static Assets
    def post(self, request, ProjectId):
        serializer = StaticAssetSerializer(data=request.data)
        if serializer.is_valid():
            db.collection('Projects').document(ProjectId).collection(
                u'StaticAssets').document(request.data.get("title")).set(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaticAsset(APIView):


    # Get selected Static Asset
    def get(self, request, ProjectId, StaticAssetId):
        doc_ref = db.collection(u'Projects').document(ProjectId).collection(
            u'StaticAssets').document(StaticAssetId)

        doc = doc_ref.get()
        if doc.exists:
            serializer = StaticAssetSerializer(doc.to_dict())
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Edit Static Asset
    def patch(self, request, ProjectId, StaticAssetId):
        doc_ref = db.collection(u'Projects').document(ProjectId).collection(
            u'StaticAssets').document(StaticAssetId)
        doc_ref.update(request.data)

        doc = doc_ref.get()
        if doc.exists:
            serializer = StaticAssetSerializer(doc.to_dict())
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
