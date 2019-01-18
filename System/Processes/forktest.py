import os

pid = os.fork()
if pid != 0:
    print('parent\n')
else:
    print('child\n')

print('exiting')
