@echo off

rem Hapus file di folder dist/ jika ada
echo Menghapus file lama di folder dist/...
rmdir /s /q dist

rem Build package baru
echo Membuat distribusi package...
python setup.py sdist bdist_wheel

rem Upload package ke PyPI
echo Mengunggah package ke PyPI...
twine upload dist/*

echo Proses selesai.
