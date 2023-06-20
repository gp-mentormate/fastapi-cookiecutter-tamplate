import factory

from src.users.v1.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f'user{n}@example.com')
    password = 'Testpass123!'
