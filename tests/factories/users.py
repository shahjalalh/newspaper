import factory

from newspaper.apps.users import models


class UserFactory(factory.DjangoModelFactory):
    username = 'j.doe'
    first_name = 'John'
    last_name = 'Doe'
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)
    password = 'supersecret'

    is_active = True
    is_staff = False
    is_superuser = False

    class Meta:
        model = models.User

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        password = kwargs.pop('password')
        user = super(UserFactory, cls)._create(target_class, *args, **kwargs)

        if password:
            user.set_password(password)
            user.clear_password = password
            user.save()
        return user
