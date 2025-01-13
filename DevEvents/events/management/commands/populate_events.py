import random

from django.core.management.base import BaseCommand

from events.management.constants import location_names, cities, addresses, countries
from events.models import Location

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

    def generate_sample_data(self):
        return {
            'location_names': random.choice(location_names),
            'addresses': random.choice(addresses),
            'cities': random.choice(cities),
            'countries': random.choice(countries)
        }

    def handle(self, *args, **options):
        count = options['count']

        if options['clear']:
            self.stdout.write('Clearing existing locations...')
            Location.objects.all().delete()

        self.stdout.write(f"Let's start creating {count} test locations...")

        for location in range(count):
            try:
                data = self.generate_sample_data()
                location = Location.objects.create(
                    name=data.get('location_names'),
                    address=data.get('addresses'),
                    city=data.get('cities'),
                    country=data.get('countries')
                    )

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating location {location + 1}: {str(e)}')
                )
        self.stdout.write(
            self.style.SUCCESS(f'{count} events successfully created')
        )