# from Medium.medium import Medium
#
#
# if __name__ == '__main__':
#     query = 'SELECT userid, count(userid), occupation FROM users WHERE gender=M GROUP by occupation having age>16'
#     # query = 'SELECT movieid, title, count(Adventure) FROM movies WHERE Adventure=1 GROUP by title having releasedate>01-JAN-1970'
#     # query = 'SELECT movieid, title, count(Adventure) FROM movies WHERE Adventure=1'
#     # query = 'SELECT * FROM movies WHERE Adventure=1'
#     medium = Medium(query)
#     medium.run()

from Medium.medium import Medium
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/Zenoh/rest', methods=['GET'])
def rest_service():
    query_parameters = request.args
    print(query_parameters.get('query'))
    query = str(query_parameters.get('query'))
    #query = 'SELECT userid, count(userid), occupation FROM users WHERE gender=M GROUP by occupation having age>16'
    #print(query)
    medium = Medium(query)
    result = medium.run()
    print('--------------In INITIATE - SENDING JSON TO POSTMAN---------------------')
    # print(result)
    # finalResult = { }

    return jsonify(result)

if __name__ == '__main__':
    app.run()