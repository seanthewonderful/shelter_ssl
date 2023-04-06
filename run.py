from flaskr import app

if __name__ == "__main__":
    from os import system
    system("source config.sh")
    app.run()