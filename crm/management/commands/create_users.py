from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates predefined users'

    def handle(self, *args, **options):
        # Суперюзер
        User.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@example.com'
        )

        # Бухгалтер
        accountant = User.objects.create_user(
            username='accountant',
            password='accountant123',
            email='accountant@example.com'
        )
        accountant.is_staff = True
        accountant.save()

        # Менеджер
        User.objects.create_user(
            username='manager',
            password='manager123',
            email='manager@example.com'
        )

        self.stdout.write(self.style.SUCCESS('Successfully created predefined users'))