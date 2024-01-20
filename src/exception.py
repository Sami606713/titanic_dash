import sys
from src.logger import logging
# Error Message Detail
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message=f"Error message name is [{file_name}] in line no [{exc_tb.tb_lineno}] error message [{str(error)}]"

    return error_message

# Coustom Exception
class Coustom_exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message

# if __name__=="__main__":
#     try:
#         n=samillah
#     except Exception as e:
#         logging.info("Exception occur")
#         raise Coustom_exception(e,sys)