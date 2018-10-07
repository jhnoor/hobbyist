import random

from django.shortcuts import get_object_or_404
from hobbyist.api import models
from hobbyist.api import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model


@api_view(['PUT'])
def downvote(request, project_pk):
    project = models.Project.objects.get(pk=project_pk)
    project.karma += 1
    project.save()
    return Response()


@api_view(['PUT'])
def upvote(request, project_pk):
    project = models.Project.objects.get(pk=project_pk)
    project.karma -= 1
    project.save()
    return Response()


@api_view(['POST'])
def comment(request, project_pk):
    project = models.Project.objects.get(pk=project_pk)
    commenter = {}
    if(request.user.pk):
        commenter = None
    else:
        commenter = get_user_model().objects.get(pk=1)

    project_comment = models.ProjectComment.objects.create(text=request.data["text"], project=project, commenter=commenter)
    project_comment.save()
    serializer = serializers.ProjectCommentSerializer(project_comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectViewSet(viewsets.ViewSet):
    """
    API endpoint for projects
    """
    def create(self, request):
        permission_classes = (IsAuthenticated)
        serializer = serializers.ProjectCreateSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = models.Project.objects.all().order_by('-karma')
        serializer = serializers.ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ProjectSerializer(project)
        return Response(serializer.data)


class ProjectCommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = models.ProjectComment.objects.all()
        serializer = serializers.ProjectCommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.ProjectComment.objects.filter(project__id=pk)
        serializer = serializers.ProjectCommentSerializer(queryset, many=True)
        return Response(serializer.data)
