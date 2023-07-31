class Game:
    def __init__(self, home_team, away_team, home_score, away_score):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score

class ScoreBoard:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def remove_all_games(self):
        #this will clear all games from list of games
        self.games.clear()
        print("All games have been removed")       

    def display_scores(self):
        #check if list of games is empty
        if not self.games:
            print("There are no games to display.")
            return

        #show all the Teams Scores if there are games in the list
        print("Scores for all teams")
        for game in self.games:
            print("Scores for team  "+ game.home_team + " is " +str(game.home_score) + " : Scores for team " + game.away_team + " is " + str(game.away_score))
     
    #this function will start getting the games 
    def game_start(self):
        # ask user to enter the number of total games
        num_games = int(input("Enter the number of games: "))
        # Ask the user to enter team names and scores
        for i in range(num_games):
            print("Add Scores for Game number ", i + 1)
            home_team = input("Enter name of home team: ")
            away_team = input("Enter name of away team: ")
            home_score = int(input("Enter scores for home team " + home_team + ": "))
            away_score = int(input("Enter scores for away team " + away_team + ": "))

            #created an object of Game class and add it to the Scorbaord
            game= Game(home_team, away_team, home_score, away_score)
            #this function will add game object to the games list
            self.add_game(game) 
            print("Your score for Games has been entered")  

        user_choice = int(input("Do you want to see the added scores? Press 1 for YES: "))
        if user_choice == 1:
            #this function call will display all the added scores of games
            self.display_scores()
        else:
            #print invalid choice if a user enter anything else than 1
            print("Invalid choice!")     

    def update_score(self):
        #ask the user to enter the team names to update the score for
        print("Enter the details of the game to update:")
        home_team = input("Enter name of home team: ")
        away_team = input("Enter name of away team: ")
        updated = False
        for game in self.games:
            if game.home_team == home_team and game.away_team == away_team:
                home_score = int(input("Enter new score for " + home_team + ": "))
                away_score = int(input("Enter new score for " + away_team + ": "))
                game.home_score = home_score
                game.away_score = away_score
                updated = True
                break  

        if updated:
            print("Game score has been updated successfully.")
            #this function will be called and display the updated scores
            self.display_scores()
        else:
            print("Game with the entered teams not found in the scoreboard.")          

    def get_summary(self):
        #check if there is no game in the ScoreBoard
        if not self.games:
            print("No games found in the scoreboard.")
            return
        #if there are games in score board 
        sorted_games = sorted(self.games, key=lambda game: (game.home_score == game.away_score, game.home_score + game.away_score), reverse=True)
        #initialize the list for games with same total score
        same_total_score_games = []
        other_games = []

        for game in sorted_games:
            if any(g for g in same_total_score_games if g.home_score + g.away_score == game.home_score + game.away_score):
                same_total_score_games.append(game)
            else:
                other_games.append(game)

        summary_total_games = same_total_score_games + other_games
        print("Summary of Games by Total Score:")
        for game in summary_total_games:
            print("Scores for team  "+ game.home_team + " is " +str(game.home_score) + " : Scores for team " + game.away_team + " is " + str(game.away_score))
            

def main():
    scoreboard = ScoreBoard()
    menu=str(input("Press M to see the menu  :"))
    while menu== "M" or menu=="m":
        print("\nMenu:")
        print("1. Start a game")
        print("2. Update score")
        print("3. Get a summary of Games by total score")
        print("4. Remove all games from Score board")
        print("5. Exit")
        choice = int(input("Enter your choice...: "))

        if choice == 1:
            scoreboard.game_start()
        elif choice == 2:
            scoreboard.update_score()
        elif choice == 3:
            scoreboard.get_summary()
        elif choice == 4:
            scoreboard.remove_all_games()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select options from 1 to 5")


if __name__ == "__main__":
    main()
