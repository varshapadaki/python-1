import threading
import time
import random
import unittest

class Team:
    def __init__(self, name):
        self.name = name

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

    def create_match(self, team1, team2):
        match_id = self.next_match_id
        match = Match(match_id, team1, team2)
        self.matches[match_id] = match
        self.next_match_id += 1
        print(f"Match {match_id} created between {team1.name} and {team2.name}")

    def update_match_score(self, match_id, team1_score, team2_score):
        match = self.matches.get(match_id)
        if match:
            match.team1_score = team1_score
            match.team2_score = team2_score
            if team1_score > team2_score:
                match.winner = match.team1.name
            elif team2_score > team1_score:
                match.winner = match.team2.name
            else:
                match.winner = "Draw"
            print(f"Match {match_id} score updated")

    def display_match_details(self, match_id):
        match = self.matches.get(match_id)
        if match:
            print(f"Match ID: {match.match_id}")
            print(f"Team 1: {match.team1.name} (Score: {match.team1_score})")
            print(f"Team 2: {match.team2.name} (Score: {match.team2_score})")
            print(f"Winner: {match.winner}")
        else:
            print(f"Match {match_id} not found")

# Example usage
if __name__ == "__main__":
    # Create IPLMatchTracker instance
    tracker = IPLMatchTracker()

    # Create teams
    team1 = Team("Mumbai Indians")
    team2 = Team("Chennai Super Kings")

    # Schedule matches
    tracker.create_match(team1, team2)
    tracker.create_match(Team("Royal Challengers Bangalore"), Team("Kolkata Knight Riders"))

    # Update match scores
    tracker.update_match_score(1, 180, 170)
    tracker.update_match_score(2, 150, 160)

    # Display match details
    tracker.display_match_details(1)
    tracker.display_match_details(2)
    tracker.display_match_details(3)  # This will show "Match 3 not found"


