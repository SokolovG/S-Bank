import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker

from events.management.constants import (location_names,
                                         categories_names,
                                         format_choices,
                                         technologies)
from events.models import Location, Category, Event, Comment
from users.models import Organizer, Profile




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
        entity_type = 'Location'
        locations = []
        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} test locations...")
                location_name = random.choice(location_names)
                address = self.faker.address()
                city = self.faker.city()
                country = self.faker.country()

                location_data = {
                    'name': location_name,
                    'address': address,
                    'city': city,
                    'country': country
                }
                location = Location.objects.create(**location_data)
                locations.append(location)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}.')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} locations successfully created')
        )

        return locations

    def generate_user_data(self, count):
        entity_type = 'Users'
        users_list = []
        for index in range(count):
            try:
                username = self.faker.user_name()
                first_name = self.faker.first_name()
                last_name = self.faker.last_name()
                email = self.faker.email()
                password = 'testpass123'

                user_data = {
                    'password': password,
                    'username': username,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                }

                user = User.objects.create(**user_data)
                users_list.append(user)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}.')
                )
        self.stdout.write(
            self.style.SUCCESS(f'{count} users successfully created')
        )

        return users_list

    def generate_category_data(self, count, categories):
        entity_type = 'Category'
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
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}.')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} categories successfully created')
        )
        return categories_list

    def generate_organizer_data(self, count, users):
        entity_type = 'Organizer'
        organizers_list = []
        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} organizers...")
                name = self.faker.company()[:25]
                description = self.faker.paragraph()
                website = self.faker.url()
                contact = self.faker.url()
                verified = self.faker.boolean()
                number_of_events = self.faker.random_int(min=0, max=50)
                rating = self.faker.random_int(min=0, max=5)
                user = users[index]

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
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}.')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} organizers successfully created')
        )
        return organizers_list

    def generate_event_data(self, count, users, location, category, organizer):
        entity_type = 'Event'
        events_list = []
        for index in range(count):
            try:
                self.stdout.write(f"Let's start creating {index} test events...")
                name = f'{self.faker.word().capitalize()} Meetup'
                description = self.faker.paragraph()
                format = random.choice(format_choices)
                max_participants = self.faker.random_int(min=100, max=200)
                user = users[index]
                event_data = {
                    'name': name,
                    'description': description,
                    'author': user,
                    'category': category[index],
                    'organizer': organizer[index],
                    'location': location[index],
                    'is_online': self.faker.boolean(),
                    'is_verify': self.faker.boolean(),
                    'is_published': self.faker.boolean(),
                    'you_are_member': self.faker.boolean(),
                    'max_participants': self.faker.random_int(min=100, max=200),
                    'members': self.faker.random_int(min=10, max=max_participants),
                    'format': format,
                }

                current_date = timezone.now()
                event_data['pub_date'] = current_date
                event_data['event_start_date'] = current_date + timedelta(days=self.faker.random_int(min=1, max=30))
                event_data['event_end_date'] = event_data.get('event_start_date') + timedelta(days=self.faker.random_int(min=1, max=3))
                registration_deadline = event_data['event_start_date'] - timedelta(days=self.faker.random_int(min=1, max=5))

                if registration_deadline < current_date:
                    registration_deadline = current_date + timedelta(days=1)
                event_data['registration_deadline'] = registration_deadline

                if event_data['is_online']:
                    event_data['meeting_link'] = self.faker.url()

                event = Event.objects.create(**event_data)
                events_list.append(event)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}.')
                )

        self.stdout.write(
            self.style.SUCCESS(f'{count} events successfully created')
        )
        return events_list

    def generate_comment_data(self, count, events, users):
        entity_type = 'Comments'
        comments_list = []
        for index in range(count):
            self.stdout.write(f"Let's start creating {index} comments...")
            try:
                comments_data = {
                    'text': self.faker.paragraph(),
                    'event': events[index],
                    'author': users[index],
                }

                comment = Comment.objects.create(**comments_data)
                comments_list.append(comment)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}.')
                )
        self.stdout.write(
            self.style.SUCCESS(f'{count} comments successfully created')
        )

        return comments_list

    def generate_profile_data(self, count, users, locations, technologies, events=None):
        entity_type = 'Profile'
        profile_list = []
        for index in range(count):
            self.stdout.write(f"Let's start creating {index} profiles...")
            try:
                profile_data = {
                    'user': users[index],
                    'location': locations[index],
                    'interested_technologies': technologies[index],
                    'notifications_enabled': self.faker.boolean(),
                }

                profile = Profile.objects.create(**profile_data)
                if events:
                    num_events = self.faker.random_int(0, 3)
                    random_events = self.faker.random_choices(
                        elements=events,
                        length=num_events
                    )
                    profile.registered_events.add(*random_events)
                profile_list.append(profile)

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating {entity_type} {index + 1}: {str(e)}.')
                )
        self.stdout.write(
            self.style.SUCCESS(f'{count} profiles successfully created')
        )

        return profile_list

    def handle(self, *args, **options):
        count = options['count']

        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Event.objects.all().delete()
            Comment.objects.all().delete()
            Organizer.objects.all().delete()
            Category.objects.all().delete()
            Location.objects.all().delete()
            User.objects.all().delete()
            Profile.objects.all().delete()
            Comment.objects.all().delete()


        users = self.generate_user_data(count)
        locations = self.generate_location_data(count)
        categories = self.generate_category_data(count, categories_names)
        organizers = self.generate_organizer_data(count, users)

        events = self.generate_event_data(count,
                                          users,
                                          locations,
                                          categories,
                                          organizers)
        comments = self.generate_comment_data(count, events, users)
        profiles = self.generate_profile_data(count,users,locations, technologies, events)
