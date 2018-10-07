from rest_framework import serializers
from hobbyist.api import models
from hobbyist.users.serializers import CustomUserSerializer


class ProjectCommentSerializer(serializers.ModelSerializer):
    commenter = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = models.ProjectComment
        fields = ('id', 'text', 'commenter')


class ProjectSerializer(serializers.ModelSerializer):
    comments = ProjectCommentSerializer(many=True, read_only=True)
    owner = CustomUserSerializer(many=False, read_only=True)
    participants = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = ('id', 'title', 'description', 'karma',
                  'comments', 'owner', 'participants')


class ProjectCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            validated_data['owner'] = self.context['request'].user
        return super(ProjectCreateSerializer, self).create(validated_data)

    class Meta:
        model = models.Project
        fields = ('title', 'description')
