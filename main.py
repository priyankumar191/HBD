from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("Happy Birthday!", P("Wishing you a great day! 🎉"))

# Serve locally when running `python main.py`
if __name__ == "__main__":
    serve()