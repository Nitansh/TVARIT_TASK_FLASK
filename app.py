# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13...19
# inclusive -- then that value counts as 0, except 15 and 16 do not count as a teen. The input is passed as
# command line arguments and output is to be printed on screen
import json
from flask import Flask, request

from constant import ACTUAL_TEEN_LIST, ERROR_MSG_INVALID_INPUT, ERROR_MSG_INVALID_COUNT_ARGS, ARGS_ALLOWED
from validation import validate_arguments_length, get_converted_args
from logic import calculate_sum

app = Flask(__name__)

@app.route( '/sum', methods=['POST'] )
def main():
  actual_args = request.get_json()
  if validate_arguments_length( actual_args, ARGS_ALLOWED ):
    if get_converted_args( actual_args ):
      return app.response_class(
        response=json.dumps( { "result" : calculate_sum( get_converted_args( actual_args ), ACTUAL_TEEN_LIST ) } ),
        status=200,
        mimetype='application/json',
      )
    else :
      return app.response_class(
        response=json.dumps( { 'error' : ERROR_MSG_INVALID_INPUT } ),
        status=400,
        mimetype='application/json',
      )
  else:
    return app.response_class(
      response=json.dumps( { 'error' : ERROR_MSG_INVALID_COUNT_ARGS } ),
      status=400,
      mimetype='application/json',
    )

if __name__ == '__main__':
  app.run( host ='0.0.0.0', port = 5001, debug = False )
