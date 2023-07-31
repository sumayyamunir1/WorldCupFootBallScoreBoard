import unittest
import sys
from unittest.mock import patch
sys.path.append("..") 
from implementation_score_board.score_board import ScoreBoard, Game

class TestScoreBoard(unittest.TestCase):
    # test case to check if the game is added to score board correctly
    def test_single_game_start(self):
        scoreboard_obj=ScoreBoard()
        i_user= "1\nCanada\nAustralia\n13\n34\n1\n"
        
        # use patch to replace the built-in input funtion with our predefined input during the test
        with patch("builtins.input", side_effect=i_user.split()):
             scoreboard_obj.game_start()
             self.assertEqual(len(scoreboard_obj.games), 1)
             
             # Assert that the added game has the correct scores
             game_add = scoreboard_obj.games[0]
             self.assertEqual(game_add.home_team, "Canada")
             self.assertEqual(game_add.away_team, "Australia")
             self.assertEqual(game_add.home_score, 13)
             self.assertEqual(game_add.away_score, 34)

    def test_multiple__or_empty_game_start(self):  
        scoreboard_obj=ScoreBoard()
        expected_games = [
            ("Canada", "Australia", 13, 34),
            ("Liverpool", "America", 30, 31),
            ("", "Malta", 60, 50),
            ("France", "", 50, 50),
            ("", "", 50, 50)
        ]   
        
        with patch("builtins.input") as mock_input:
            user_entered_games= [str(len(expected_games))] 
            for game in expected_games: 
                 # Enter name of team and their scores
                 # converts each item in the game to a string
                user_entered_games.extend(str(item) for item in game) 
            mock_input.side_effect = user_entered_games 

            #call the game_start method for multiple games
            user_entered_games.append('1')
            scoreboard_obj.game_start()
        actual_games= scoreboard_obj.games
        self.assertEqual(len(actual_games),len(expected_games))

        for i, game in enumerate(scoreboard_obj.games):
                home_team, away_team, home_score, away_score = expected_games[i]
                self.assertEqual(game.home_team, home_team)
                self.assertEqual(game.away_team, away_team)
                self.assertEqual(game.home_score, home_score)
                self.assertEqual(game.away_score, away_score)

        self.assertNotIn(Game("", "Malta",60,50), actual_games)
        self.assertNotIn(Game("France", "",50,50), actual_games)
        self.assertNotIn(Game("", "",50,50), actual_games)

    def test_update_score_game_exist(self):    
        scoreboard_obj=ScoreBoard()  
        game = Game("LONDON", "BRAZIL", 2, 1)
        scoreboard_obj.add_game(game)

        with patch("builtins.input", side_effect=["LONDON", "BRAZIL", 79, 2]):
            scoreboard_obj.update_score()

        updated_game = scoreboard_obj.games[0] 
        self.assertEqual(updated_game.home_score, 79)
        self.assertEqual(updated_game.away_score, 2)

    def test_update_score_game_not_exist(self):    
        scoreboard_obj=ScoreBoard()  
        game = Game("LONDON", "BRAZIL", 2, 1)
        scoreboard_obj.add_game(game)

        with patch("builtins.input", side_effect=["BArbara", "Banglore"]):
            scoreboard_obj.update_score()
        #verify that the score for the game does not changed
        updated_game = scoreboard_obj.games[0] 
        self.assertEqual(updated_game.home_score, 2)
        self.assertEqual(updated_game.away_score, 1)    


    def test_update_score_empty_scoreboard(self):
        scoreboard_obj = ScoreBoard()  
        
        #update the score when there are no games in the score board
        with patch("builtins.input", side_effect=["LONDON", "BRAZIL", 79, 2]):
            scoreboard_obj.update_score()

        #verify that the game list in the score board is empty
        self.assertEqual(len(scoreboard_obj.games), 0)

    def test_get_summary(self):    
        scoreboard_obj = ScoreBoard() 
        #adding games in Scoreboard 
        g1 = Game("LONDON", "BRAZIL", 2, 1)
        g2 = Game("America", "Norway", 56, 90)
        g3 = Game("Sweden", "Denmark", 30, 30)
        g4 = Game("Haland", "Finland", 25, 25)
        scoreboard_obj.add_game(g1)
        scoreboard_obj.add_game(g2)
        scoreboard_obj.add_game(g3)
        scoreboard_obj.add_game(g4)

    def test_get_summary_no_games(self):
        scoreboard_obj = ScoreBoard() 
       
        with patch("builtins.print") as mock:
            scoreboard_obj.get_summary()
            expected = "No games found in the scoreboard."
            mock.assert_called_with(expected)

       


if __name__ == '__main__':
    unittest.main()