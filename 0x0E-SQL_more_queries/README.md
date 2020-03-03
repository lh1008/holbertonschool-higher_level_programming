# 0x0E. SQL - More queries

## Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

## Tasks

_**0. My privileges!**_  
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

_**1. Root user**_  
Write a script that creates the MySQL server user `user_0d_1`.

_**2. Read user**_  
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

_**3. Always a name**_  
Write a script that creates the table `force_name` on your MySQL server.

_**4. ID can't be null**_  
Write a script that creates the table `id_not_null` on your MySQL server.

_**5. Unique ID**_  
Write a script that creates the table `unique_id` on your MySQL server.

_**6. States table**_  
Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

_**7. Cities table**_  
Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

_**8. Cities of California**_  
Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

_**9. Cities by States**_  
Write a script that lists all cities contained in the database `hbtn_0d_usa`.

_**10. Genre ID by show**_  
Import the database dump from `hbtn_0d_tvshows` to your MySQL server.  
Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

_**11. Genre ID for all shows**_  
Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

_**12. No genre**_  
Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

_**13. Number of shows by genre**_  
Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

_**14. My genres**_  
Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

_**15. Only Comedy**_  
Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

_**16. List shows and genres**_  
Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.
