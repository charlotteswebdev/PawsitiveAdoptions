from unittest import TestCase, main
import requests

class TestSelectingEventsByCategory(TestCase):
    def test_events_endpoint_no_category(self):
        response = requests.get('http://localhost:5000/api/events')
        self.assertEqual(response.status_code, 200)

    def test_events_endpoint_with_category(self):
        response = requests.get('http://localhost:5000/api/events?category=Romance')
        self.assertEqual(response.status_code, 200)

    def test_invalid_category(self):
        pass

class TestingSelectingAllCategories(TestCase):
    def test_categories_endpoint(self):
        response = requests.get('http://localhost:5000/api/categories')
        self.assertEqual(response.status_code, 200)

class TestingDatabaseConnection(TestCase):
    def test_db_connected(self):
        pass

    def test_failed_db_connection(self):
        pass

    def test_invalid_db_query(self):
        pass

class TestEndpointRequests(TestCase):
    def test_root_endpoint_connected(self):
        pass

    def test_error_message(self):
        pass

if __name__ == '__main__':
    main()

