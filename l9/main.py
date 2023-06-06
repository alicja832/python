import module
import datetime
import logging
logging.basicConfig(filename="test.log",filemode='w',format='%(asctime)s %(message)s')
logger=logging.getLogger()
logger.setLevel(logging.ERROR)
logger.info('debug')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
try:
    module.fun_two('02242607223',datetime.date(2002,4,26),'kobieta')
except ValueError as ex1:
    print("error")
#samo raise-przekazuje wyjatek dalej-kiedy juz mam obiekt
try:
    s=module.average(False)
except ValueError as ex1:
    print("error")
logger.info(s)
try:
    module.karta('1234567898765437')
except ValueError as ex1:
    print("error")