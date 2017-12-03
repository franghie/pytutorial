import logging

#logging to file
# debug
# info
# warn
# error
logging.basicConfig(filename='example.log', format='%(asctime)s %(levelname)-8s %(message)s ', level=logging.INFO)

logging.debug("i put cable into the bag")
logging.info("we need to attend prayer meeting")
logging.warning("no milk")
logging.error("gas stove is not working")