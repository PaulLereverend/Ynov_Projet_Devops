from automate.src import app
import sys

if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        app.run(sys.argv[1])