
from django.core.management.base import BaseCommand
from flights.models import Flights, Airport

class Command(BaseCommand):
    help = 'Adds a flight to the database'

    def handle(self, *args, **kwargs):
        
        # Retrieve the airport instances
        nyc_airport = Airport.objects.get(code="NYC")
        ada_airport = Airport.objects.get(code="ADA")
        dxb_airport = Airport.objects.get(code="DXB")
        ade_airport = Airport.objects.get(code="ADE")
        # Add more airports as needed

        # Define a list of Flights instances to be created
        flights_to_add = [
        Flights(origin=nyc_airport, destination=ade_airport, duration=450),
        Flights(origin=ada_airport, destination=nyc_airport, duration=430),
        Flights(origin=dxb_airport, destination=ade_airport, duration=100),
        Flights(origin=dxb_airport, destination=ada_airport, duration=330),
        # Add more Flights instances as needed
        ]

        # Use bulk_create to add all flights at once
        Flights.objects.bulk_create(flights_to_add)

        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(flights_to_add)} flights'))

        #############################################

        # airports = [
        # Airport(code="NYC", city="New York"),
        # Airport(code="DXB", city="Dubai"),
        # Airport(code="ADA", city="Turkey"),
        # Airport(code="ADE", city="Yemen	"),
        # ]
        # Airport.objects.bulk_create(airports)

        # self.stdout.write(self.style.SUCCESS('Successfully added flight'))

        #############################################
        
        # all_flights = Flights.objects.all()
        # self.stdout.write('Current flights in the database:')
        # for flight in all_flights:
        #     self.stdout.write(f'{flight.id}: {flight.origin} to {flight.destination} lasting {flight.duration} minutes')
        ##############################################
        # Retrieve a flight by its ID (replace 1 with the actual ID you're interested in)
        # flight = Flights.objects.get(id=1)

        # # Accessing flight details
        # print(f"Flight ID: {flight.id}")
        # print(f"Origin Airport Code: {flight.origin.code}, City: {flight.origin.city}")
        # print(f"Destination Airport Code: {flight.destination.code}, City: {flight.destination.city}")
        # print(f"Flight Duration: {flight.duration} minutes")

    