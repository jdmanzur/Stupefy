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


def print_quota_error_message():
    print("\nOh, no! We're so sorry buddy, but we can only do 50 songs a day due to Youtube limitations, the previous songs converted until now are present in the playlist you created,  but we can't convert anymore songs. We are terribly sorry and hope you had a nice experience the same way")
    print("You can still try it out another day, huh? Hope to see you soon...")