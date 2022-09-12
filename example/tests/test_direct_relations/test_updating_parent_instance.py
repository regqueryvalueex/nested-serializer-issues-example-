import pytest

from api.meetings.direct_relation_serializers import CommentSerializer

pytestmark = [pytest.mark.django_db]


def test_update_meeting_via_comment(populated_meeting):
    old_comment = populated_meeting.comments.get()

    assert populated_meeting.comments.count() == 1

    serializer = CommentSerializer(
        instance=old_comment,
        data={
            'description': 'editing meeting title',
            'meeting': {
                'pk': populated_meeting.pk,
                'title': 'Changed!'
            }
        }
    )

    assert serializer.is_valid()
    serializer.save()

    populated_meeting.refresh_from_db()
    assert populated_meeting.title == 'Changed!'


def test_create_new_meeting_via_comment(populated_meeting):
    old_comment = populated_meeting.comments.get()
    assert populated_meeting.comments.count() == 1

    serializer = CommentSerializer(
        instance=old_comment,
        data={
            'description': 'editing meeting title',
            'meeting': {
                'title': 'New one!'
            }
        }
    )

    assert serializer.is_valid()
    comment = serializer.save()

    populated_meeting.refresh_from_db()

    assert populated_meeting.title != 'New one!'
    assert populated_meeting.comments.count() == 0

    assert comment.meeting.id != populated_meeting.id


def test_steel_other_meeting_via_comment(populated_meeting):
    assert populated_meeting.comments.count() == 1

    serializer = CommentSerializer(
        data={
            'description': 'editing meeting title',
            'meeting': {
                'pk': populated_meeting.pk,
                'title': 'Stolen meeting!'
            }
        }
    )

    assert serializer.is_valid()
    comment = serializer.save()

    populated_meeting.refresh_from_db()

    assert populated_meeting.title == 'Stolen meeting!'
    assert populated_meeting.comments.count() == 2

    assert comment.meeting.id == populated_meeting.id
