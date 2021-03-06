import os
import json
import unittest
import responses
from .context import eventgateway

with open(os.path.dirname(__file__)+'/testData.json', 'r') as f:
    testData = json.load(f)


class EgHappyPath(unittest.TestCase):
    def setUp(self):
        self.eg = eventgateway.EventGateway()
        self.egUrl = "http://localhost:4001"
        self.test_checkConnection()

    # HealthCheck #

    @responses.activate
    def test_checkConnection(self):
        responses.add(responses.GET, "{}/v1/status".format(self.egUrl),
                      status=200)
        self.assertTrue(self.eg.checkConnection())

    # Create stuff #

    @responses.activate
    def test_createEventType(self):
        responses.add(responses.POST,
                      "{}/v1/spaces/default/eventtypes".format(self.egUrl),
                      json=testData["eventtypeValid"], status=201)
        self.assertEqual(
            self.eg.createEventType(testData["eventtype"]),
            testData["eventtypeValid"]
        )

    @responses.activate
    def test_createFunction(self):
        responses.add(responses.POST,
                      "{}/v1/spaces/default/functions".format(self.egUrl),
                      json=testData["functionValid"], status=201)
        self.assertEqual(
            self.eg.createFunction(testData["function"]),
            testData["functionValid"]
        )

    @responses.activate
    def test_createSubscription(self):
        responses.add(responses.POST,
                      "{}/v1/spaces/default/subscriptions".format(self.egUrl),
                      json=testData["subscriptionValid"], status=201)
        self.assertEqual(
            self.eg.createSubscription(testData["subscription"]),
            testData["subscriptionValid"]
        )

    # Get All stuff #

    @responses.activate
    def test_getAllEventType(self):
        getAll = {
            "eventTypes": [testData["eventtypeValid"]]
        }
        responses.add(responses.GET,
                      "{}/v1/spaces/default/eventtypes".format(self.egUrl),
                      json=getAll, status=200)
        self.assertEqual(
            self.eg.getAllEventType(),
            getAll
        )

    @responses.activate
    def test_getAllFunction(self):
        getAll = {
            "functions": [testData["functionValid"]]
        }
        responses.add(responses.GET,
                      "{}/v1/spaces/default/functions".format(self.egUrl),
                      json=getAll, status=200)
        self.assertEqual(
            self.eg.getAllFunction(),
            getAll
        )

    @responses.activate
    def test_getAllSubscription(self):
        getAll = {
            "subscription": [testData["subscriptionValid"]]
        }
        responses.add(responses.GET,
                      "{}/v1/spaces/default/subscriptions".format(self.egUrl),
                      json=getAll, status=200)
        self.assertEqual(
            self.eg.getAllSubscription(),
            getAll
        )
