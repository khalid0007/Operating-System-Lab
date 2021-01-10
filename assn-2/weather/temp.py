# importing libraries 
import subprocess 
import os 

temp = subprocess.Popen(['find', './fifo', '-type',  'p'], stdout = subprocess.PIPE)
# output = list(map(lambda x: x.lstrip('.').lstrip('/'), temp.communicate()[0].decode('utf-8')))

output = str(temp.communicate()[0].decode('utf-8'))
output = list(filter(lambda x: len(x) > 0, map(lambda x: x.lstrip('.').lstrip('/'), output.split('\n'))))
# print(temp.communicate()[0].decode('utf-8'))


print(output)