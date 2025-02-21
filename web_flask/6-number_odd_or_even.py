#!/usr/bin/python3
"""script that starts Flask web app display HTML page only if n is an int"""

from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ('/')

    Returns:
        str: A simple greeting message
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the '/hbnb' URL

    Returns:
        str: The string "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the '/c/<text>' URL

    Args:
        text (str): The text provided in the URL

    Returns:
        str: The string "C " followed by the value of the text variable
    """
    return "C {}".format(escape(text.replace("_", " ")))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route handler for the /python/ URL with default value and /python/text URL

    Args:
        text (str): The text provided in the URL

    Returns:
        str: The string "Python " followed by the value of the text variable
    """
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Route handler for the '/number/<n>' URL with a number parameter

    Args:
        n (int): The numeric value provided in the URL

    Returns:
        str:string "{n} is a number" if n is int, else a 404 Not Found error
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for the '/number_template/<n>' URL with a number parameter

    Args:
        n (int): The numeric value provided in the URL

    Returns:
        str:HTML page displaying the number in an H1 tag inside the BODY tag
    """
    return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler for the /number_odd_or_even/<n> URL with a number parameter

    Args:
        n (int): The numeric value provided in the URL

    Returns:
        str:HTML page display if number is odd or even in H1 tag in  BODY tag
    """
    return render_template('6-number_odd_or_even.html', number=n,
                           odd_even='odd' if n % 2 != 0 else 'even')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
