import time as tm
from dateutil.parser import parse
from .views import *
from django.test import TestCase
from django.test import Client
from .models import Modules, Groundtruth, Rooms, Timemodule, Wifilogdata, PercentagePredictions, EstimatePredictions
import datetime
from django.core.management import call_command




class OccupantsViewsTestCase(TestCase):

    fixtures = ['initial_data']
    #call_command("loaddata", "initial_data.json", verbosity=3)

    # Test general links
    def test_homepage(self):
        """Test that the homepage is accessible"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_login(self):
        """Test that the login page is accessible"""
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)
	
    def test_logout(self):
        """Test that the log out page is accessible"""
        resp = self.client.get('/logout/')
        self.assertEqual(resp.status_code, 200)
	
    def test_register(self):
        """Test that the registration page is accessible"""
        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)
    
    def test_Stats(self):
        """Test that the Stats page is accessible"""
        resp = self.client.get('/Stats/')
        self.assertEqual(resp.status_code, 200)
    
    # Test API
    def test_RoomList(self):
        """Test that the homepage is accessible"""
        resp = self.client.get('/RoomList/')
        self.assertEqual(resp.status_code, 200)

    def test_ModuleList(self):
        """Test that the login page is accessible"""
        resp = self.client.get('/ModuleList/')
        self.assertEqual(resp.status_code, 200)
	
    def test_GroundtruthList(self):
        """Test that the log out page is accessible"""
        resp = self.client.get('/GroundtruthList/')
        self.assertEqual(resp.status_code, 200)
	
    def test_TimemoduleList(self):
        """Test that the registration page is accessible"""
        resp = self.client.get('/TimemoduleList/')
        self.assertEqual(resp.status_code, 200)
    
    def test_BinaryPredictionsList(self):
        """Test that the Stats page is accessible"""
        resp = self.client.get('/BinaryPredictionsList/')
        self.assertEqual(resp.status_code, 200)
    
    def test_PercentagePredictionsList(self):
        """Test that the registration page is accessible"""
        resp = self.client.get('/PercentagePredictionsList/')
        self.assertEqual(resp.status_code, 200)
    
    def test_EstimatePredictionsList(self):
        """Test that the Stats page is accessible"""
        resp = self.client.get('/EstimatePredictionsList/')
        self.assertEqual(resp.status_code, 200)

    def setUp(self):
        # Every test needs a client.
        self.client = Client()




    def test_addroom(self):
        """Test that the database empty and is responding to queries"""
        respBefore = Rooms.objects.all()
        Rooms.objects.create(
            room='B-002',
            building='Computer Science',
            campus='Belfield',
            capacity=90
        )
        Rooms.objects.create(
            room='B-003',
            building='Computer Science',
            campus='Belfield',
            capacity=90
        )
        Rooms.objects.create(
            room='B-004',
            building='Computer Science',
            campus='Belfield',
            capacity=220
        )
        respAfter = Rooms.objects.all()
        print('Before', len(respBefore))
        print('After', len(respAfter))
        self.assertTrue(len(respAfter) == 3)


    def test_addmodules(self):

        respBefore = Rooms.objects.all()
        Modules.objects.create(
            modulename='COMP30600',
            numreg=40
        )
        Modules.objects.create(
            modulename='COMP47350',
            numreg=35
        )
        Modules.objects.create(
            modulename='COMP41100',
            numreg=60
        )
        Modules.objects.create(
            modulename='none',
            numreg=0
        )
        respAfter = Modules.objects.all()
        print('Before', len(respBefore))
        print('After', len(respAfter))
        self.assertTrue(len(respAfter) == 4)













#
#
#     # def test_GenGraph(self):
#     #     c = Client()
#     #     c.login(username='', password='')
#     #     # Extra parameters to make this a Ajax style request.
#     #     kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
#     #     url = '/GenGraph'
#     #     data = {'timeModuleId': 236,}
#     #     # csrf_client = Client(enforce_csrf_checks=True)
#     #
#     #     response = c.post(url, data, **kwargs)
#     #     self.assertEqual(response.status_code, 200)
#
#
#
#         # response = self.client.post(url, data, **kwargs)
#
#         """ test needed that the query is in the database """
#
#
#     # def test_calendarGen(self):
#     #     """Test fails due to csrf not sent and query data not sent"""
#     #     resp = self.client.post('/calendarGen')
#     #     self.assertEqual(resp.status_code, 200)
#     #
#     # def test_RoomDayGraph(self):
#     #     """Test fails due to csrf not sent and query data not sent"""
#     #     resp = self.client.post('/RoomDayGraph')
#     #     self.assertEqual(resp.status_code, 200)
#     #
#     # def test_Rooms(self):
#     #     """Test fails due to csrf not sent and query data not sent"""
#     #     resp = self.client.post('/Rooms/')
#     #     self.assertEqual(resp.status_code, 200)
#
#
#
#
#
# """ test that you can not access protected pages without logging in"""
#
#
# def epochtime(x):
#     """ rewrite as test """
#     string = parse(x)
#     epoch = int(tm.mktime(string.timetuple()))
#     return epoch
#
# print(epochtime("Wednesday, 27-Jul-16 11:37:51 GMT"))
