import pymysql


class DB_OP:
    def __init__(self, host='localhost', db='mysql', user='root', pwd=None):
        self.host = host
        self.db_name = db
        self.user = user
        if pwd is None:
            print("[Err DB_OP]===> {0}:{1}:{2} need password ".format(host, db, user))
        else:
            self.pwd = pwd
        try:
            self.handle = pymysql.connect(self.host, self.user, self.pwd, self.db_name)
        except Exception as e:
            print("Err occured in DB_OP __init__")
            exit(-1)
        self.cursor = self.handle.cursor()

    """
    def DB_Connect(self):

        cursor = self.handle.cursor()
        return cursor
    """