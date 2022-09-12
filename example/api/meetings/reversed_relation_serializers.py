from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from meetings.models import Meeting, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'pk',
            'description',
        )


class MeetingSerializer(WritableNestedModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Meeting
        fields = (
            'pk',
            'title',
            'comments',
        )
