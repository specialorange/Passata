# passata/management/commands/createsu.py
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if (
            not get_user_model()
            .objects.filter(username=os.environ["DJANGO_ADMIN_UNAME"])
            .exists()
        ):
            get_user_model().objects.create_superuser(
                username=os.environ["DJANGO_ADMIN_UNAME"],
                password=os.environ["DJANGO_ADMIN_PW"],
            )
        print("Superuser has been created.")
