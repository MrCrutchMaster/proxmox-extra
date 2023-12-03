from os import popen
stream = popen('top -c')
output = stream.read()
print(output)