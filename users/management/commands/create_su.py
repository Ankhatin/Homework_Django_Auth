from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='ankhatin@gmail.com',
            first_name='Admin',
            last_name='Home',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123')
        user.save()