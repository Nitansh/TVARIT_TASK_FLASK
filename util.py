import json

def get_response( app, status, response, error, mime = 'application/json' ):
  return app.response_class(
    response = json.dumps( { "error" : response } ) if error else json.dumps( { "result" : response } ),
    status = status,
    mimetype = mime,
  )