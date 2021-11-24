import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# not important to understand just put at the top when logging

#logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# saves all logging information in myProgamLog.txt

# logging.disable(logging.CRITICAL)
# disables all logging statements at the CRITICAL level and below

logging.debug('Start of program')

def factorial(n): # wrong
    logging.debug('Start of facotrial(%s)' %(n))
    total = 1
    for i in range(n+1): # to make right - for i in  range(1,n+1):
        total*=i
        logging.debug('i is %s, total is %s' %(i, total))

    logging.debug('Return value is %s'%(total))
    return total

print(factorial(5))

logging.debug('End of program')

# Basically just a red print statement
# But you can call logging.disable(logging.CRITICAL) at the top to disable them all

# log levels in order from lowest to highest

# debug
# info
# warning
# error
# critical
