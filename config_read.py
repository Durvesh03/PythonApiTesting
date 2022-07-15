from configparser import ConfigParser

config = ConfigParser()

#read from config file
#config.read('C:\\Users\\Durvesh\\PycharmProjects\\pythonProject\\Config.cfg')
config.read('.\\Config.cfg') #to make the path dynamic (./ or .\\ means current project)
print(config.get('Section', 'username'))