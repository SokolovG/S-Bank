import random

from django.core.management.base import BaseCommand

from events.management.constants import location_names, cities, addresses, countries, categories, category_slugs, category_descriptions
from events.models import Location, Category

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of events to create'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing events before creating new ones'
        )

    def generate_location_data(self, index):
        return {
            'location_names': location_names[index],
            'addresses': addresses[index],
            'cities': cities[index],
            'countries': countries[index]
        }

    def generate_category_data(self, index):
        return {
            'categories': categories[index],
            'slugs': category_slugs[index],
            'descriptions': category_descriptions[index],
        }

    def handle(self, *args, **options):
        count = options['count']

        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Location.objects.all().delete()
            Category.objects.all().delete()


        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} test locations...")
                data = self.generate_location_data(index)
                location = Location.objects.create(
                    name=data.get('location_names'),
                    address=data.get('addresses'),
                    city=data.get('cities'),
                    country=data.get('countries')
                    )

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating location {index + 1}: {str(e)}')
                )
        self.stdout.write(
            self.style.SUCCESS(f'{count} locations successfully created')
        )

        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} test categories...")
                data = self.generate_category_data(index)
                category = Category.objects.create(
                    name=data.get('categories'),
                    slug=data.get('slugs'),
                    description=data.get('descriptions')
                )

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating category {index + 1}: {str(e)}')
        )

        self.stdout.write(
            self.style.SUCCESS(f'{count} categories successfully created')
        )