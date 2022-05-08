from django.test import TestCase

# Create your tests here.
from cars.models import Car, Category


class CarTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='Test cat')
        Car.objects.create(name='45678988765346', price=123443, currency='$', year=2000, category=cat,
                           vin='764576879867545')

    def test_animals_can_speak(self):
        car = Car.objects.get(name="45678988765346")
        self.assertEqual(car.vin, '764576879867545')
        print(car.vin)


class CarTestCase1(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='Test cat')
        Car.objects.create(name='45678988765346', price=123443, currency='$', year=2000, category=cat,
                           vin='764576879867545')

    def test_animals_can_speak(self):
        car = Car.objects.get(name="45678988765346")
        self.assertEqual(car.vin, '764576879867545')
        print(car.vin)


class CarTestCase2(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='Test cat')
        Car.objects.create(name='45678988765346', price=123443, currency='$', year=2000, category=cat,
                           vin='764576879867545')

    def test_animals_can_speak(self):
        car = Car.objects.get(name="45678988765346")
        self.assertEqual(car.vin, '764576879867545')
        print(car.vin)
