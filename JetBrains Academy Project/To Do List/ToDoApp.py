from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, date
from sqlalchemy.orm import sessionmaker


# Making Engine
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# Once you've created your database file, you need to create a table in it. First, create a model class that
# describes the table in the database. All model classes should inherit
# from the DeclarativeMeta class that is returned by declarative_base():
Base = declarative_base()

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field

# After we've described our table, it's time to create it in our database. All we need is to call the create_all()
# method and pass engine to it:
Base.metadata.create_all(engine)

# This method creates a table in our database by generating SQL queries according to the models we described.
# Now we can access the database and store data in it. To access the database, we need to create a session:
Session = sessionmaker(bind=engine)
session = Session()

# The session object is the only thing you need to manage the database. To create a row in our table,
# you need to create an object of the model class and pass it to the add() method:
# --------------------------------------------------------------------------------------------------------------
# new_row = Table(string_field='This is string field!',
#          date_field=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
# session.add(new_row)
# session.commit()
# ---------------------------------------------------------------------------------------------------------------

# To get all rows from the table, you can pass the model class to the query() method that selects all rows
# from the table represented by a model class:
# -----------------------------------------------------------
# rows = session.query(Table).all()
# -----------------------------------------------------------
# The all() method returns all rows from the table as a Python list.
# Each element of this list is an object of the model class. You can access the row fields by their names:
# -----------------------------------------------------------------------------------------------------------------
# first_row = rows[0] # In case rows list is not empty
#
# print(first_row.string_field) # Will print value of the string_field
# print(first_row.id) # Will print the id of the row.
# print(first_row) # Will print the string that was returned by __repr__ method
# ------------------------------------------------------------------------------------------------------------------

menu = '''1) Today's tasks
2) Add task
0) Exit'''

def main_menu():
    while True:
        print(menu)
        menu_input = input()
        if menu_input == '1':
            print()
            today_task()
        if menu_input == '2':
            print()
            add_task()
        if menu_input == '0':
            print()
            print('Bye!')
            exit()

def add_task():
    print('Enter task')
    to_add = input()
    new_row = Table(task=to_add)
    session.add(new_row)
    session.commit()
    del new_row


    print('The task has been added!')
    print()

def today_task():
    print('Today:')
    rows = session.query(Table).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for x in range (len(rows)):
            first_row = rows[x]
            print(f'{first_row.id}. {first_row.task}')
    print()


main_menu()