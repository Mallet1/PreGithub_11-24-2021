import traceback

"""

************
*          *
*          *
*          *
************


"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if width<2 or height<2:
        raise Exception('"width" and "height" must be greater than or equal than 2.')
    
    print(symbol*width)

    for i in range(height-2):
        print(symbol+(' ' *(width-2))+symbol)

    print(symbol*width)


boxPrint('*',5,5)

# raise Exception('This is the error message.')
# Used to find bugs

try:
    raise Exception('This is the error message.') # makes generic error message
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc()) # writes the error message in error_log.txt in the cwd
    errorFile.close()
    print('The traceback info was written to error_log.txt')

# assert condition, 'error message' if condition is false returns error message
# assert statement syntax ^

market_2nd={'ns': 'green', 'ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key]=='green':
            intersection[key]='yellow'
        elif intersection[key]=='yellow':
            intersection[key]='red'
        elif intersection[key]=='red':
            intersection[key]='green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

# asserts are for programmer errors not user errors
# raise Exception used for user errors
# both will usually work
