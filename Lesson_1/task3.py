from datetime import timedelta

main = int(input("Your seconds: "))
unixtime = timedelta(seconds = main)
print('Time in hh:mm:ss: ', unixtime)