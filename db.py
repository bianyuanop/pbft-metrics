import pymysql

class EdgeStore:
    def __init__(self) -> None:
            self.conn = pymysql.connect(host = 'localhost',
                                user = 'chan',
                                password='Diy.2002',
                                database='pbft',
                                cursorclass=pymysql.cursors.DictCursor)
    
    def pickByRound(self, round: int):
        sql = f"SELECT * FROM edges where round={round}"
        cursor = self.conn.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

        
