def outahere():
    import os
    print('bye os world')
    os._exit(99)
    print('never reached')

if __name__ == '__main__':
    outahere()
