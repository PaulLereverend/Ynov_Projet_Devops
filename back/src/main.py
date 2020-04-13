from app import app
# from flask import jsonify, flash, request
# from flask_restful import Resource, Api
import model.automate
import model.unite
import sys

sys.dont_write_bytecode = True	

if __name__ == "__main__":
    app.run(debug=True)
