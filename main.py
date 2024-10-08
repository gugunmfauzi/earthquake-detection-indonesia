"""
Aplikasi Deteksi Gempa BMKG.go.id
"""

import deteksigempa

gempa_di_indonesia = deteksigempa.deteksigempa('https://bmkg.go.id')
gempa_di_indonesia.tampilkan_keterangan()
gempa_di_indonesia.run()