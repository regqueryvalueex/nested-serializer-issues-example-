import pytest

from api.meetings.reversed_relation_serializers import MeetingSerializer

pytestmark = [pytest.mark.django_db]


def test_steal_comment(populated_meeting):
    old_comment = populated_meeting.comments.get()

    assert populated_meeting.comments.count() == 1

    serializer = MeetingSerializer(
        data={
            'title': 'Hello',
            'comments': [
                {
                    'description': 'Stolen!',
                    'pk': old_comment.pk,
                },
                {
                    'description': 'got bored again',
                },
            ]
        }
    )

    assert serializer.is_valid()
    new_meeting = serializer.save()

    assert new_meeting.title == 'Hello'
    assert new_meeting.comments.count() == 2

    assert populated_meeting.comments.count() == 0  # 'Oh no, comment now is stolen'
    old_comment.refresh_from_db()
    assert old_comment.meeting == new_meeting
