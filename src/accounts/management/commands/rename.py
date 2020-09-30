from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Renames a Django Project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django Project Name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        files_to_rename = ['base/settings/base.py', 'base/wsgi.py', 'manage.py']
        folder_to_rename = 'base'

        for f in files_to_rename:
            with open(f, 'r') as file:
                file_data = file.read()
            file_data = file_data.replace('base', new_project_name)

            with open(f, 'w') as file:
                file.write(file_data)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project Has been Renamed to %s'))
