from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom (extended) user model.

    The user model is extended by default projects, this way
    we don't have to bother with difficult migrations in the future.
    """
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.get_username()
