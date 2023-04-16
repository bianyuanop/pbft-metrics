import pymysql

class EdgeStore:
    def __init__(self) -> None:
            self.conn = pymysql.connect(host = 'localhost',
                                user = 'chan',
                                password='Diy.2002',
                                database='pbft',
                                cursorclass=pymysql.cursors.DictCursor)
    
    def pickByRound(self, round: int):
        sql = f"SELECT * FROM edges where round={round} ORDER BY ts"
        cursor = self.conn.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def pickFromTo(self, start: int, end: int):
        sql = f"SELECT * FROM edges where round >= {0} AND round <= {end} ORDER BY ts"

        cursor = self.conn.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def pickByNumMessages(self, count: int):
        sql = f"SELECT * FROM edges ORDER BY ts LIMIT {count} "

        cursor = self.conn.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
        


        
