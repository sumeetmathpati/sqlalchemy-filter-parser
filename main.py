from parser import parser
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import DownloadEvents, Downloads

engine = create_engine("postgresql+psycopg2://sumeet:@localhost/postgres")
Session = sessionmaker(bind=engine)

# Open a session to interact with your database
session = Session()

# Retrieve data from your table
data = session.query(Downloads)

filters = parser.parse(data, session, "tenant in s , iris")

filters = [f.subquery() for f in filters]
data = session.query(*filters)
print(list(data))


# Close the session when you're done
session.close()