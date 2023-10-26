"""
    task6_1_starter.py  -   Module for the School and SchoolManger classes

    Class module for our School and SchoolManager classes.

    The School class simply holds information about school data.
    The SchoolManager is used to connect to and query against
    the course_data.db sqlite3 database.

    -------------------------------------------------------------------------

    Helpful Hints:
    1. Create the School class with the following attributes:
        school_id, fullname, city, state, country

    2. In the __init__, pass in parameters for each and set them as instance attributes


    -------


    3. Create the SchoolManager class beneath School.  Define two methods:
        __init__() and find()

        Remember each method should have a self passed in.

        For now, just put a 'pass' statement in the body of each method.



    4. Complete the __init__() by passing into it the name of the database file
       that we are working with (course_data.db).  Save the filename as an
       attribute in the self object (e.g., self.name = name)



    5. The find() method should accept 3 arguments: the search term,
       the column to search on, and the column to sort on.  Here's
       a possible way to define it:

       def find(self, value, column, sort_by):
           pass



    6. Implement the find() method.

       Connect to and work with the database in a similar fashion
       as you did in task5_1_starter.py.

       You may use the following sql (you can optionally define it in the class outside of any methods):
            SELECT_SCHOOLS_SQL = 'SELECT school_id, fullname, city, state, country FROM schools WHERE column like ?'


       * Note the WHERE clause! The column name in the WHERE clause is variable.  But you
       * can't make this a question mark (?) due to SQL injection concerns.

       * You can however replace the word 'column' using the string class' replace() method.  But you
       * can only replace it with an approved list of columns names, you can't replace it with
       * user input.

       * The following code can be used to insert the variable column name:

       PERMITTED_SEARCH_COLUMNS = ['fullname', 'city', 'state', 'country']   # place at the class level

       # in find():
       if column in self.PERMITTED_SEARCH_COLUMNS:
            self.SELECT_SCHOOLS_SQL = self.SELECT_SCHOOLS_SQL.replace('column', column)


	   As done in the get_location() method of task5_1_starter.py, connect to, query,
	   and build a list of School objects from the database.



    7. Sort your results based on the provided sort_by value.  You can use the
       following to help:

               results.sort(key=lambda s: vars(s).get(sort_by))

       This converts the school object, s, into a dictionary and then sorts on
       the desired key of that dictionary.



    8. Don't forget to return your results from the find() function

"""
from contextlib import closing
import sqlite3

class School:
    def __init__(self, school_id, fullname, city, state, country):
        self.school_id = school_id
        self.fullname = fullname
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        return f'{self.fullname} ({self.city}, {self.state})'

    __repr__ = __str__


# The SchoolManager class has been started for you, you should complete the
# __init__() and find() methods as described in the hints above.
class SchoolManager:

    PERMITTED_SEARCH_COLUMNS = ['fullname', 'city', 'state', 'country']

    def __init__(self, db_filename):
        self.db_filename = db_filename

    def find(self, value, column='fullname', sort_by='fullname'):
        results = []
        SELECT_SCHOOLS_SQL = f'SELECT school_id, fullname, city, state, country FROM schools WHERE {column} like ?'

        if column in self.PERMITTED_SEARCH_COLUMNS:
            with closing(sqlite3.connect(self.db_filename)) as conn:
                cursor = conn.cursor()
                params = ('%' + value + '%',)
                cursor.execute(SELECT_SCHOOLS_SQL, params)

                for record in cursor:
                    results.append(School(*record))
        # print(vars(results[0]))
        results.sort(key=lambda s: vars(s).get(sort_by))

        return results

# test your solution out by running the code below and verifying that it works
if __name__ == '__main__':
    print(SchoolManager('course_data.db').find('Loyola'))
    print(SchoolManager('course_data.db').find('ID', column='state', sort_by='state'))

    print('\nThis is how the code can break:')
    s1 = SchoolManager('course_data.db')
    print(s1.find('Loyola', column='fullname'))
    print(s1.find('ID', column='state', sort_by='fullname'))

    # print(s1.SELECT_SCHOOLS_SQL)
    # s1.SELECT_SCHOOLS_SQL = 'Some really dangerous SQL'
    # print(s1.SELECT_SCHOOLS_SQL)
