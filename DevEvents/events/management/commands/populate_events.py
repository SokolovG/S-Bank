import random

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker

from events.management.constants import location_names, cities, addresses, countries, categories, category_slugs, category_descriptions
from events.models import Location, Category, Event


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = Faker('ru_RU')


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

    def generate_location_data(self, count):
        locations = []
        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} test locations...")
                location_name=random.choice(location_names)
                address = self.faker.address()
                city = self.faker.city()
                country = self.faker.county()

                location = Location.objects.create(
                    name=location_name,
                    address=address,
                    city=city,
                    country=country
                )
                locations.append(location)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating location {index + 1}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} locations successfully created')
        )

        return locations

    def generate_category_data(self, count):
        categories = []
        for index, cat in enumerate(categories[:count]):
            try:
                slug = slugify(cat)
                description = self.faker.paragraph()
                category = Category.objects.create(
                    name=cat,
                    slug=slug,
                    description=description
                )
                categories.append(category)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating category {index + 1}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} categories successfully created')
        )
        return categories

    def generate_event_data(self, count, user, location, category, organizer):
        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} test events...")
                name = self.faker.company()
                description = self.faker.paragraph()
                event = Event.objects.create(
                    name=name,
                    description=description,
                    author=user,
                    organizer=organizer,
                    pub_date='',
                    location=location,
                    is_published='',
                    event_start_date='',
                    event_end_date='',
                    category=category,
                    is_online='',
                    meeting_link='',
                    is_verify='',
                    max_participants='',
                    registration_deadline='',
                    format='',
                    members='',
                    photos='',
                    you_are_member=''
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating events {index + 1}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} events successfully created')
        )

    def handle(self, *args, **options):
        count = options['count']

        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Location.objects.all().delete()
            Category.objects.all().delete()
            Event.objects.all().delete()

        locations = self.generate_location_data(count)
        categories = self.generate_category_data(count)
        # events = self.generate_event_data()

