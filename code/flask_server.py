"""Simple flask server to display data.

It uses two different routes in order to show routing stuff in flask.
For the demo go to => APP_ADDRE:APP_PORT/1 (ie: http://localhost:8000/1)
"""

from flask import Flask
from flask import render_template

from ploting_utils import line_plot
from datasource import SerialReader

app = Flask(__name__)

sr = SerialReader()
sr.start()


@app.route('/')
def index():
    """Index view of the app."""
    return "\o/"


@app.route('/<int:device>')
def hello_world(device):
    """Device view of the app."""
    if device == 1:
        ts, hums, temps = sr.get_data()
        datas = [line_plot(ts, hums), line_plot(ts, temps)]
        return render_template("ok.html", plots=datas)
    else:
        error = "Unknown device {}".format(device)
        return render_template("error.html", error=error)


def main():
    """Run the code of the file."""
    app.run(debug=False)


if __name__ == '__main__':
    main()
