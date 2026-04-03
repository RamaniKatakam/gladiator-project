class TeamDCView:
    def display_player_info(self,team_dc):
        print("Player Name: ", team_dc.get_name())
        print("Player Height: ", team_dc.get_height())
        print("Player Weight: ", team_dc.get_weight())
        print("Games Played: ", team_dc.get_games_played())