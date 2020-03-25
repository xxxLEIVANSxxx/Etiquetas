import Pyro4
import random

quantidade = 100
bilhetes = random.sample(range(1000,9999), quantidade)

@Pyro4.expose
class Bilhetadora(object):
  def pegar_bilhete(self):
	return bilhetes.pop(len(bilhetes)-1)

daemon = Pyro4.Daemon()
uri = daemon.register(Bilhetadora)

print("Ready. Object uri =", uri)
daemon.requestLoop()