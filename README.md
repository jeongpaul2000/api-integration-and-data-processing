# This project repository features:
- 1. A local endpoint responding to curl GET
'localhost:3000/hello_world' with a 200 status and
{"hello": "world"}

- 2. A testing framework set up with one test that runs
and asserts 1==1

Additional branches contain devations of the code for experimentation/learning of the API environment

# Dependencies
- flask requests pytest (pip install)

# How to Create Local Endpoint

In your first terminal:
- run `python app.py` (Sets up the server)

In another terminal:
- run `curl http://localhost:5000/hello_world`
- you should see the proper JSON response ()

# How to Pass a Test
- run pytest
