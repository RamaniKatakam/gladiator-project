from controller.TeamDCController import TeamDCController
from model.TeamDC import TeamDC

def main():
    team_dc_controller = TeamDCController()
    team_dc_model=TeamDC()
    for _ in range(1):
            team_dc_controller.request_processor(team_dc_model)

if __name__=="__main__":
    main()