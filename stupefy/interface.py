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

def print_quota_warning(total):
    print("\nSorry bud, we really wanted to convert all your %d songs, but due to Youtube limitations we can only do 50 songs a day" % total)
    print("We can still convert the first 50 tracks tho, so it's not that bad! :)\n")
    answer = input("Do you still want it? Y/N\n")

    return answer

def print_goodbye():
    print("\nThanks for using Stupefy, see you later\n")
