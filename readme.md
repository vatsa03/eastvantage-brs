This app is continerized and pushed to docker hub.
The image can be found here: https://hub.docker.com/r/kvatsa/eastvantage

Prerequisites:

```docker```

To start the app run the following commands:

```
docker pull kvatsa/eastvantage
docker run -p 8000:8000 kvatsa/eastvantage
```

Theoretical Question answers:
- Question 1: Explain how FastAPI handles asynchronous requests and its
benefits over synchronous code in Python.

FastAPI leverages Python's async/await syntax to define asynchronous endpoints and functions. By marking certain functions with async, you can make them awaitable, allowing the server to handle other requests while waiting for I/O-bound operations to complete.
Also FastAPI is designed to be ASGI compliant. ASGI allows the server to process HTTP requests asynchronously. This means that FastAPI can handle a large number of concurrent connections efficiently.

- Question 2: Describe how dependency injection works in FastAPI and give an
example of its practical use.

In the code of Book review system get_db is an example of dependency injection
Example:
```
@app.post("/books/get_review")
def get_review(title: str, db: Session = Depends(get_db)):
    query = db.query(Review)
    query = query.filter(Review.title == title)
    reviews = query.all()
    return reviews
```
