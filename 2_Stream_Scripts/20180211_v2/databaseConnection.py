import sqlite3

class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS DPSpace (id integer, hand text, position integer, pot integer,chip_player1 integer,chip_player2 integer,chip_player3 integer,chip_player4 integer,chip_player5 integer,chip_player6 integer, nrGames integer, previous_action text, action text)")
        self.conn.commit()

    def checkDP(self, hand, position, pot, chip_player1, chip_player2, chip_player3, chip_player4, chip_player5, chip_player6, nrGames, previous_action="Null"):
        #previous action is null as default in case there are no previous actions
        #search database for match
        self.cur.execute("SELECT * FROM book WHERE hand = ? AND position = ? AND pot = ? AND chip_player1 = ? AND chip_player2 = ? AND chip_player3 = ? AND chip_player4 = ? AND chip_player4 = ? AND chip_player5 = ? AND chip_player6 = ?", (hand,position,pot,chip_player1,chip_player2,chip_player3,chip_player4,chip_player5,chip_player6))
        rows= self.cur.fetchall()
        #see how many results there are
        if len(rows) == 1: # if there does exist a decision point then return the action taken with that decision point
            return rows[11]#index of the action column
        elif len(rows) == 0: #if there are no decision points return 0 to tell the script to add the info to the DPS.
            return 0

    def __del__(self):
        self.conn.close()
