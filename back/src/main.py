from app import app
import model.automate
import model.unite
import sys

sys.dont_write_bytecode = True	

# def converter(o):
#     if isinstance(o, (datetime.date, datetime.datetime)):
#         return o.timestamp()

# def toJSON(data):
#     return json.dumps(data, default=converter)

if __name__ == "__main__":
    app.run(debug=True)
