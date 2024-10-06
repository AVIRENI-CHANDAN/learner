from backend import create_app

app = create_app()


@app.get("/")
def index():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    app.run(debug=True)
