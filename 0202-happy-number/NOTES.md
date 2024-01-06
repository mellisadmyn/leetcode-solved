**Pendekatan untuk mendapatkan setiap digit n**:
Sisa bagi (last_digit) adalah digit terakhir dari angka dan floor division (n) memberikan angka tanpa digit terakhir. Ini memungkinkan kita mendapatkan digit-digit dari angka n yang dimasukkan user.
​
Contoh **n = 252**
Digit terakhir: 252 % 10 menghasilkan 2.
Menghapus digit terakhir: 252 // 10 menghasilkan 25.
Digit terakhir dari 25: 25 % 10 menghasilkan 5.
Menghapus digit terakhir dari 25: 25 // 10 menghasilkan 2.
Digit terakhir dari 2: 2 % 10 menghasilkan 2.
Menghapus digit terakhir dari 2: 2 // 10 menghasilkan 0.
​
Jadi, kita telah mengambil setiap digit dari angka 252, yaitu 2, 5, dan 2, menggunakan pendekatan ini.