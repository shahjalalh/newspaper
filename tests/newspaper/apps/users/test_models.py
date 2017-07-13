import pytest

from tests.factories.users import UserFactory


@pytest.mark.django_db
def test_str():
    user = UserFactory()
    assert str(user) == 'j.doe'
