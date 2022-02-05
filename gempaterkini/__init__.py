import requests
from bs4 import BeautifulSoup


def ekstraksi_data():

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        tanggal = soup.find(class_='waktu')
        magnitudo = soup.find(class_='ic magnitude').next_sibling
        kedalaman = soup.find(class_='ic kedalaman').next_sibling
        lokasi = soup.find(class_='ic koordinat').next_sibling
        pusat = soup.find(class_='ic lokasi').next_sibling
        dirasakan = soup.find(class_='ic dirasakan').next_sibling

        hasil = dict()
        hasil['tanggal'] = tanggal.text.split(',')[0]
        hasil['waktu'] = tanggal.text.split(',')[1]
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['lokasi'] = lokasi
        hasil['pusat'] = pusat
        hasil['dirasakan'] = dirasakan
        return hasil

    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data")
        return
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"{result['pusat']}")
    print(f"{result['dirasakan']}")

if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)
