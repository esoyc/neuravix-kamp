# Görev Noktası Okuyucu

NeuraVix Yazılım Eğitim Kampı 2. hafta Python projesi (Grup A - Temel Sürüm).

## Projenin Amacı

GeoJSON dosyasındaki görev noktalarını okumak, Haversine formülü ile noktalar arasındaki mesafeleri hesaplamak ve toplam rota uzunluğunu belirlemek.

## Kullanılan Modüller

- json
- math

## Çalıştırma

Python 3.12 gereklidir. Terminalde proje klasörüne girilerek aşağıdaki komut çalıştırılır:

`python main.py`

## Açıklama

Projede 1. gün kombinasyonlarından kombinasyon_001.geojson dosyası kullanılmıştır. Dosyanın adı gorevler.geojson olarak değiştirilmiştir.

Program görev noktaları arasındaki mesafeleri ve toplam rota uzunluğunu metre cinsinden ekrana yazdırır. Referans noktası olan datum, rota hesabına dahil edilmez.
