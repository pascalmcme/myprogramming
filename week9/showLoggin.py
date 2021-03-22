import logging
#logging.basicConfig(level=logging.INFO) # if we want to show different levels. 
logging.basicConfig(filename = "./debugging.log",filemode = "w",level=logging.DEBUG,


)

logging.error("this is an error") #
logging.critical("critical!")  #
logging.warning("warning!") # These run by defauly
logging.info("still going")


