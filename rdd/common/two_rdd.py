import common.basic as basic

class two_rdd ():

    def __init__ (self):
        self.lines = basic.create_rdd('GitHubLog.txt')
