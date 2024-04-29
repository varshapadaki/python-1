import threading
import time
import random
import unittest

class Match:
    def __init__(self, match_id, team1, team2):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.team1_score = None
        self.team2_score = None
        self.winner = None

class IPLMatchTracker:
    def __init__(self):
        self.matches = {}
        self.next_match_id = 1
        self.lock = threading.Lock()

    def create_match(self, team1, team2):
        match_id = self.next_match_id
        match = Match(match_id, team1, team2)
        with self.lock:
            self.matches[match_id] = match
            self.next_match_id += 1
        print(f"Match {match_id} created between {team1} and {team2}")

    def display_match_details(self, match_id):
        with self.lock:
            match = self.matches.get(match_id)
            if match:
                print(f"Match ID: {match.match_id}")
                print(f"Team 1: {match.team1} (Score: {match.team1_score})")
                print(f"Team 2: {match.team2} (Score: {match.team2_score})")
                print(f"Winner: {match.winner}")
            else:
                print(f"Match {match_id} not found")

    def update_match_score(self, match_id, team1_score, team2_score):
        def update_score():
            with self.lock:
                match = self.matches.get(match_id)
                if match:
                    match.team1_score = team1_score
                    match.team2_score = team2_score
                    if team1_score > team2_score:
                        match.winner = match.team1
                    elif team2_score > team1_score:
                        match.winner = match.team2
                    else:
                        match.winner = None
                    print(f"Match {match_id} score updated")

        thread = threading.Thread(target=update_score)
        thread.start()

    def delete_match(self, match_id):
        with self.lock:
            if match_id in self.matches:
                del self.matches[match_id]
                print(f"Match {match_id} deleted")
            else:
                print(f"Match {match_id} not found")

# Unit tests for IPLMatchTracker
class TestIPLMatchTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = IPLMatchTracker()

    def test_create_match(self):
        self.tracker.create_match("Mumbai Indians", "Chennai Super Kings")
        self.assertEqual(len(self.tracker.matches), 1)

    def test_display_match_details(self):
        self.tracker.create_match("Royal Challengers Bangalore", "Kolkata Knight Riders")
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.tracker.display_match_details(1)
            expected_output = """\
Match ID: 1
Team 1: Royal Challengers Bangalore (Score: None)
Team 2: Kolkata Knight Riders (Score: None)
Winner: None
"""
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update_match_score(self):
        self.tracker.create_match("Delhi Capitals", "Sunrisers Hyderabad")
        self.tracker.update_match_score(1, 180, 170)
        match = self.tracker.matches[1]
        self.assertEqual(match.team1_score, 180)
        self.assertEqual(match.team2_score, 170)

    def test_delete_match(self):
        self.tracker.create_match("Rajasthan Royals", "Punjab Kings")
        self.tracker.delete_match(1)
        self.assertIsNone(self.tracker.matches.get(1))

if __name__ == "__main__":
    unittest.main()

