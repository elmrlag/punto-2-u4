import urllib, json
from urllib.request import urlopen

url = "https://www.dolarsi.com/api/api.php?type=dolar"

response = urlopen(url)
data = json.loads(response.read())

for i in data:
    if (i["casa"]["nombre"] == "Oficial"):
        print("VALOR OFICIAL ENCONTRADO")
        OficialVenta = i["casa"]["venta"]
        aux = OficialVenta.split(",")
        aux1 = float(aux[0])
        aux2 = float(aux[1])/1000
        OficialVenta = float(aux1 + aux2)


