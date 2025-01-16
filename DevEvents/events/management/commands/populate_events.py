import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from faker import Faker

from events.management.constants import location_names, categories, format_choices
from events.models import Location, Category, Event
from users.models import Organizer


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
                location_name = random.choice(location_names)
                address = self.faker.address()
                city = self.faker.city()
                country = self.faker.county()

                location_data = {
                    'location_name': location_name,
                    'address': address,
                    'city': city,
                    'country': country
                }
                location = Location.objects.create(**location_data)
                locations.append(location)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}. Data: {location_data}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} locations successfully created')
        )

        return locations

    def generate_category_data(self, count):
        categories_list = []
        for index, cat in enumerate(categories[:count]):
            try:
                slug = slugify(cat)
                description = self.faker.paragraph()
                category_data = {
                    'name': cat,
                    'slug': slug,
                    'description': description
                }
                category = Category.objects.create(**category_data)
                categories_list.append(category)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}. Data: {category_data}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} categories successfully created')
        )
        return categories_list

    def generate_organizer_data(self, count, user):
        organizers_list = []
        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} organizers...")
                name = self.faker.company()
                description = self.faker.paragraph()
                website = self.faker.url()
                contact = self.faker.url()
                verified = self.faker.boolean()
                number_of_events = self.faker.random_int(min=0, max=50)
                rating = self.faker.random_int(min=0, max=5)

                organizer_data = {
                'name': name,
                'description': description,
                'website': website,
                'contact': contact,
                'verified': verified,
                'number_of_events': number_of_events,
                'rating': rating,
                'user': user
            }

                organizer = Organizer.objects.create(**organizer_data)
                organizers_list.append(organizer)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}. Data: {organizer_data}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} organizers successfully created')
        )
        return organizers_list

    def generate_event_data(self, count, user, location, category, organizer):
        events_list = []
        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} test events...")
                name = f'{self.faker.word().capitalize()} Meetup'
                description = self.faker.paragraph()
                format = random.choice(format_choices)

                event_data = {
                    'name': name,
                    'description': description,
                    'author': user,
                    'organizer': organizer,
                    'location': location,
                    'category': category,
                    'is_online': self.faker.boolean(),
                    'is_verify': self.faker.boolean(),
                    'is_published': self.faker.boolean(),
                    'max_participants': self.faker.random_int(min=100, max=200),
                    'members': self.faker.random_int(min=10, max=200),
                    'format': format
                }

                current_date = datetime.now()
                event_data['pub_date'] = current_date
                event_data['event_start_date'] = current_date + timedelta(days=self.faker.random_int(min=1, max=30))
                event_data['event_end_date'] = event_data['event_start_date'] + timedelta(days=self.faker.random_int(min=1, max=3))
                event_data['registration_deadline'] = event_data['event_start_date'] - timedelta(days=self.faker.random_int(min=1, max=5))

                if event_data['is_online']:
                    event_data['meeting_link'] = self.faker.url()
                event = Event.objects.create(**event_data)
                events_list.append(event)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}. Data: {event_data}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} events successfully created')
        )
        return events_list

    def handle(self, *args, **options):
        count = options['count']
        User = get_user_model()
        users = User.objects.all()
        user = users.first()

        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Location.objects.all().delete()
            Category.objects.all().delete()
            Event.objects.all().delete()
            Organizer.objects.all().delete()

        locations = self.generate_location_data(count)
        categories = self.generate_category_data(count)
        organizers = self.generate_organizer_data(count, user)

        events = self.generate_event_data(count,
                                          user,
                                          random.choice(locations),
                                          random.choice(categories),
                                          random.choice(organizers))

