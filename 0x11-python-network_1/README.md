# 0x11. Python - Network #1

## Learning Objectives


- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` #requestsiswaysimplerthanurllib
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

### Tasks

_**0. What's my status? #0**_  
Write a Python script that fetches `https://intranet.hbtn.io/status`  

_**1. Response header value #0**_  
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.  

_**2. POST an email #0**_  
Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)  

_**3. Error code #0**_  
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).  

_**4. What's my status? #1**_  
Write a Python script that fetches `https://intranet.hbtn.io/status`  

_**5. Response header value #1**_  
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header  

_**6. POST an email #1**_  
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.  

_**7. Error code #1**_  
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.  

_**8. Search API**_  
Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.  

_**9. My Github!**_  
Write a Python script that takes your Github credentials (username and password) and uses the [Github API](https://developer.github.com/v3/users/#get-the-authenticated-user) to display your `id`  
