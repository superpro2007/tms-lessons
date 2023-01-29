seconds = int(input())
minutes = seconds // 60
seconds %= 60
print(str(minutes) + ':' + str(seconds))