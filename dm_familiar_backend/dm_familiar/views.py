from django.shortcuts import render
from django.http.response import Http404
from .serializers import ProjectSerializer, TemplateSerializer
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
            print(doc)
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
        doc_ref = db.collections(u'Projects').document(ProjectId)

        doc = doc_ref.get()
        if doc.exists:
            serializer = ProjectSerializer(doc.to_dict())
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Template(APIView):


    def post(self, request):
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            db.collection('Projects').document(ProjectID).add(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


