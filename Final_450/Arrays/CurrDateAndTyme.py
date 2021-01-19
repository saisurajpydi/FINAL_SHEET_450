import datetime 
def print_time():
    parser = datetime.datetime.now()
    return parser.strftime("%d-%m-%y %H %M %S")
print(print_time())