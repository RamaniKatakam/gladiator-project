from model.TeamDC import TeamDC
from repository.TeamDCRepository import TeamDCRepository
from view.TeamDCView import TeamDCView
team_dc_model = TeamDC()
team_dc_view = TeamDCView()


class TeamDCController:
    def __init__(self):
        self.repo=TeamDCRepository()
    def request_processor(self,team_dc_model):
        name=input("Enter Player Name: ")
        team_dc_model.set_name(name)
        height=float(input("Enter Player Height(cm): "))
        team_dc_model.set_height(height)
        weight=float(input("Enter Player Weight(kg): "))
        team_dc_model.set_weight(weight)
        games_played=int(input("Enter Games Played: "))
        team_dc_model.set_games_played(games_played)
        team_dc_view.display_player_info(team_dc_model)
        player_id=self.repo.save_player(team_dc_model)
        print("Player saved with ID: ", player_id)

team_dc_controller = TeamDCController()

#for i in range(4):
team_dc_controller.request_processor(team_dc_model)
