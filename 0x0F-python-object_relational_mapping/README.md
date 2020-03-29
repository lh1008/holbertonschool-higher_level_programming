# 0x0F. Python - Object-relational mapping

## Learning Objectives

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

`SQLAlchemy` & `MySQLdb`

## Tasks

_**0. Get all states**_  
Write a script that lists all states from the database `hbtn_0e_0_usa`  

_**1. Filter states*_  
Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`.  

_**2. Filter states by user input**_  
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.  

_**3. SQL Injection...**_  
Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!  

_**4. Cities by states**_  
Write a script that lists all `cities` from the database `hbtn_0e_4_usa`  

_**5. All cities by state**_  
Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`  

_**6. First state model**_  
Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`  

_**7. All states via SQLAlchemy**_  
Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`  

_**8. First state**_  
Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`  

_**9. Contains `a`**_  
Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`  

_**10. Get a state**_  
Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`  

_**11. Add a new state**_  
Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`  

_**12. Update a state**_  
Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`  

_**13. Delete states**_  
Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`  

_**14. Cities in state**_  
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.  
