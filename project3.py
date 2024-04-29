import threading
import time
import random
import unittest

class Team:
    def __init__(self, name):
        self.name = name

class Match:
    def __init__(self, match_id, team1, team2, team1_score=None, team2_score=None):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.winner = None

class Match_Result_Tracker:
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

    def delete_match(self, match_id):
        if match_id in self.matches:
            del self.matches[match_id]
            print(f"Match {match_id} deleted successfully")
        else:
            print(f"Match {match_id} not found")

    def display_match_details(self, match_id):
        match = self.matches.get(match_id)
        if match:
            print(f"Match ID: {match.match_id}")
            print(f"Team 1: {match.team1.name} (Score: {match.team1_score})")
            print(f"Team 2: {match.team2.name} (Score: {match.team2_score})")
            print(f"Winner: {match.winner}")
        else:
            print(f"Match {match_id} not found")

    def team_statistics(self, team_name):
        total_matches = 0
        total_wins = 0
        total_losses = 0
        total_draws = 0

        for match in self.matches.values():
            if match.team1.name == team_name:
                total_matches += 1
                if match.winner == team_name:
                    total_wins += 1
                elif match.winner == "Draw":
                    total_draws += 1
                else:
                    total_losses += 1
            elif match.team2.name == team_name:
                total_matches += 1
                if match.winner == team_name:
                    total_wins += 1
                elif match.winner == "Draw":
                    total_draws += 1
                else:
                    total_losses += 1

        return {
            "Total Matches Played": total_matches,
            "Total Wins": total_wins,
            "Total Losses": total_losses,
            "Total Draws": total_draws
        }

# Example usage
if __name__ == "__main__":
    # Create Match_Result_Tracker instance
    tracker = Match_Result_Tracker()

    # Create teams
    team1 = Team("Mumbai Indians")
    team2 = Team("Chennai Super Kings")
    team3 = Team("Royal Challengers Bangalore")
    team4 = Team("Kolkata Knight Riders")
    team5 = Team("Delhi Capitals")
    team6 = Team("Gujarat Titans")

    # Schedule matches
    tracker.create_match(team1, team2)
    tracker.create_match(team3, team6)
    tracker.create_match(team1, team4)
    tracker.create_match(team5, team6)
    tracker.create_match(team1, team6)
    tracker.create_match(team2, team3)
    tracker.create_match(team4, team5)
    tracker.create_match(team3, team4)
    tracker.create_match(team2, team5)
    print()
    
    # Delete a match
    tracker.delete_match(3)
    print()

    # Display match details after deletion
    tracker.display_match_details(10)  # This will show "Match 10 not found"
    print()



    # Update match scores
    tracker.update_match_score(1, 180, 170)
    tracker.update_match_score(2, 150, 150)
    tracker.update_match_score(3, 206, 217)
    tracker.update_match_score(4, 166, 186)
    tracker.update_match_score(5, 127, 168)
    tracker.update_match_score(6, 175, 172)
    tracker.update_match_score(7, 257, 201)
    tracker.update_match_score(8, 188, 134)
    tracker.update_match_score(9, 238, 212)
    print()
    

    # Display match details
    tracker.display_match_details(1)
    tracker.display_match_details(2)
    tracker.display_match_details(3)
    tracker.display_match_details(4)
    tracker.display_match_details(5)
    tracker.display_match_details(6)
    tracker.display_match_details(7)
    tracker.display_match_details(8)
    tracker.display_match_details(9)
    tracker.display_match_details(10)  # This will show "Match 10 not found"
    print()
    

    
    # Display team statistics for each team one below the other in a dictionary format
    teams = [team1, team2, team3, team4, team5, team6]
    for team in teams:
        team_stats = tracker.team_statistics(team.name)
        print(f"Team: {team.name}")
        for key, value in team_stats.items():
            print(f"{key}: {value}")
        print()
        
    
