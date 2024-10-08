import requests
from bs4 import BeautifulSoup
"""
Method = fungsi
filed/atribute = variable
"""

class deteksigempa:
    def __init__(self, url):
        self.Description = 'To get lastest information eathquake from BMKG.go.id'
        self.result = None
        self.url = url

    def ekstraksi_data(self):
        """
        Tanggal : 21 September 2024
        Waktu : 06:26:20 WIB
        Magnitudo : 4.8
        Kedalaman : 22 km
        Lokasi : LS=8.57 BT=115.32
        Pusat gempa : berada di darat 3 km baratdaya Gianyar
        Dirasakan : (Skala MMI): IV Gianyar, III Badung, III Denpasar, III Tabanan, III Karangasem, III Bangli, II Buleleng, II Mataram, II Lombok Barat
        :return:
        """
        try:
            content = requests.get(self.url)
        except Exception:
            return None
        if content.status_code == 200:
            # print(content.text)
            soup = BeautifulSoup(content.text, 'html.parser')

            result = soup.find('span', {'class': 'waktu'})
            Waktu = result.text.split(',') [1]
            Tanggal = result.text.split(',')[0]

            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')
            i = 0
            Magnitudo = None
            LS = None
            BT = None
            Dirasakan = None

            for res in result:
                if i ==1:
                    Magnitudo = res.text
                elif i == 2:
                    Kedalaman = res.text
                elif i == 3:
                    Koordinat = res.text.split(' - ')
                    LS = Koordinat[0]
                    BT = Koordinat[1]
                elif i == 4:
                    Lokasi = res.text
                elif i == 5:
                    Dirasakan = res.text
                i = i + 1
            # Magnitudo = 0

            hasil = dict()
            hasil['Tanggal'] = Tanggal
            hasil['Waktu'] = Waktu
            hasil['Magnitudo'] = Magnitudo
            hasil['Kedalaman'] = Kedalaman
            hasil['Lokasi'] = Lokasi
            hasil['Koordinat'] = {'LS': LS, 'BT': BT}
            hasil['Dirasakan'] = Dirasakan
            self.result = hasil
        else:
            return None

    def tampilkan_data(self):
        if self.result is None:
            print("Tidak bisa menemukan data gempa terkini")

        print('Gempa Terkahir Berdasarkan BMKG')
        print(f"Tanggal {self.result['Tanggal']}")
        print(f"Waktu {self.result['Waktu']}")
        print(f"Magnitudo {self.result['Magnitudo']}")
        print(f"Kedalaman {self.result['Kedalaman']}")
        print(f"Lokasi {self.result['Lokasi']}")
        print(f"Koordinat: LS={self.result['Koordinat']['LS']}, BT={self.result['Koordinat']['BT']}")
        print(f"Dirasakan {self.result['Dirasakan']}")

    def run(self):
        self.ekstraksi_data()
        self.tampilkan_data()

if __name__ == '__main__':
    gempa_di_indonesia = deteksigempa('https://bmkg.go.id')
    print('Description', gempa_di_indonesia.Description)
    gempa_di_indonesia.run()
    # gempa_di_indonesia.ekstraksi_data()
    # gempa_di_indonesia.tampilkan_data()