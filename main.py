import fastapi

app = fastapi.FastAPI()

@app.post('/login')
def login():
    """ 
    Authenticates a user using email or phone number.
    Returns a token on success.

    request body:
     - username or phone number: unique identification for user
     - password
    """
    return "Fake token"