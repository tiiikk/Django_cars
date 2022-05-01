import json

from django.core.management.base import BaseCommand

from cars.models import Category, Car


class Command(BaseCommand):
    help = 'Loads cars from json into db.'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1, type=str)

    def handle(self, *args, **options):
        path = options['path'][0]

        with open(path, 'r') as f:
            data = json.load(f)

        categories = set()
        for car in data:
            categories.add(car['category'])
        
        _ = Category.objects.bulk_create(
            [Category(name=name) for name in categories],
            ignore_conflicts=True,
        )

        categories = Category.objects.all()
        categories_name_id = {c.name: c.pk for c in categories}
        # {'Mazda': 50}

        cars = []
        for car in data:
            currency = car['price'][0]
            price = float(car['price'][1:])

            c = Car(
                name=car['name'],
                vin=car['vin'],
                price=price,
                currency=currency,
                year=car['year'],
                category_id=categories_name_id[car['category']],
            )

            cars.append(c)

        Car.objects.bulk_create(cars, ignore_conflicts=True)
