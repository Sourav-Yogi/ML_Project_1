import sys
import logging
from src.logger import logging

def error_message_details(error, error_detail: sys):
    # Extract exception details (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()

    # Get the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Get the exact line number where the exception occurred
    line_number = exc_tb.tb_lineno

    # Create a formatted error message with file name, line number, and error details
    error_message = "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message  # Return the formatted error message
    

class CustomException(Exception):  
    # Custom exception class that extends the built-in Exception class
    def __init__(self, error_message, error_detail: sys):
        # Initialize the base Exception class with the provided error message
        super().__init__(error_message)

        # Generate and store the detailed error message
        self.error_message = error_message_details(error_message, error_detail=error_detail)
    
    def __str__(self):
        # When the exception object is printed, return the detailed error message
        return self.error_message
    
# # To check weather the code is properly working or not
# if __name__ == "__main__":
#     try:
#         # Example code that will intentionally cause a ZeroDivisionError
#         a = 1 / 0
#     except Exception as e:
#         # Log the exception occurrence
#         logging.info("Divide by Zero")

#         # Raise the custom exception with detailed error information
#         raise CustomException(e, sys)
