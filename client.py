import Pyro4

uri = input("URI Object? ").strip()
for i in range(4):
    print("Pegando um bilhete")
    bilhetadora = Pyro4.Proxy(uri)
    bilhete_atual = bilhetadora.pegar_bilhete()
    print("Pegou o bilhete numero: " + str(bilhete_atual))