class Env(object):
    def __init__(self, DevEnv, ProdEnv):
        self.dev = DevEnv
        self.prod = ProdEnv

    def __str__(self):
        return "{0} {1}".format(self.dev, self.prod)

class AppSetting(object):
    def __init__(self, test, ServerConfig):
        self.test = test
        self.serverEnv = Env(**ServerConfig)
    def __str__(self):
        return f"{self.test},{self.serverEnv}"
        #return "{0} ,{1}".format(self.test, self.serverEnv, self.youtubeService)
    