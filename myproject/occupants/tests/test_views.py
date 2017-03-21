import time as tm
from dateutil.parser import parse
from occupants.views import *
from django.test import TestCase
from django.test import Client
from occupants.models import Rooms



class OccupantsViewsTestCase(TestCase):

    def test_add_room(self):
        """Test that the database empty and is responding to queries"""
        respBefore = Rooms.objects.all()
        print('Before', respBefore, ': len', len(respBefore))

        Rooms.objects.create(
            room='B-005',
            building='CS',
            campus='DUBLIN',
            capacity=25
        )
        Rooms.objects.create(
            room='B-006',
            building='CS',
            campus='DUBLIN',
            capacity=50
        )
        Rooms.objects.create(
            room='B-009',
            building='CS',
            campus='DUBLIN',
            capacity=120
        )

        respAfter = Rooms.objects.all()
        print('After', respAfter, ': len', len(respAfter))
        self.assertTrue(len(respAfter) == 3)