from sqlalchemy import create_engine
class DbEngine:
    def __init__(self,user,password,host,db_name):
        self.user=user
        self.password=password
        self.host=host
        self.db_name=db_name
    def get_engine(self):
        engine = create_engine('postgresql+psycopg2://{user}:{password}@{host}/{db_name}'
                .format(user=self.user,password=self.password,host=self.host,db_name=self.db_name))
        return engine
