from avro.datafile import DataFileReader

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


logging.info("Should display this")
logging.warning("It does not display the info message above")
