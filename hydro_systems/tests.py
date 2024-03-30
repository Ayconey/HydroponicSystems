from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import HydroSystem, Measurement


class HydroSystemTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Creating a test user
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.admin = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpass')
        self.client.force_authenticate(user=self.user)

        # Creating a hydroponic system for testing
        self.hydro_system = HydroSystem.objects.create(name="Test System", owner=self.user)

    def test_hydro_system_list_create_as_admin(self):
        """Test adding a new hydroponic system as an admin"""
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/hydro/hydro-systems/', {'name': 'Admin System'}, format='json')

        # Checking if the response returns status HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Checking if the number of HydroSystem objects in the database increased by 1
        self.assertEqual(HydroSystem.objects.count(), 2)

    def test_user_hydro_system_list_create(self):
        """Test adding a new hydroponic system by a user"""
        response = self.client.post('/hydro/hydro-systems/', {'name': 'New System'}, format='json')

        # Checking if the response returns status HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Checking if the number of HydroSystem objects in the database increased by 1
        self.assertEqual(HydroSystem.objects.count(), 2)

    def test_hydro_system_retrieve(self):
        """Test retrieving a hydroponic system"""
        response = self.client.get(f'/hydro/hydro-systems/{self.hydro_system.id}/')

        # Checking if the response returns status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Checking if the name of the system retrieved from the response matches the expected one
        self.assertEqual(response.data['name'], 'Test System')

    def test_hydro_system_update(self):
        """Test updating a hydroponic system"""
        updated_data = {'name': 'Updated System'}
        response = self.client.put(f'/hydro/hydro-systems/{self.hydro_system.id}/', updated_data, format='json')

        # Checking if the response returns status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refreshing the object from database to get updated values
        self.hydro_system.refresh_from_db()

        # Checking if the name of the system has been updated correctly
        self.assertEqual(self.hydro_system.name, 'Updated System')

    def test_hydro_system_destroy(self):
        """Test destroying a hydroponic system"""
        response = self.client.delete(f'/hydro/hydro-systems/{self.hydro_system.id}/')

        # Checking if the response returns status HTTP 204 No Content (as the object is deleted)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Checking if the HydroSystem object has been deleted from the database
        with self.assertRaises(HydroSystem.DoesNotExist):
            HydroSystem.objects.get(id=self.hydro_system.id)

    def test_hydro_system_retrieval_not_owner(self):
        """Test hydroponic system retrieval by not owner user"""
        user2 = User.objects.create_user(username='testuser2', password='12345')
        hydro_system = HydroSystem.objects.create(name="Test System 2", owner=user2)
        response = self.client.get(f'/hydro/hydro-systems/{hydro_system.id}/')

        # Checking if the response returns status HTTP 403
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MeasurementTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Creating a test user
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)

        # Creating a hydroponic system and a measurement for testing
        self.hydro_system = HydroSystem.objects.create(name="Test System", owner=self.user)
        self.measurement = Measurement.objects.create(system=self.hydro_system, date='2022-01-01', ph=7.0,
                                                      water_temperature=20.0, tds=500.0)

    def test_measurements_from_hydro_system_list_create(self):
        """Test adding a new measurement to a hydroponic system"""
        response = self.client.post(f'/hydro/hydro-systems/{self.hydro_system.id}/measurements/',
                                    {'date': '2022-01-02', 'ph': 7.2, 'water_temperature': 21.0, 'tds': 550.0}, format='json')

        # Checking if the response returns status HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Checking if the number of Measurement objects in the database increased by 1
        self.assertEqual(Measurement.objects.count(), 2)

    def test_measurement_retrieve(self):
        """Test retrieving a single measurement"""
        response = self.client.get(f'/hydro/measurements/{self.measurement.id}/')

        # Checking if the response returns status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Checking if the value of the retrieved measurement matches the expected one
        self.assertEqual(response.data['ph'], 7.0)

    def test_measurement_update(self):
        """Test updating a single measurement"""
        updated_data = {'date':'2022-01-01', 'ph':7.5, 'water_temperature':20.0, 'tds':500.0}
        response = self.client.put(f'/hydro/measurements/{self.measurement.id}/', updated_data, format='json')

        # Checking if the response returns status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refreshing the object from database to get updated values
        self.measurement.refresh_from_db()

        # Checking if the ph value of the measurement has been updated correctly
        self.assertEqual(self.measurement.ph, 7.5)

    def test_measurement_destroy(self):
        """Test destroying a single measurement"""
        response = self.client.delete(f'/hydro/measurements/{self.measurement.id}/')

        # Checking if the response returns status HTTP 204 No Content (as the object is deleted)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Checking if the Measurement object has been deleted from the database
        with self.assertRaises(Measurement.DoesNotExist):
            Measurement.objects.get(id=self.measurement.id)

    def test_measurement_retrieval_not_owner(self):
        """Test measurement retrieving by not owner user"""
        user2 = User.objects.create_user(username='testuser2', password='12345')
        hydro_system = HydroSystem.objects.create(name="Test System 2", owner=user2)
        measurement = Measurement.objects.create(system=hydro_system, date='2022-01-01', ph=7.0,
                                                 water_temperature=20.0, tds=500.0)
        response = self.client.get(f'/hydro/measurements/{measurement.id}/')

        # Checking if the response returns status HTTP 403 FORBIDDEN
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)