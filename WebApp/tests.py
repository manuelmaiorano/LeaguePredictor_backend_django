from django.test import TestCase
from .algo import *
from .serializers import LeagueRowSerializer
# Create your tests here.
class TestAlgo(TestCase):
    def test_algo(self):
        t1 = Team('nap', 10, 10, 2)
        t2 = Team('mil', 10, 12, 0)
        lg = League('sa', 30, [t1, t2])
        results = calculate_probabs(lg)
        print(results)

class TestCalcView(TestCase):
    def test_view_calc(self):
        data =  {
                    "name": "serieb",
                    "description": "serieb",
                    "total_games": 38,
                    "rows": [
                        {
                            "team_name": "Benevento",
                            "wins": 10,
                            "draws": 2,
                            "losses": 1,
                            "probab": 0.0
                        },
                        {
                            "team_name": "hella",
                            "wins": 10,
                            "draws": 2,
                            "losses": 1,
                            "probab": 0.0
                        }
                    ]
                }
        response = self.client.post('/api/calculate/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_view_calc_bad(self):
        data =  {
                    "name": "serieb",
                    "description": "serieb",
                    "total_games": 10,
                    "rows": [
                        {
                            "team_name": "Benevento",
                            "wins": 10,
                            "draws": 2,
                            "losses": 1,
                            "probab": 0.0
                        },
                    ]
                }
        response = self.client.post('/api/calculate/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_view_calc_neg(self):
        data =  {
                    "name": "serieb",
                    "description": "serieb",
                    "total_games": 10,
                    "rows": [
                        {
                            "team_name": "Benevento",
                            "wins": -10,
                            "draws": 2,
                            "losses": 1,
                            "probab": 0.0
                        },
                    ]
                }
        response = self.client.post('/api/calculate/', data=data, content_type='application/json')
        print(response.content)
        self.assertEqual(response.status_code, 400)

    def test_valid(self):
        data = {
                "team_name": "Benevento",
                "wins": -10,
                "draws": 2,
                "losses": 1,
                "probab": 0.0
        }
        print(LeagueRowSerializer(data=data).is_valid())