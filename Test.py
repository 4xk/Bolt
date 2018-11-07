import Bolt

token = "Your Token"
bolt = Bolt.Bolt() #Create bolt instance
instance = bolt.newInstance() #create new bot instance, used to connect to channels
instance.connect(token=token, botname="Bot account username", channel='Channel to connect to') #add channel to connect to, doesnt connect immediately
instance.go() #connects to all the channels 