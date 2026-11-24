import json
import math


class GorevNoktasi:
    def __init__(self, ad, aciklama, enlem, boylam):
        self.ad = ad
        self.aciklama = aciklama
        self.enlem = enlem
        self.boylam = boylam

    def __str__(self):
        return f"{self.ad} - {self.aciklama} ({self.enlem}, {self.boylam})"


def haversine(n1, n2):
    R = 6371000

    enlem1 = math.radians(n1.enlem)
    enlem2 = math.radians(n2.enlem)

    boylam1 = math.radians(n1.boylam)
    boylam2 = math.radians(n2.boylam)

    enlem_farki = enlem2 - enlem1
    boylam_farki = boylam2 - boylam1

    a = (math.sin(enlem_farki / 2) ** 2
         + math.cos(enlem1) * math.cos(enlem2)
         * math.sin(boylam_farki / 2) ** 2)

    mesafe = 2 * R * math.asin(math.sqrt(a))

    return mesafe


try:
    with open("gorevler.geojson", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)

    noktalar = []

    for feature in veri["features"]:
        ad = feature["properties"]["name"]
        aciklama = feature["properties"]["description"]

        if ad == "datum":
            continue

        boylam = feature["geometry"]["coordinates"][0]
        enlem = feature["geometry"]["coordinates"][1]

        nokta = GorevNoktasi(ad, aciklama, enlem, boylam)
        noktalar.append(nokta)

    print("Görev Noktaları:")

    for nokta in noktalar:
        print(nokta)

    print("\nNoktalar Arasındaki Mesafeler:")

    toplam_mesafe = 0

    for i in range(len(noktalar) - 1):
        mesafe = haversine(noktalar[i], noktalar[i + 1])

        toplam_mesafe += mesafe

        print(f"{noktalar[i].ad} -> {noktalar[i + 1].ad}: {mesafe:.2f} metre")

    print(f"\nToplam rota uzunluğu: {toplam_mesafe:.2f} metre")

except FileNotFoundError:
    print("gorevler.geojson dosyası bulunamadı.")
