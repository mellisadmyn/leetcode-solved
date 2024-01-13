Fungsi `is_alphanumeric` digunakan untuk memeriksa apakah suatu karakter dalam string adalah karakter alphanumeric atau tidak. Dalam konteks penyelesaian masalah ini, kita ingin memastikan bahwa kita hanya mempertimbangkan huruf (baik huruf besar maupun kecil) dan angka dalam string, sementara mengabaikan karakter-karakter lain seperti spasi atau tanda baca. Fungsi ini mengembalikan nilai `True` jika karakter yang diberikan adalah huruf atau angka, dan `False` jika tidak. 

`s = "A man, a plan, a canal: Panama"`

Indeks 0: 'A'
Indeks 1: ' '
Indeks 2: 'm'
Indeks 3: 'a'
Indeks 4: 'n'
Indeks 5: ','
Indeks 6: ' '
Indeks 7: 'a'
Indeks 8: ' '
Indeks 9: 'p'
Indeks 10: 'l'
Indeks 11: 'a'
Indeks 12: 'n'
Indeks 13: ','
Indeks 14: ' '
Indeks 15: 'a'
Indeks 16: ' '
Indeks 17: 'c'
Indeks 18: 'a'
Indeks 19: 'n'
Indeks 20: 'a'
Indeks 21: 'l'
Indeks 22: ':'
Indeks 23: ' '
Indeks 24: 'P'
Indeks 25: 'a'
Indeks 26: 'n'
Indeks 27: 'a'
Indeks 28: 'm'
Indeks 29: 'a'


1. **Iterasi Pertama**:
    - Pointer `left` diatur di awal string (indeks 0).
    - Pointer `right` diatur di akhir string (indeks len(s) - 1).

	 Contoh: left (indeks 0) = A dan right (indeks 29) = a, karena ini tidak memenuhi 2 kondisi while diawal, maka kita akan masuk ke if statement dimana kita akan compare dan mengabaikan jika berbeda upper case atau lower case, karena ini huruf yang sama maka kita akan lanjut dengan compute left += 1 dan right -= 1

2. **Iterasi Kedua**:
    - Pointer `left` + 1 = 0 + 1 = 1
    - Pointer `right` - 1 = 29 - 1 = 28

	 Contoh: left (indeks 1) = spasi dan right (indeks 28) = m, karena ini memenuhi kondisi while yang pertama, maka kita akan masuk ke while statement dimana kita akan compute left += 1 sehingga menjadi `left` + 1 = 1 + 1 = 2 di iterasi ketiga

3. **Iterasi Ketiga**:
    - Pointer `left` + 1 = 1 + 1 = 2
    - Pointer `right`  - 1 = 29 - 1 = 28

	 Contoh: left (indeks 2) = m dan right (indeks 28) = m, karena ini tidak memenuhi 2 kondisi while diawal, maka kita akan masuk ke if statement dimana kita akan compare dan mengabaikan jika berbeda upper case atau lower case, karena ini huruf yang sama maka kita akan lanjut dengan compute left += 1 dan right -= 1

Selama proses ini, pointer terus bergerak ke arah tengah, mencari karakter huruf atau angka untuk dibandingkan. Langkah-langkah ini terus berlanjut sampai pointer kiri dan kanan bertemu atau saling melampaui. Jika selama proses ini tidak ditemukan pasangan huruf yang tidak cocok, hasilnya adalah `True` dan string dianggap palindrom.