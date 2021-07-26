import unittest

from constant import ACTUAL_TEEN_LIST, ERROR_MSG_INVALID_INPUT, ERROR_MSG_INVALID_COUNT_ARGS, ARGS_ALLOWED
from validation import validate_arguments_length, get_converted_args
from logic import calculate_sum

class TestLogicAndValidation( unittest.TestCase ):

    def test_argument_length( self ):
      self.assertEqual( validate_arguments_length( [ 1, 2], 2 ), True )
      self.assertEqual( validate_arguments_length( [ 1 ], 1 ), True )
      self.assertEqual( validate_arguments_length( [ 1, 2], 1 ), False )
      self.assertEqual( validate_arguments_length( [ 1, 2, 3 ], 2 ), False )

    def test_get_converted_args( self ):
      self.assertEqual( get_converted_args( [ '1', '2' ] ), [ 1, 2 ] )
      self.assertEqual( get_converted_args( [ '1', 'a' ] ), False )

    def test_calculate_sum( self ):
      self.assertEqual( calculate_sum( [1, 2, 3 ], ACTUAL_TEEN_LIST ), 6 )
      self.assertEqual( calculate_sum( [1], [1] ), 0 )
      self.assertEqual( calculate_sum( [1,4,5], [1,2,3] ), 9 )
      self.assertEqual( calculate_sum( [1,10,5], [1,2,10] ), 5 )

if __name__ == '__main__':
    unittest.main()