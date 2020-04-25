from app import app
import model.automate
import model.unite
import sys

sys.dont_write_bytecode = True

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
