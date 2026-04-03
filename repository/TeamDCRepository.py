import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host':os.getenv('DB_HOST'),
    'port':os.getenv('DB_PORT'),
    'dbname':os.getenv('DB_NAME'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD')
}
def get_connection():
    return psycopg2.connect(**DB_CONFIG)

class TeamDCRepository:
    def create_table(self,conn):
        create_sql="""
        create table if not exists team_dc_players(
            id serial primary key,
            name varchar(100) not null,
            height decimal(6,2) not null,
            weight decimal(6,2) not null,
            games_played int not null,
            created_at timestamp default current_timestamp
        );
        """
        with conn.cursor() as cursor:
            cursor.execute(create_sql)
            conn.commit()
    def save_player(self,model):
        insert_sql="""
        insert into team_dc_players(name,height,weight,games_played)
        values(%s,%s,%s,%s)
        returning id;
        """
        conn=None
        try:
            conn=get_connection()
            self.create_table(conn)
            with conn.cursor() as cursor:
                cursor.execute(insert_sql,(model.get_name(),model.get_height(),model.get_weight(),model.get_games_played()))
                player_id=cursor.fetchone()[0]
                conn.commit()
            return player_id
        except Exception as e:
            print("Error saving player: ", e)
        finally:
            if conn:
                conn.close()