import pyfiglet


def print_welcome_message():    
    print("\n")
    result = pyfiglet.figlet_format("Stupefy", font="roman")
    print(result)

def print_progress_bar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    #the number of iterations and the total is required
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)

    if iteration == total: 
        print()