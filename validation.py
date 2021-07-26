def validate_arguments_length( args, ARGS_ALLOWED ):
  actual_args_passed = len( args )
  return actual_args_passed == ARGS_ALLOWED

def get_converted_args( args ):
  try:
    return [ int( i ) for i in args ]
  except ValueError:
    return False
