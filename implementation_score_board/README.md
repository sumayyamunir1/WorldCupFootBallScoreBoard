# World Cup Football Score Board

This project implements a Score Board for tracking football matches during the World Cup.
This allow users to add games, update scores and get the summary of total scores.
The user will have a Menu to selection an option.
1. Start a game
2. Update score
3. Get a summary of Games by total score
4. Remove all games from Score board
5. Exit

# The project structure is organized as following:

WORLDCUPFOOTBALLSCOREBOARD/
implementation_score_board/   -> this file contains the implementation of all functions
score_board.py
test/
test_score_board.py   -> this file contains all the test cases for score board

## Installation

1. Clone this repository to your local machine.
   git clone <repository_url>
2. Go to the project directory.
   cd project , in my case it is WorldCupFootballScoreBoard
3. Run the tests to ensure everything is set up correctly
python -m unittest discover -s test
4. Run the test cases by going into project root direstory, and run each test seperately by using the follwoing command:
python -m unittest "testFolderName.testFileName.testClassName.testName
In my case,I use this command to run each test by changing the test name at the end of this command
python -m unittest test.test_score_board.TestScoreBoard.test_single_game_start
5. Run the Score Board functionality, go to project implementation file.In my case, cd implementation_score_board -> run the command "python score_board.py"

## Usage

1. Import the ScoreBoard and Game class from `implementation/score_board.py` into your Python script.In my case it is... 
from implementation_score_board.score_board import ScoreBoard, Game
2. Create the object of ScoreBoard to start tracking games:
scoreboard = ScoreBoard()
3. Call the game_start() function to start adding games:
scoreboard.game_start()
Ask user to enter the number of games for ScoreBoard, then ask user to enter home team, away team for each game and add scores to each team.
4. View the summary of Scores for each team:
scoreboard.get_summary()
5: Update the Score for existing games using:
scoreboard.update_score()
5. Remove games from Score Board using:
   scoreboard.remove_all_games()
6. Exit the program by selecting the option number 5 from the Menu.


## Assumptions and Solutions from my Side:

1. The implementation assumes that the user input will be valid input when add or update a game. The functionality does not works for invalid inputs like invalid team names or non-integer scores.
2. The implementation of adding scores only support integer data for games. The Game class attributes can be updated according to the other data types if there is a need.
3. Currently Scoreboard can take unlimited number of games to be added. We can set the limit number of games to be added.
4. The program keep track of games in memory at the time of execution only and lost data when the program terminated. We can use database or file system to store games data to be used later.
5. The project is using built-in åython modules for testing  like unittest.mock and unittest. We can consider using "pytest" and "coverage" for advanced testing.